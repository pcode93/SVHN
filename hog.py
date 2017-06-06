from __future__ import print_function

import math
import scipy
from scipy.io import loadmat as load
import numpy as np
import matplotlib.pyplot as plt

import mlp
from preprocess import Preprocess

(x_train, y_train) = Preprocess(load('train_32x32.mat')).rgb2gray().uint8().hog().get()

(x_test, y_test) = Preprocess(load('test_32x32.mat')).rgb2gray().uint8().hog().get()

(x_valid, y_valid) = (x_train[math.floor(0.8*len(x_train)):,:], y_train[math.floor(0.8*len(y_train)):,:])
(x_train, y_train) = (x_train[:math.floor(0.8*len(x_train)),:], y_train[:math.floor(0.8*len(y_train)),:])

print(x_train.shape[0], 'train samples')
print(x_valid.shape[0], 'validation samples')
print(x_test.shape[0], 'test samples')

(name, model) = mlp.create_mlp(np.shape(x_train)[1], 1e-5, ('tanh', 784, 0.2))

mlp.train_mlp(model, 100, x_train, y_train, x_valid, y_valid)
mlp.test_mlp(model, x_test, y_test)

w = np.squeeze(model.layers[0].get_weights())
hw = w[0].T
n=10
plt.figure(figsize=(50, 8))
for i in range(n):
    ax = plt.subplot(5, n, i + 1)
    plt.imshow(hw[i].reshape(27, 27))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(5, n, i + 1 + n)
    plt.imshow(hw[i+n].reshape(27, 27))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(5, n, i + 1 + n + n)
    plt.imshow(hw[n+n+i].reshape(27, 27))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(5, n, i + 1 + n + n + n)
    plt.imshow(hw[n+n+i+n].reshape(27, 27))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(5, n, i + 1 + n + n +n +n)
    plt.imshow(hw[n+n+i+n+n].reshape(27, 27))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()