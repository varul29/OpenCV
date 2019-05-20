import cv2
import numpy as np


def main():
   counter = 0
   cap=cv2.VideoCapture(0)
   if cap.isOpened():
      
      ret,frame = cap.read()

   else:
      ret =False

   ret,frame1 = cap.read()
   ret,frame2 = cap.read()

   while ret:
      ret,frame = cap.read()
      #VideoFileOutput.write(frame)

      d=cv2.absdiff(frame1,frame2)

      grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)

     

      blur =cv2.GaussianBlur(grey,(5,5),0)
      ret,th=cv2.threshold(blur,20,240,cv2.THRESH_BINARY)
      dilated=cv2.dilate(th,np.ones((3,3),np.uint8),iterations=3)
      c,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

      for contour in c:
        area = cv2.contourArea(contour)
        #print(area)

        if area > 2000:
           cv2.drawContours(frame1, contour, -1, (0, 255, 0), 3)
           counter += 1

           '''
           # Proximity Detection using frame
           if counter == 5:
              _,frame3 = cap.read()
              cv2.imshow("frame3",frame3)
              '''
      '''
      # Define ROI according to pixel [y1:y2, x1:x2]
      roi = frame1[240: 480, 0: 640]
      frame1 = roi
      cv2.drawContours(frame1,c,-1,(0,255,0),2)
      '''

      #cv2.imshow("win1",frame2)
      cv2.imshow("inter",frame1)
      
      if cv2.waitKey(20) == 27:
         break
      frame1 = frame2
      ret,frame2= cap.read()
   cv2.destroyAllWindows()
   #VideoFileOutput.release()
   cap.release()
main()   
