import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurr = cv2.GaussianBlur(grey, (5, 5), 0)
    highlight = cv2.Canny(blurr, 50, 150)
    return highlight
def req_reg(image):
    height = image.shape[0]
    triangle = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,triangle,255)
    return mask

img = cv2.imread("test_image.jpg")
cann = canny(img)










cv2.imshow("test",req_reg(img))
cv2.waitKey(0)
