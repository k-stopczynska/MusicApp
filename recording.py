import pyaudio
import base64
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def get_frames(output_file):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, frames_per_buffer=CHUNK, input=True
    )
    print("Recording started, precc Ctrl + c to stop")

    frames = []
    seconds = 8
    # try:
    for _ in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    # except KeyboardInterrupt:
    #     pass

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with open(output_file, "wb") as file:
        file.write(b"".join(frames))
        file.close()
    print(f"Recording saved to {output_file}.")


def convert_raw_to_base64():
    get_frames("recorded.raw")
    time.sleep(3)
    with open("recorded.raw", "rb") as file:
        audio_raw = file.read()
        audio_encoded = base64.b64encode(audio_raw)
        file.close()
        with open("recorded.txt", "wb") as file:
            file.write(audio_encoded)
            file.close()
        return audio_encoded
