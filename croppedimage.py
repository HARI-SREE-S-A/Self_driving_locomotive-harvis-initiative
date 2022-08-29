import cv2
import numpy as np
import matplotlib.pyplot as plt

def conversn(image):
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurr = cv2.GaussianBlur(grey,(5,5),0)
    canny = cv2.Canny(blurr,50,150)
    return canny
def region(image):
    height = image.shape[0]
    triangle = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,triangle,255)
    masked = cv2.bitwise_and(image,mask)
    return masked

img = cv2.imread("test_image.jpg")
out1 = conversn(img)
out2 = region(out1)
cv2.imshow("out",out2)


cv2.waitKey(0)
