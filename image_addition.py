# image_addition.py
# adding a scalar to an image 
# 6.26.22 

import cv2
import numpy as np 

img = cv2.imread('./bball.jpg')
print(img.shape)

scalar = np.ones((img.shape), dtype="uint8") * 2
# print(scalar)

img_add = cv2.add(img, scalar)
img_subtract = cv2.subtract(img, scalar)
img_multiply = cv2.multiply(img, scalar)
img_divide = cv2.divide(img, scalar)

np.ar

# display
ret = cv2.imshow('orig', img)
cv2.waitKey(0)
# cv2.destroyWindow('orig')
ret = cv2.imshow('added', img_add)
cv2.waitKey(0)
ret = cv2.imshow('subtract', img_subtract)
cv2.waitKey(0)
ret = cv2.imshow('multiply', img_multiply)
cv2.waitKey(0)
ret = cv2.imshow('divide', img_divide)
cv2.waitKey(0)

cv2.destroyAllWindows()

