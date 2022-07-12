# contrast.py
# adjust contrast for either grayscale or color image automatically
# 7/12/22

import cv2


class Contrast(object):
    def __init__(self, image):
        self._image = image

    def adjustContrast(self):
        # determine if grayscale or color
        isGray = len(self._image.shape) == 2

        if isGray:
            img = cv2.equalizeHist(self._image)
        else:
            img_yuv = cv2.cvtColor(self._image, cv2.COLOR_BGR2YUV)
            img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
            # merge back to BGR
            img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        return img
