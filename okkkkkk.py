import numpy as np
import cv2
#pic1=cv2.imread("C:/C:\Users\Atf2th\Desktop/New folder (15)/avengers_battle_of_new_york.0.jpg")
#size=100
#pic1 = cv2.resize(pic1,(size,size))
cascPath = "C:/Users/Atf2th/Desktop/New folder (2)/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

vid = cv2.VideoCapture(0)
vid.set(3,640) 
vid.set(4,480)

while True:
    ret, img = vid.read()
    emoji = cv2.imread("c:/download.jpg")
    emoji2 = cv2.imread("c:/emoji3.jpg")
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))

    selected = 0
    
    for (x,y,w,h) in faces:

        if (selected % 2) == 0:
            emoji = cv2.resize(emoji, (w, h))
            img[y:y+h, x:x+w] = emoji #(Y1:Y2, X1:X2)    
        else:
            emoji2 = cv2.resize(emoji2, (w, h))
            img[y:y+h, x:x+w] = emoji2 #(Y1:Y2, X1:X2)
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imshow("test", img)

        selected = selected + 1

        k = cv2.waitKey(1) & 0xff
        if k == 27: 
            break

cap.release()
cv2.destroyAllWindows()
