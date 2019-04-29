import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #_is function which is return from the function and we dont care about it

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)

    lower_or = np.array([0,30,0])
    upper_or = np.array([255,255,255])


    mask = cv2.inRange(hsv, lower_or, upper_or)
    #cv2.imshow('mask', mask)
    
    #Mask will be with in the mask frame will be with in the frame
    res = cv2.bitwise_and(frame, frame, mask = mask)  
    #cv2.imshow('result', res)

    #For Averaging to clear the noise between the image - averaging the pixels
    kern = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kern)

    cv2.imshow('smooth', smoothed)

    #Gausssian Blur Check
    blur = cv2.GaussianBlur(res,(15,15), 0)
    cv2.imshow('blur', blur)

    #Median Blur Checl
    median = cv2.medianBlur(res,15)
    cv2.imshow('median', median)

    #Bilateral Blur Check
    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral', bilateral)
    
    
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
