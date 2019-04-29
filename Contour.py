import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame,(5,5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_white = np.array([110,20,10])
    upper_white = np.array([150,255,255])

    mask = cv2.inRange(hsv,  lower_white, upper_white)

    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 26:
            cv2.drawContours(frame, contours, -1, (0,180,0),3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2destroyAllWindows()

    
