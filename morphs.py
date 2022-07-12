import cv2


class MorphFilters(object):
    def __init__(self, image: object, kernel: object, iterations: object = 1) -> object:
        self._image = image
        self._kernel = kernel
        self._iterations = iterations
        self._outputimg = None

    def erode(self):
        self._outputimg = cv2.erode(self._image, self._kernel, iterations=self._iterations)
        return self._outputimg

    def dilate(self):
        self._outputimg = cv2.dilate(self._image, self._kernel, iterations=self._iterations)
        return self._outputimg

    def show(self, windowName):
        cv2.imshow(windowName, self._outputimg)
        cv2.waitKey(0)
