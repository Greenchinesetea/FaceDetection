import numpy as haha
import cv2
ix = -1
iy = -1
drawing = False
def draw(event,x,y,flag,param):
    global gx, gy, dy, img
    if(event == cv2.EVENT_LBUTTONDOWN):
        dy == True
        gx = x
        gy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dy == True:
            cv2.rectangle(img, pt1=(gx,gy), pt2=(x, y),color = (43,205,238))
    elif event == cv2.EVENT_LBUTTONUP:
        dy = False
        cv2.rectangle(img, pt1=(gx,gy), pt2=(x, y),color = (43,205,238))

cv2.namedWindow('image') 
poo = cv2.imread("E:/f.jpg")
vid = cv2.VideoCapture(0)
brr,frame = vid.read()
fs = cv2.resize(frame,(450,450) )
ps = cv2.resize(poo,(450,450) )
img = cv2.add(ps, fs)
cv2.setMouseCallback('image',draw)

while True: 
    cv2.imshow('image', img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
vid.release()
cv2.destroyAllWindows()





