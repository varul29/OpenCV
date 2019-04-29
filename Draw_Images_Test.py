import numpy as np
import cv2

img = cv2.imread('Watch.jpeg',cv2.IMREAD_COLOR)

#cv2.line(img, (Start(x,y)), till(x,y), (color code), pixels)
cv2.line(img, (0,0), (150,150), (255,255,255), 15)
#for Rectangle
#cv2.rectangle(img, Top Left coordinates(), Bottom Right Coordinates(), color, width)
cv2.rectangle(img, (15,25), (200,150),(0,255,0), 5)

#for Circle
#cv2.circle(img, Centre(x and y), radius, color, (Solid color or transparent) )
cv2.circle(img, (100,63), 55, (0,0,255), -1)

#polygon pts impotant
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape(-1,1,2)
cv2.polylines(img, [pts], True,(0,255,255),3)

#write somthing in Image
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img, 'openCV Tuts!', (Position to write), font, letter thickness,(Color), Letter Spacing, cv2.LINE_AA)
cv2.putText(img, 'openCV Tuts!', (0,130), font, 1,(200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
