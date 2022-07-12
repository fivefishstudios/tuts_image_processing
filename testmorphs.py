# testmorphs.py
# test erosion and dilation, using classes
# white areas either get eroded, or dilated.
# 7/12/22

import cv2
from morphs import MorphFilters
import numpy as np

image = cv2.imread('./images/morphology.jpg', cv2.IMREAD_UNCHANGED)

# (self, image: object, kernel: object, iterations: object = 1)

kernel = np.ones((3, 3), np.uint8)
iterations = 1

morph = MorphFilters(image, kernel, iterations)

# original
cv2.imshow('Original', image)
cv2.waitKey()

morph.erode()
morph.show('Erode')

morph.dilate()
morph.show('Dilate')

