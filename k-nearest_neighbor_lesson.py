# k-nearest_neighbor_lesson.py
# demo of k-nearest neighbor
# https://docs.opencv.org/4.x/d5/d26/tutorial_py_knn_understanding.html
# 7/16/22

import cv2
import numpy as np
import matplotlib.pyplot as plt

# seed
# np.random.seed(12020199)

# create feature set containing (x,y) values of 25 known/training data
numData = 15
trainData = np.random.randint(0, 100, (numData, 2)).astype(np.float32)

# label each one either as Red or Blue with numbers 0 and 1
responses = np.random.randint(0, 2, (numData, 1)).astype(np.float32)

# take the Red neighbors and plot them
red = trainData[responses.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

# take the Blue neighbors and plot them
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', marker='s')  # s = square

# add newcomer data  (marked in green)
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'magenta', 'o')

# determine where this newcomer belongs to, red or blue?
k = 5
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, dist = knn.findNearest(newcomer, k)

print("result (0=red, 1=blue): {} ".format(results))
print("nearest neighbors (0=red, 1=blue): {} ".format(neighbours))
print("distances: {} ".format(dist))
print("k: {}".format(k))

# plot newcomer
plt.show()
