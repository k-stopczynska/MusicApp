import pyaudio
import base64
import time
from files import write_to_file

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def get_frames(output_file):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, frames_per_buffer=CHUNK, input=True
    )
    print("Recording started...")

    frames = []
    seconds = 2

    for _ in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    write_to_file(output_file, b"".join(frames))
    print(f"Recording saved to {output_file}.")


def convert_raw_to_base64():
    get_frames("recorded.raw")
    time.sleep(3)
    with open("recorded.raw", "rb") as file:
        audio_raw = file.read()
        audio_encoded = base64.b64encode(audio_raw)
        file.close()
        write_to_file("recorded.txt", audio_encoded)
        print("Recording saved to recorded.txt.")
        return audio_encoded
