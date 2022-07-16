# k-means_multiple_lesson.py
# multiple features k-means
# 7/16/22

import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence

# rs = RandomState(MT19937(SeedSequence(123456789)))
# np.random.seed(3434425800)
X = np.random.randint(1, 1000, (10, 2))
Y = np.random.randint(1, 1000, (10, 2))
Z = np.vstack((X, Y))
Z = np.float32(Z)

# define criteria and apply kmeans
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, 3, None, criteria, attempts=100, flags=None, centers=cv2.KMEANS_RANDOM_CENTERS)

# now separate the data, note the flatten()
A = Z[label.ravel() == 0]
B = Z[label.ravel() == 1]
C = Z[label.ravel() == 2]
D = Z[label.ravel() == 3]

# plot the data
plt.scatter(A[:,0], A[:,1], c='magenta')
plt.scatter(B[:,0], B[:,1], c='darkred')
plt.scatter(C[:,0], C[:,1], c='teal')
plt.scatter(D[:,0], D[:,1], c='mediumpurple')

plt.scatter(center[:,0], center[:,1], s=80, c='red', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()


