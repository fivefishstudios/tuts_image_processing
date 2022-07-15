# detect_nonconvex_shapes.py
# detect shapes with cutouts in them (non-convex shape)
# 7/14/22

import cv2


# input is a color image
def get_contours(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold the image
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    # find the contours
    contours, hierarchy = cv2.findContours(thresh, 2, 1)    # what are these parameters?
    return contours


if __name__ == '__main__':
    img = cv2.imread('./images/jets-with-cutout.jpg')   # replace photo

    # iterate over etracted contours
    for contour in get_contours(img):
        orig_contour = contour
        # as you lower the multiplier, the contour outline follows original image more closely
        epsilon = 0.01 * cv2.arcLength(contour, True)
        contour = cv2.approxPolyDP(contour, epsilon, True)

        # extract convex hull from the contour
        hull = cv2.convexHull(contour, returnPoints=False)

        # extract convexity defects from the above hull
        defects = cv2.convexityDefects(contour, hull)

        if defects is None:
            continue

        # draw lines and circles to show the defects
        for i in range(defects.shape[0]):
            start_defect, end_defect, far_defect, _ = defects[i, 0]
            start = tuple(contour[start_defect][0])
            end = tuple(contour[end_defect][0])
            far = tuple(contour[far_defect][0])
            cv2.circle(img, far, 8, [0, 255, 0],-1)
            cv2.drawContours(img, [contour], -1, (0, 0, 255), 3)

    cv2.imshow('Convexity Defects', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


