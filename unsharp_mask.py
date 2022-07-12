# unsharp_mask.py 
# Canny Processing of video
# 6.24.22 

import cv2
import numpy as np 

img = cv2.imread('./erin-robin.JPG')
img_watermark = cv2.imread('./test1.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# unsharp mask
img_smoothed = cv2.GaussianBlur(img,(35,35),140)
img_unsharp = cv2.addWeighted(img, 1.4, img_smoothed, -0.5, 0)

img_with_mark = img.copy()
cv2.bitwise_or(img_watermark, img_watermark, img_with_mark)

# display photo
ret = cv2.imshow('Original',img)
cv2.waitKey(0)

# ret = cv2.imshow('Smoothed',img_smoothed)
# cv2.waitKey(0)
#
# ret = cv2.imshow('Unsharp/Sharpened',img_unsharp)
# cv2.waitKey(0)

ret = cv2.imshow('Watermark',img_with_mark)
cv2.waitKey(0)