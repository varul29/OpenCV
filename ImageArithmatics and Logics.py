import cv2
import numpy as np

#shapes of both the image has to same
img1 = cv2.imread('3DScatter.png')
img2 = cv2.imread('p2.png')

'''
#Formulae 1 - Not adding any pixels
add = img1 + img2
'''

'''
Formulae 2 -  Adding all the pixel values
# Values - (155,211,79) + (50,170,200) = 205, 381, 279... translated to (255,255,255)
add = cv2.add(img1,img2)
print(add)
cv2.imshow('add', weighted)
'''
'''
Formulae 3 - use for Weighted Image where you can adjust the percentage of image to be added with another image
weighted = cv2.addweighted(alpha values,0.6, beeta values, 0.4, gama values)
weighted = cv2.addWeighted(img1,0.6, img2, 0.4, 0)
print(weighted)
cv2.imshow('add', weighted)
'''

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.waitKey(0)
cv2.destroyAllWindows()
