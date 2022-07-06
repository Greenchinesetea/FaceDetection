import numpy as haha
import cv2

def click(event,x,y,flag,param):
        global xe, xb
        xe = 0
        xb = 0
        if(event == cv2.EVENT_LBUTTONDBLCLK):
                if(10 < x < 110 and 50 < y < 150):
                    xe = 1
                    print(xe)
                if (10 < x < 110 and 160 < y < 260):
                    xe = 2
                    print(xe)
                    
                if (10 < x < 110 and 270 < y < 370):
                    xe = 3
                    print(xe)
                    
                if (10 < x < 110 and 380 < y < 480):
                    xe = 4
                    print(xe)
                    
                if (520 < x < 620 and 50 < y < 150):
                    xb = 1
                    print("xb", xb)
                    
        return xe, xb


cv2.namedWindow("winname",cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("winname",click)

e1 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e1.png")
e2 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e2.png")
e3 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e3.png")
e4 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e4.png")
b = cv2.imread("C:/Users/acer/Documents/FaceDetection/b.png")


cascPath = "C:/Users/acer/Documents/FaceDetection/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)


vid = cv2.VideoCapture(1)
while vid.isOpened():
        brr,frame = vid.read()
        e1 = cv2.resize(e1, (100, 100,))
        e2 = cv2.resize(e2, (100, 100))
        e3 = cv2.resize(e3, (100, 100))
        e4 = cv2.resize(e4, (100, 100))
        b = cv2.resize(b, (100, 100))

        frame[50:150, 10:110] = e1
        frame[160:260, 10:110] = e2
        frame[270:370, 10:110] = e3
        frame[380:480, 10:110] = e4
        frame[50:150, 520:620] = b
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors =5, minSize=(30, 30))
       

        
        
        for (x, y, w, h) in faces:
                
                if(xe == 1):
                        e1 = cv2.resize(e1, (w, h))
                        frame[y:y+h, x:x+w] = e1 #(Y1:Y2, X1:X2)
                        print("e1")  
                elif(xe == 2):
                        e2 = cv2.resize(e2, (w, h))
                        frame[y:y+h, x:x+w] = e2 #(Y1:Y2, X1:X2)  
                elif(xe == 3):
                        e3 = cv2.resize(e3, (w, h))
                        frame[y:y+h, x:x+w] = e3 #(Y1:Y2, X1:X2)  
                elif(xe == 4):
                        e4 = cv2.resize(e4, (w, h))
                        frame[y:y+h, x:x+w] = e4 #(Y1:Y2, X1:X2)  
                elif(xb == 1):
                        pass
                else:
                    e1 = cv2.resize(e1, (w, h))
                    frame[y:y+h, x:x+w] = e1
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                xe = xe + 1
                xb = xb + 1

        cv2.imshow("winname", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
    
vid.release()
cv2.destroyAllWindows()



