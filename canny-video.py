# canny-video.py 
# Canny Processing of video
# 6.24.22 
# Reference: https://towardsdatascience.com/practical-image-process-with-opencv-8405772c603e
# About HoughP Lines: https://stackoverflow.com/questions/35609719/opencv-houghlinesp-parameters

import cv2
import numpy as np 

# vid = cv2.VideoCapture('./SanDiego805.mp4')
vid = cv2.VideoCapture('../_video/Nashville-01.mp4')

# while file is open, do the following loop
while vid.isOpened():
    ret, img = vid.read()
    img_copy = img.copy()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.blur(img_gray, (5,5))  # (x movement, y movement)
    # img_blur = cv2.bilateralFilter(img_gray, 15, 120, 120)  # slow
    # img_blur = cv2.GaussianBlur(img_gray, (3,5),10) # ksize must be odd, sigmax
    img_blur = cv2.medianBlur(img_gray, 7) # ksize must be odd, sigmax
    img_edge = cv2.Canny(img_blur,70,180)

    lines = cv2.HoughLinesP(img_edge,1,np.pi/180,1,1,1)
    # print(lines)
    # draw lines on original image
    for line in lines:
        # print('line data:', line)
        x1,y1,x2,y2 = line[0]
        cv2.line(img_copy,(x1,y1),(int(x2), int(y2)),(0,255,0),2)

    # create side by side image
    img_edge_bgr = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    row1 = np.concatenate((img,img_edge_bgr), axis=1)    

    img_blur_bgr = cv2.cvtColor(img_blur, cv2.COLOR_GRAY2BGR)
    row2 = np.concatenate((img_blur_bgr,img_copy), axis=1)    
    final_img = np.concatenate((row1, row2), axis=0)

    #display
    ret = cv2.imshow("Original", final_img)
    if cv2.waitKey(1) == ord('q'):
        break 

vid.release()
cv2.destroyAllWindows()
