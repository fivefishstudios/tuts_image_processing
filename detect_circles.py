# detect_circles.py 
# Detect Circles in image
# 6.25.22 
# NOTE: I can't understand how all this works. Too many parameters

import cv2
import numpy as np 

img = cv2.imread('./bball.jpg')

# convert to gray
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# display
ret = cv2.imshow('Output', img_gray)
cv2.waitKey(0)

# apply image threshold to grayscale 
# (thresh, img_thresh) = cv2.threshold(img_gray, 145, 255, cv2.THRESH_BINARY)


# blur a bit
img_blur = cv2.GaussianBlur(img_gray, (13,13),15)
# display
ret = cv2.imshow('Output', img_blur)
cv2.waitKey(0)


# edge detect
img_edge = cv2.Canny(img_blur,10,85)
# display
ret = cv2.imshow('Output', img_edge)
cv2.waitKey(0)

circles = cv2.HoughCircles(img_edge,cv2.HOUGH_GRADIENT,1,150,param1=150,param2=50,minRadius=118,maxRadius=313)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),6)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

# display
ret = cv2.imshow('Output', img)
cv2.waitKey(0)

cv2.destroyAllWindows()