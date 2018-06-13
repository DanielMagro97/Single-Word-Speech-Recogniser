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
    choice = eval(input("Would you like to record training data for:\n"
                 "1) Bass\n"
                 "2) Drum\n"
                 "3) Guitar\n"
                 "4) Piano\n"
                 "5) Violin\n"))

    # Recording a speech training file based upon which option the user selected
    if choice == 1:
        print("Recording Training Data for Bass")
        wavrecord(fs=8000, duration=10, output_filename="training//bass//bass-training.wav")
    elif choice == 2:
        print("Recording Training Data for Drum")
        wavrecord(fs=8000, duration=10, output_filename="training//drum//drum-training.wav")
    elif choice == 3:
        print("Recording Training Data for Guitar")
        wavrecord(fs=8000, duration=10, output_filename="training//guitar//guitar-training.wav")
    elif choice == 4:
        print("Recording Training Data for Piano")
        wavrecord(fs=8000, duration=10, output_filename="training//piano//piano-training.wav")
    elif choice == 5:
        print("Recording Training Data for Violin")
        wavrecord(fs=8000, duration=10, output_filename="training//violin//violin-training.wav")
    else:
        print("Invalid option")
