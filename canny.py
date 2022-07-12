# canny.py 
# Canny Processing of images 
# 6.24.22 
# Reference: https://towardsdatascience.com/practical-image-process-with-opencv-8405772c603e
# About HoughP Lines: https://stackoverflow.com/questions/35609719/opencv-houghlinesp-parameters

from turtle import width
import cv2
import numpy as np 

def mask_of_image(image):
    height = image.shape[0] 
    width = image.shape[1]
    y=490 
    polygons = np.array([[(0,y),(0,height),(width, height),(width,y)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)     # process only white areas of masked image
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

img = cv2.imread('./road.png')

#display
ret = cv2.imshow("Original", img)
cv2.waitKey(0)



# process image
# (tresh, img_treshold) = cv2.threshold(img_gray,127,255, cv2.THRESH_BINARY) # treshold, max value if pixel exceeds treshold value
# print("Threshold return value: ", tresh )
# display processed image
# ret = cv2.imshow("Threshold", img_treshold)
# cv2.waitKey(0)

#convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurring
img_blur = cv2.blur(img_gray, (7,7))  # (x movement, y movement)
# display blurred image
ret = cv2.imshow("Blur", img_blur)
cv2.waitKey(0)




#edge detection
img_edge = cv2.Canny(img_blur,50,200)
# display edge detection image
ret = cv2.imshow("Canny", img_edge)
cv2.waitKey(0)

# create mask. display mask
img_mask = mask_of_image(img_edge)
ret = cv2.imshow("Mask", img_mask)
cv2.waitKey(0)

# use HoughLinesP on the masked image, i.e. removing top half of image
lines = cv2.HoughLinesP(img_mask,1,np.pi/180,1,1,1)
print(lines)
# draw lines on original image
for line in lines:
    # print('line data:', line)
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(int(x2), int(y2)),(0,255,0),2)

ret = cv2.imshow('Orig', img)
cv2.waitKey(0)