# alphatest.py
# test alpha blending using bitwise_and
# 7/11/22

import cv2
import numpy as np

image = cv2.imread('./ball.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread('./ball2.jpg', cv2.IMREAD_COLOR)
image_logo = cv2.imread('./alphalogo.png', cv2.IMREAD_UNCHANGED)

# scrap transparency
# image_logo = image_logo[:3]

print(image_logo.shape)
cv2.imshow('Logo', image_logo)
cv2.waitKey(0)
# get dimensions of logo
# lh, lw = image_logo.shape[:2]
# (b,g,r,a) = cv2.split(image_logo)
# b = cv2.bitwise_and(b,b, mask=a)
# g = cv2.bitwise_and(g,g, mask=a)
# r = cv2.bitwise_and(r,r, mask=a)
# image_logo = cv2.merge([b,g,r,a])

# temp space for output
output = image.copy()

# this produces an error because image and image_logo don't have the same size (i.e. including alpha channel)
# specificall, our image does not have an alpha channel
# so we need to add alpha channel to our original image so it matches depth size of our transparent logo image

h, w = image.shape[:2]  # get dimension of original image (we'll multiply wxh to get total # of elements to add as 4th channel
# image = np.dstack([image, np.ones((h, w), dtype='uint8') * 255])  # now we have a 4 channel PNG file with transparency channel

# we still have an error because our image and logo size are not the same, the logo is smaller in wxh
# let's create an empty image (same size as original image) so we can put the logo in the corner of that empty image
# watermark = np.zeros((h, w, 4), dtype='uint8')

# put our logo in corner of our watermark canvas
# watermark[h - lh: h, w - lw: w] = image_logo

image_logo = cv2.resize(image_logo,(h,w),interpolation=cv2.INTER_AREA)

# blend the original image and our watermark image
# cv2.addWeighted(image, 0.15, watermark, 1.0, 0, output)
# cv2.addWeighted(image, 0.8, image2, .2, 0, output)
cv2.addWeighted(image, 0.8, image_logo, .2, 0, output)

cv2.imshow('Logo', image_logo)
cv2.waitKey(0)

# cv2.imshow('Watermark', watermark)
# cv2.waitKey(0)

cv2.imshow('Output with Logo', output)
cv2.waitKey(0)
