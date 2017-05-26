from __future__ import print_function

import pickle
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from scipy.io import loadmat as load
from preprocess import Preprocess

kmeans = MiniBatchKMeans(n_clusters=100, init='k-means++',verbose=0).fit(pickle.load(open('sift_scaled.pickle', 'rb')))
pickle.dump(kmeans, open('sift_kmeans_scaled.pickle', 'wb'))