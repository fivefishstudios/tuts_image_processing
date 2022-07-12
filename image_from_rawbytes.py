# image_from_rawbytes.py
# random raw bytes to either grayscale or color image
# 7/7/22

import cv2
import numpy
import os

randomBytes = bytearray(os.urandom(120000))

flat_np_array = numpy.array(randomBytes)

# create gray scale random image
image_gray = flat_np_array.reshape(300,400)
cv2.imshow('Gray', image_gray)
cv2.waitKey(0)

# create color random image
image_color = flat_np_array.reshape(200,200,3)
cv2.imshow('Color', image_color)
key = cv2.waitKey(0)
print(key)

exit(0)

