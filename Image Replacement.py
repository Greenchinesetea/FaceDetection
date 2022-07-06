# ------ import libraries ------#
import cv2
import numpy as np

# -------- Read images ---------#
img = cv2.imread("c:/Pic1.png")
emoji = cv2.imread("c:/emoji1.jpg")

# ------ Change image size -----#
emoji = cv2.resize(emoji, (100, 100))

# ------- Replace image --------#
img[50:150, 30:130] = emoji #(Y1:Y2, X1:X2)

cv2.imshow("Image", img)

