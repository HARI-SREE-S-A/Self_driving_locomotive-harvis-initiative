import cv2
import numpy as np


img = cv2.imread("test_image.jpg")

cv2.imshow("test",img)

cv2.waitKey(0)