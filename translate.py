# translate.py 
# translating images  
# 6.23.22 
# EXPLANATION
# https://stackoverflow.com/questions/10667834/trying-to-understand-the-affine-transform 
# Here is a mathematical explanation of affine transform: this is a matrix of size 3x3 that 
# applies the foolowing transformations on 2D vector: Scale in X axis, scaleY, rotation, skew, 
# translation in x axis and y. These are 6 transformations and thus you have six elements in 
# your 3x3 matrix. The bottom row is always [0 0 1]. Why? because the bottom row represents the 
# a perspective transformation in axis x and y, and affine transformation does not include
#  perspective transform. (If you want to apply perspective warping use homography: also 3x3 matrix )
# What is the relation between 6 values you insert into affine matrix and the 6 transformation 
# it does? Let us look at this 3x3 matrix like

# e*Zx*cos(a),     -q1*sin(a)  ,    dx,
# e*q2*sin(a),     Zy*cos(a),       dy,
# 0       ,        0  ,             1

#     The dx and dy elements are translation in x and y axis (just move the picture left-right, up down).
#     Zx is the relative scale(zoom) you apply to the image in X axis.
#     Zy is the same as above for y axis
#     a is the angle of rotation of the image. This is tricky since when you want to rotate 
#         by 'a' you have to insert sin(), cos() in 4 different places in the matrix.
#     'q' is the skew parameter. It is rarely used. It will cause your image to skew on the 
#         side (q1 causes y axis affects x axis and q2 causes x axis affect y axis)
#     Bonus: 'e' parameter is actually not a transformation. It can have values 1,-1. 
#          If it is 1 than nothing happens, but if it is -1 than the image is flipped 
#          horizontally. You can use it also to flip the image vertically but, 
#          this type of transformation is rarely used.

# Very important Note!!!!!
# The above explanation is mathematical. It assumes you multiply the matrix by column 
# vector from the right. As far as I remember, Matlab uses reverse multiplication (row 
# vector from the left) so you will need to transpose this matrix. I am pretty sure 
# that openCV uses regular multiplication but you need to check it. Just enter only 
# translation matrix (x shifted by 10 pixels, y by 1).

# 1,0,10
# 0,1,1
# 0,0,1

# If you see a normal shift than everything is OK, but If shit appears than transpose 
# the matrix to:

# 1,0,0
# 0,1,0
# 10,1,1 

import cv2 
import numpy as np 

img = cv2.imread('./pcb-1000x1000.JPG') # 1000 x 1000 

# using Matrix for translating images by using the function warpAffine() 
height, width = img.shape[:2] 
output_x_move = -330
output_y_move = -150
Matrix = np.float32([[1, 0, output_x_move ], 
                     [0, 1, output_y_move ]])
print(Matrix)

img_translated = cv2.warpAffine(img, Matrix, (width, height))

cv2.imshow('Translated', img_translated)
cv2.waitKey(0)