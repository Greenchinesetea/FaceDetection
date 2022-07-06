import cv2
import numpy as haha
cascPath = "C:/Users/acer/Documents/FaceDetection/haarcascade_frontalface_default.xml"
vid = cv2.VideoCapture("C:/Users/acer/Documents/FaceDetection/f.mp4")
s = 0
while vid.isOpened():
    brr,frame = vid.read()
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors =5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("Faces found", frame)
    print("Found {0} faces!".format(len(faces)))
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
vid.release()
cv2.destroyAllWindows()