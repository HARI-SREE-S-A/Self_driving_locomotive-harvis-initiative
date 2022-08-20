import cv2
import numpy as np

img = cv2.imread("test_image.jpg")
imgcpy = np.copy(img)
img_gray = cv2.cvtColor(imgcpy,cv2.COLOR_BGR2GRAY)
smoothen = cv2.GaussianBlur(img_gray,(5,5),0)




cv2.imshow("image",smoothen)

cv2.waitKey(0)