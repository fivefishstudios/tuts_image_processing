# contrastImage.py
# demo program to adjust contrast of either grayscale or color image
# 7/12/22

import cv2
from contrast import Contrast

img = cv2.imread('./images/parktree-dark.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('Original', img)
cv2.waitKey()

myContrast = Contrast(img)

img_contrast = myContrast.adjustContrast()

cv2.imshow('Output', img_contrast)
cv2.waitKey()

cv2.destroyAllWindows()