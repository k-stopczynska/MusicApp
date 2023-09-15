import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def get_frames():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, frames_per_buffer=CHUNK, input=True
    )
    print("start recording...")
    # frames = []
    seconds = 3
    for i in range(0, int(RATE / CHUNK * seconds)):
        frames = stream.read(CHUNK)
        # print(data)
        # frames.append(data)
  
    print("recording stopped")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return frames, p


# def download_recording():
#     frames, p = get_frames()
#     wf = wave.open("recording.wav", "wb")
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b"".join(frames))
#     wf.close()

# download_recording()
