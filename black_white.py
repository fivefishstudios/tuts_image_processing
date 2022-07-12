# black_white.py 
# exploring grayscale/black and white images  
# 6.24.22 
# Reference: https://towardsdatascience.com/practical-image-process-with-opencv-8405772c603e

import cv2

img = cv2.imread('./jetson nano.JPG')

#convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# process image
(tresh, img_treshold) = cv2.threshold(img_gray,127,255, cv2.THRESH_BINARY) # treshold, max value if pixel exceeds treshold value
print("Threshold return value: ", tresh )

# blurring
img_blur = cv2.blur(img, (111,321))  # (x movement, y movement)

#display
ret = cv2.imshow("Original", img)
cv2.waitKey(0)

# display processed image
# ret = cv2.imshow("Threshold", img_treshold)
# cv2.waitKey(0)

# display processed image
ret = cv2.imshow("Blur", img_blur)
cv2.waitKey(0)
