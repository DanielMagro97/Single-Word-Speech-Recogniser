import scipy.io.wavfile
import python_speech_features
import numpy


# Function which can be called to exctract MFCCs
def mfcc_extract(signal, fs=8000):
    mfccs = python_speech_features.mfcc(
        signal=signal, samplerate=fs, winlen=0.025,
        winstep=0.01, numcep=13, nfilt=26, nfft=512,
        lowfreq=0, highfreq=None, preemph=0.97,
        ceplifter=22, appendEnergy=True
    )
    return mfccs


# Extracting MFCCs from the five training sound (.wav) files
fs1, data1 = scipy.io.wavfile.read('training//bass//bass-training.wav')
mfccs_bass = mfcc_extract(signal=data1, fs=fs1)

fs2, data2 = scipy.io.wavfile.read('training//drum//drum-training.wav')
mfccs_drum = mfcc_extract(signal=data2, fs=fs2)

fs3, data3 = scipy.io.wavfile.read('training//guitar//guitar-training.wav')
mfccs_guitar = mfcc_extract(signal=data3, fs=fs3)

fs4, data4 = scipy.io.wavfile.read('training//piano//piano-training.wav')
mfccs_piano = mfcc_extract(signal=data4, fs=fs4)

fs5, data5 = scipy.io.wavfile.read('training//violin//violin-training.wav')
mfccs_violin = mfcc_extract(signal=data5, fs=fs5)


# Saving the MFCCs as a Binary File
numpy.save('training//bass//mfccs_bass.npy', mfccs_bass)
numpy.save('training//drum//mfccs_drum.npy', mfccs_drum)
numpy.save('training//guitar//mfccs_guitar.npy', mfccs_guitar)
numpy.save('training//piano//mfccs_piano.npy', mfccs_piano)
numpy.save('training//violin//mfccs_violin.npy', mfccs_violin)

print("MFCCs have been extracted and saved to disk.")