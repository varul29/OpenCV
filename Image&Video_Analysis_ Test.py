import numpy as np
import cv2

img = cv2.imread('Watch.jpeg', cv2.IMREAD_COLOR)
'''
pixel color values
px = img[100,200]
print(px)

# Assign your own Pixels
img[55] = [255,255,255]
px = img[55,55]
print(px)

#Reigone of image(Roi)

roi = img[100:150, 100:150]
print(roi)

# Assign your own Pixels to ROI

img[100:150, 100:150] = [255,255,255]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

#cut specific pixel and use apply it anywhere in the snap

img[100:150, 100:150] = [255,255,255]

watch_face = img[37:111, 107:194] #111-37 = 74 and 194-107 =87

img[0:74, 0:87] = watch_face # has to be the same size 

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
