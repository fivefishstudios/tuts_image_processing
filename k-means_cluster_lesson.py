# k-means_cluster_lesson
# 7/16/22

import numpy as np
import cv2
from matplotlib import pyplot as plt

x = np.random.randint(0, 125, size=50)
y = np.random.randint(126, 255, 50)

z = np.hstack([x, y])
z = z.reshape((len(x) + len(y), 1))
z = np.float32(z)

# visualize data
plt.hist(z, 512, [0, 256])
plt.show()

# define criteria for k-means
# (type, max_iter = 10, epsilon = 1.0)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# set flags
flags = cv2.KMEANS_RANDOM_CENTERS

# apply kmeans
compactness, labels, centers = cv2.kmeans(z, K=2, bestLabels=None, criteria=criteria, attempts=10, flags=flags)

# filters the z based on whether its 0 or 1
A = z[labels == 0]
B = z[labels == 1]

# plot
plt.hist(A, 256, [0,256], color='r')
plt.hist(B, 256, [0,256], color='b')
plt.hist(centers, 32, [0,256], color='y')
plt.show()

