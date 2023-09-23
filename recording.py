import pyaudio  # module for recording raw music
import base64  # module to convert raw binary file to base64- format that is
# needed in request according to documentation of an API
import time
from files import write_to_file
from utils import headers, BASE_URL, ENDPOINTS
from request import get_response


def get_frames(output_file):
    # data format needed for request according to documentation of an API
    # only file_format will change
    chunk = 1024
    file_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(
        format=file_format, channels=channels, rate=rate,
        frames_per_buffer=chunk, input=True
    )
    print("Play your music, recording will start in 3 seconds...")
    time.sleep(3)
    print("Recording started...")

    frames = []
    # sometimes it's too short (Shazam usually gets 20s of recording)
    # but API won't handle larger requests and send 413 error response
    seconds = 8

    for _ in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording stopped")
    stream.stop_stream()
    stream.close()
    p.terminate()

    write_to_file(output_file, b"".join(frames), "wb")
    print(f"Raw recording saved to {output_file}")


def convert_raw_to_base64():
    get_frames("recorded.raw")
    time.sleep(3)
    with open("recorded.raw", "rb") as file:
        audio_raw = file.read()
        audio_encoded = base64.b64encode(audio_raw)
        write_to_file("recorded.txt", audio_encoded, "wb")
        print("Base64 recording saved to recorded.txt, waiting for results...")
        return audio_encoded


def get_details_from_recording():
    decoded_frames = convert_raw_to_base64()
    headers["content-type"] = "text/plain"
    response = get_response("POST", BASE_URL + ENDPOINTS["DETECT"],
                            headers=headers, data=decoded_frames)
    if response.status_code == 200 and len(response.json()['matches']) > 0:
        details = response.json()['track']['sections']
        print(f"Title: {details[0]['metadata'][0]['text']}, ")
        print(f"\nArtist: {details[0]['metapages'][0]['caption']}, ")
        if 'text' in details[1]:
            song_text = details[1]['text']
            print("\nSong text: \n")
            for line in song_text:
                print(line)
                write_to_file("reversed_song_book.txt", f"{line[::-1]}\n", "a")
    elif len(response.json()['matches']) == 0:
        print("Your music fragment was too short, we couldn't find a match,")
        print(" try again...")
        print("We are going to start recording again in 3 seconds")
        time.sleep(3)
        get_details_from_recording()
