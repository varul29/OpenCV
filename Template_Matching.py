import cv2
import numpy as np
img = cv2.imread("Watch.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Watch3.jpg", cv2.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]
#threshold = 0.8
#print(w)
#print(h)

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

# Test Max Min in template matching
x,y,z,c = cv2.minMaxLoc(result)
print('x:'+str(x))
print('y:'+str(y))
print('z:'+str(z))
print('c:'+str(c))
watch_free = template[0:202,0:122]
cv2.imshow('watch', watch_free)

#Set the Location and the threshold
loc = np.where(result >= 0.6)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 1)

cv2.imshow('Watch3', template)
print(result)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
