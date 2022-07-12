"""
Comparing different kernels using cv2.filter2D()
"""
# filter2d_kernels.py 
# using different kernels for different image processing functions
# 6.24.22 

# Import required packages:
import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 6))
plt.suptitle("Comparing different kernels using cv2.filter2D()", fontsize=14, fontweight='bold')

# Load the original image:
image = cv2.imread('./images/scope.jpg')

# We try different kernels
# Identify kernel (does not modify the image)
kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]])

# Try different kernels for edge detection:
kernel_edge_detection_1 = np.array([[1, 0, -1],
                                    [0, 0, 0],
                                    [-1, 0, 1]])

kernel_edge_detection_2 = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

kernel_edge_detection_3 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])

# Try different kernels for sharpening:
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

kernel_unsharp_masking = -1 / 256 * np.array([[1, 4, 6, 4, 1],
                                              [4, 16, 24, 16, 4],
                                              [6, 24, -476, 24, 6],
                                              [4, 16, 24, 16, 4],
                                              [1, 4, 6, 4, 1]])

# Try different kernels for smoothing:
kernel_blur = 1 / 9 * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])

gaussian_blur = 1 / 16 * np.array([[1, 2, 1],
                                   [2, 4, 2],
                                   [1, 2, 1]])

# Try a kernel for embossing:
kernel_emboss = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]])

# Try different kernels for edge detection:
sobel_x_kernel = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

outline_kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])


# Apply all the kernels:
original_image = cv2.filter2D(image, -1, kernel_identity)
# edge_image_1 = cv2.filter2D(image, -1, kernel_edge_detection_1)
# edge_image_2 = cv2.filter2D(image, -1, kernel_edge_detection_2)
# edge_image_3 = cv2.filter2D(image, -1, kernel_edge_detection_3)
# sharpen_image = cv2.filter2D(image, -1, kernel_sharpen)
# unsharp_masking_image = cv2.filter2D(image, -1, kernel_unsharp_masking)
# blur_image = cv2.filter2D(image, -1, kernel_blur)
# gaussian_blur_image = cv2.filter2D(image, -1, gaussian_blur)
# emboss_image = cv2.filter2D(image, -1, kernel_emboss)
# sobel_x_image = cv2.filter2D(image, -1, sobel_x_kernel)
# sobel_y_image = cv2.filter2D(image, -1, sobel_y_kernel)
# outline_image = cv2.filter2D(image, -1, outline_kernel)

# see outputs
# ret = cv2.imshow('identity kernel', original_image)
# cv2.waitKey(0)
#
# ret = cv2.imshow('My kernel blur', mykernel_image)
# cv2.waitKey(0)


# experiment_kernel = 1/3 * np.array([[0,   0,  0],
#                               [1,   1,  1],
#                               [0,   0,  0]])

# generating the motion blur kernel
size=200
experiment_kernel = np.zeros((size, size))
experiment_kernel[int((size-1)/2), :] = np.ones(size)
experiment_kernel = experiment_kernel / size

# apply kernel
mykernel_image = cv2.filter2D(image, -1, experiment_kernel)

# display output
side_by_side = np.concatenate([original_image, mykernel_image],axis=1)
ret = cv2.imshow('Compare', side_by_side)
cv2.waitKey(0)

# ret = cv2.imshow('kernel blur', blur_image)
# cv2.waitKey(0)
#
# ret = cv2.imshow('gaussian blur', gaussian_blur_image)
# cv2.waitKey(0)

# ret = cv2.imshow('outline', outline_image)
# cv2.waitKey(0)
#
# ret = cv2.imshow('sobel y image', sobel_y_image)
# cv2.waitKey(0)
#
# ret = cv2.imshow('emboss image', emboss_image)
# cv2.waitKey(0)

# ret = cv2.imshow('edge 3 image', edge_image_3)
# cv2.waitKey(0)

# Show all the images:
# show_with_matplotlib(original_image, "identity kernel", 1)
# show_with_matplotlib(edge_image_1, "edge detection 1", 2)
# show_with_matplotlib(edge_image_2, "edge detection 2", 3)
# show_with_matplotlib(edge_image_3, "edge detection 3", 4)
# show_with_matplotlib(sharpen_image, "sharpen", 5)
# show_with_matplotlib(unsharp_masking_image, "unsharp masking", 6)
# show_with_matplotlib(blur_image, "blur image", 7)
# show_with_matplotlib(gaussian_blur_image, "gaussian blur image", 8)
# show_with_matplotlib(emboss_image, "emboss image", 9)
# show_with_matplotlib(sobel_x_image, "sobel x image", 10)
# show_with_matplotlib(sobel_y_image, "sobel y image", 11)
# show_with_matplotlib(outline_image, "outline image", 12)

# # Show the Figure:
# plt.show()
