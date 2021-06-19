import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#img = cv2.imread('test.jpg')
cap = cv2.VideoCapture(0)
i = 0

while 1:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #cv2.imshow('img',img)
        cv2.imwrite("output_pics/{i}.jpg".format(i=i), roi_color) 
        i += 1

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
