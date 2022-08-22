import cv2
import numpy as np

img = cv2.imread("test_image.jpg")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(grey,(5,5),0)
highlight = cv2.Canny(blurr,50,150)








cv2.imshow("output",highlight)
cv2.waitKey(0)