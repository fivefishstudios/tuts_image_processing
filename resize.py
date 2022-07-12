# resize.py 
# resizing images  
# 6.23.22 

import cv2 
import numpy as np 
# import matplotlib.pyplot as plt

img = cv2.imread('./pcb-1000x1000.JPG') # 1000 x 1000 

# new_width = int(img.shape[1]/2)
# new_height = int(img.shape[0]/2)
new_width, new_height = img.shape[:2]
new_width = int(new_width/.5)
new_height = int(new_height/.5)
small_img = cv2.resize(img,(new_width, new_height),interpolation=cv2.INTER_LINEAR)
# small_img = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
cv2.imwrite('small2.jpg', small_img)
cv2.imshow('Resized', small_img)
cv2.waitKey(0)