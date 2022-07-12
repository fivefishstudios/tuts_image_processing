# color_maps.py
# all about color maps
# 6.26.22 

# Import required packages:
import cv2

img = cv2.imread('./parktree.jpg')

# convert bgr to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# color maps
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_AUTUMN)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_BONE)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_WINTER)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_RAINBOW)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_OCEAN)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_SUMMER)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_SPRING)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_COOL)
img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_HSV)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_HOT)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_PINK)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_PARULA)
# img_colormap = cv2.applyColorMap(img_gray, cv2.COLORMAP_PLASMA)


# display
ret = cv2.imshow('Orig', img)
cv2.waitKey()
ret = cv2.imshow('Gray', img_gray)
cv2.waitKey()
ret = cv2.imshow('Colormap', img_colormap)
cv2.waitKey()