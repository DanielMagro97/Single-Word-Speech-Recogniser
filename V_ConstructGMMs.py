import numpy
from sklearn.externals import joblib    # for saving the GMMs
from sklearn.mixture import GaussianMixture #scikit-learn


# Loading the MFCCs for each word from disk
mfccs_bass = numpy.load('training//bass//mfccs_bass.npy')
mfccs_drum = numpy.load('training//drum//mfccs_drum.npy')
mfccs_guitar = numpy.load('training//guitar//mfccs_guitar.npy')
mfccs_piano = numpy.load('training//piano//mfccs_piano.npy')
mfccs_violin = numpy.load('training//violin//mfccs_violin.npy')


# Defining a function which takes the MFCCs as a parameter(input) and returns the GMM(output)
def gmm_construct(data, n_components=1):
    gmm = GaussianMixture(n_components=n_components,
                          covariance_type='diag',
                          tol=0.001,
                          reg_covar=1e-06,
                          max_iter=100,
                          n_init=1,
                          init_params='kmeans',
                          warm_start=False,
                          verbose=0,
                          verbose_interval=10)
    gmm.fit(X=data)
    return gmm


# Initializing gmm_<word> to the output of the gmm_construct function
k = 16
gmm_bass = gmm_construct(mfccs_bass, n_components=k)
gmm_drum = gmm_construct(mfccs_drum, n_components=k)
gmm_guitar = gmm_construct(mfccs_guitar, n_components=k)
gmm_piano = gmm_construct(mfccs_piano, n_components=k)
gmm_violin = gmm_construct(mfccs_violin, n_components=k)


# Saving the GMMs to disk
joblib.dump(gmm_bass, 'training//bass//gmm_bass.pkl')
joblib.dump(gmm_drum, 'training//drum/gmm_drum.pkl')
joblib.dump(gmm_guitar, 'training//guitar//gmm_guitar.pkl')
joblib.dump(gmm_piano, 'training//piano//gmm_piano.pkl')
joblib.dump(gmm_violin, 'training//violin//gmm_violin.pkl')

print("GMMs have been constructed and saved to disk")