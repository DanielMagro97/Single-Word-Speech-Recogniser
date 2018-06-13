import pyaudio # via pip install
import wave


def wavrecord(fs=8000,duration=10,output_filename="sound.wav"):
    """
    Record mono wav data from system microphone
    :param fs: Sampling frequency (Hz)
    :param duration: Duration of recording (seconds)
    :param output_filename: Absolute path of wav file to be written
    :return:
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = fs
    RECORD_SECONDS = duration

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Done!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(output_filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


if __name__ == '__main__':
    name = input("What would you like to name this .wav file? ")
    # Recording a speech file, named according to the user's input
    wavrecord(fs=8000, duration=2, output_filename= ("testing//" + name + ".wav") )