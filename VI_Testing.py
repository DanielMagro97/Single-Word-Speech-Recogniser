import scipy.io.wavfile    # for reading wav file
from Assignment.IV_ExtractMFCCs import mfcc_extract # for MFCC extraction
from sklearn.externals import joblib    # for loading the GMMs
import os       # for file functions


# Loading the GMMs from disk
gmm_bass = joblib.load('training//bass//gmm_bass.pkl')
gmm_drum = joblib.load('training//drum//gmm_drum.pkl')
gmm_guitar = joblib.load('training//guitar//gmm_guitar.pkl')
gmm_piano = joblib.load('training//piano//gmm_piano.pkl')
gmm_violin = joblib.load('training//violin//gmm_violin.pkl')


def score_gmm(data, gmm):
    log_likelihood = gmm.score(X=data)
    return log_likelihood


# Looping over Test data
for file in os.listdir('testing'):
    filename = os.fsdecode(file)
    # if the file extension is .wav (i.e. if it is a sound file)
    if filename.endswith(".wav"):
        # read the sound file
        fs, data = scipy.io.wavfile.read('testing//' + filename)
        # extract the MFCCs for that sound file
        mfccs = mfcc_extract(signal=data, fs=fs)
        # score the MFCCs under each GMM
        scores = [gmm_bass.score(mfccs), gmm_drum.score(mfccs), gmm_guitar.score(mfccs), gmm_piano.score(mfccs), gmm_violin.score(mfccs)]

        # printing what word the sound file is saying is based on the highest score
        if scores.index(max(scores)) == 0:
            print(filename + ' is saying bass')
        elif scores.index(max(scores)) == 1:
            print(filename + ' is saying drum')
        elif scores.index(max(scores)) == 2:
            print(filename + ' is saying guitar')
        elif scores.index(max(scores)) == 3:
            print(filename + ' is saying piano')
        elif scores.index(max(scores)) == 4:
            print(filename + ' is saying violin')

        continue
    else:
        continue