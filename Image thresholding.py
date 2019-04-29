'''
BASIC THRESHOLDING
'''
import cv2
import numpy as np

img = cv2.imread('p2.png')
#retval, threshold = cv2.threshold(img, pixel parameter below (will be black), pixel parameter above (will be white), cv2.THRESH_BINARY)
retval, threshold = cv2.threshold(img, 140 , 255, cv2.THRESH_BINARY)

cv2.imshow('threshold', threshold)

#For gray Scale
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 120 , 255, cv2.THRESH_BINARY)
cv2.imshow('threshold2', threshold2)

#Gray Scale with Gaussian for Adaptive threshold to give a clear Image
gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115,1)
cv2.imshow('gauss', gauss)

#otsu Threshold
retval2, otsu = cv2.threshold(grayscaled, 150,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu', otsu)


cv2.imshow('original', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
