import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #_is function which is return from the function and we dont care about it

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)

    #hsv hue sat value
    lower_or = np.array([0,25,0])
    upper_or = np.array([255,255,255])


    mask = cv2.inRange(hsv, lower_or, upper_or)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('res', res)

    # Erosion and Indialation
    kern = np.ones((5,5), np.uint8)
    # Erosion will takes place to just erode the other noise instead of specific colout
    erosion = cv2.erode(mask, kern, iterations = 1)
    dilation = cv2.dilate(mask, kern, iterations = 1)
    cv2.imshow('erode', erosion)
    cv2.imshow('dilate', dilation)

    #opening and closing -  To remove false positive and false negative
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kern)
    cv2.imshow('open', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destoryAllWindows()
cap.release()
