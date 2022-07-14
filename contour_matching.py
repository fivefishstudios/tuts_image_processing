# contour_matching.py
# find closest contour
# 7/14/22

import cv2


# extract reference contour from image
def get_ref_contour(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, cv2.THRESH_BINARY)  # type = 0?

    # Find all the contours in the thresholded image. The values # for the second and third parameters are restricted to a
    # certain number of possible values. You can learn more
    # 'findContours' function here: http://docs.opencv.org/modules/ imgproc/doc/structural_analysis_and_shape_descriptors.html
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    # Extract the relevant contour based on area ratio. We use the # area ratio because the main image boundary contour is
    # extracted as well and we don't want that. This area ratio
    # threshold will ensure that we only take the contour inside
    # the image.
    for contour_shape in contours:
        area = cv2.contourArea(contour_shape)
        img_area = img.shape[0] * img.shape[1]  # which is width and height?
        if 0.05 < area / float(img_area) < 0.8:  # ???? what is this?
            return contour_shape


# extract all contours from the image
def get_all_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    return contours


if __name__ == '__main__':
    # Boomerang reference image
    img1 = cv2.imread('./images/boomerang.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('Ref', img1)
    # cv2.waitKey()

    # input image (containing different shapes)
    img2 = cv2.imread('./images/contours-assorted.jpg', cv2.IMREAD_COLOR)

    # extract the reference contour
    ref_contour = get_ref_contour(img1)

    # extract all contours from input image
    input_contours = get_all_contours(img2)

    closest_contour = input_contours[0]
    min_dist = float("inf")

    # find the closes contour
    for contour in input_contours:
        # match the shapes and pick the closest one
        ret = cv2.matchShapes(ref_contour, contour, 1, 0.0)     # what are these parameters?
        if ret < min_dist:
            min_dist = ret
            closest_contour = contour

    cv2.drawContours(img2, [closest_contour], -1, (0,0,0), 3)   # what are these parameters?
    cv2.imshow('Output', img2)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

