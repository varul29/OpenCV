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

    '''
    we can covert single color into hsv color using
    
    dark_red = np.uint8([[[12,22,121]]])
    dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
    '''

    mask = cv2.inRange(hsv, lower_or, upper_or)
    cv2.imshow('mask', mask)
    
    #Mask will be with in the mask frame will be with in the frame
    res = cv2.bitwise_and(frame, frame, mask = mask)  
    cv2.imshow('result', res)
    
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
