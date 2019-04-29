import cv2
import matplotlib.pyplot as plt
import numpy as np

path = r"path\to\img"

img = cv2.imread(path)

#plt.imshow(img)
#plt.show()
pt1 = (86, 0) #ensure this point exists within the image
pt2 = (0, 101) #ensure this point exists within the image
cv2.line(img, pt1, pt2, (255, 255, 255))

#plt.imshow(img)
#plt.show()
#slope of line
m = float(pt2[1] - pt1[1])/float(pt2[0] - pt1[0])
c = pt1[1] - m*pt1[0]
#create mask image
mask1 = np.zeros(img.shape, np.uint8)
#for every point in the image
for x in np.arange(0, 87):
    for y in np.arange(0, 102):
        #test if point exists above the line, 
        if y > m*x + c:
            mask1[y][x] = (255, 255, 255)


#plt.imshow(mask1)
#plt.show()
fin_img = cv2.merge((img[:, :, 0], img[:, :, 1], img[:, :, 2], mask1[:,:, 0]))
#plt.imshow(fin_img)
#plt.show()

cv2.imwrite('output.png', fin_img)
