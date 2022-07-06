import numpy as haha
import cv2

cascPath = "C:/Users/acer/Documents/FaceDetection/haarcascade_frontalface_default.xml"

e1 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e1.png")
e2 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e2.png")
e3 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e3.png")
e4 = cv2.imread("C:/Users/acer/Documents/FaceDetection/e4.png")
b = cv2.imread("C:/Users/acer/Documents/FaceDetection/b.png")


faceCascade = cv2.CascadeClassifier(cascPath)
vid = cv2.VideoCapture(0)  

xe = 0 

def click(event,x,y,flag,param):
    global xe 
    
    if(event == cv2.EVENT_LBUTTONDOWN):
            
                if((x >= 10 and x <= 110) and (y >= 50 and y <= 150)):
                        xe = 1
                        print(xe) #Debug log
                elif ((x >= 10 and x <= 110) and (y >= 160 and y <= 260)):
                        xe = 2
                        print(xe) #Debug log
                elif ((x >= 10 and x <= 110) and (y >= 270 and y <= 370)):
                        xe = 3
                        print(xe) #Debug log
                elif ((x >= 10 and x <= 110) and (y >= 380 and y <= 480)):
                        xe = 4
                        print(xe) #Debug log
                elif ((x >= 520 and x <= 620) and (y >= 50 and y <= 150)):
                        xe = 5
                        
                else:
                        xe = 0
                        
        





#vid = cv2.VideoCapture(1)
cv2.namedWindow("winname",cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("winname",click)




while vid.isOpened():

        mx = xe 

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
                
                if(mx == 1):
                        
                        frame[y:y+h, x:x+w] = cv2.resize(e1, (w, h))
                        print("e1")  #Debug log
                elif(mx == 2):
                        frame[y:y+h, x:x+w] =  cv2.resize(e2, (w, h))
                elif(mx == 3):
                        
                        frame[y:y+h, x:x+w] =  cv2.resize(e3, (w, h))
                elif(mx == 4):
                        
                        frame[y:y+h, x:x+w] =  cv2.resize(e4, (w, h)) 
                elif(mx == 5):
                        
                        frame[y:y+h, x:x+w] =  cv2.blur(frame[y:y+h, x:x+w], (28,28))
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        

        cv2.imshow("winname", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
    
vid.release()
cv2.destroyAllWindows()

