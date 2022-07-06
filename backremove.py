import cv2
import numpy as np


# Parameters
blur = 21
canny_low = 15
canny_high = 150
min_area = 0.0005
max_area = 0.95
dilate_iter = 10
erode_iter = 10
mask_color = (0.0,0.0,0.0)
# load image
img = cv2.imread("C:/Users/acer/Documents/FaceDetection/e3.png")

 
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Apply Canny Edge Dection
edges = cv2.Canny(image_gray, canny_low, canny_high)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

contour_info = [(c, cv2.contourArea(c),) for c in cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[1]]

image_area = img.shape[0] * img.shape[1]  
      
        # calculate max and min areas in terms of pixels
max_area = max_area * image_area
min_area = min_area * image_area
mask = np.zeros(edges.shape, dtype = np.uint8)
for contour in contour_info:       
        if contour[1] > min_area and contour[1] < max_area:
            mask = cv2.fillConvexPoly(mask, contour[0], (255))

mask = cv2.dilate(mask, None, iterations=mask_dilate_iter)
mask = cv2.erode(mask, None, iterations=mask_erode_iter)
mask = cv2.GaussianBlur(mask, (blur, blur), 0)
mask_stack = mask_stack.astype('float32') / 255.0           
img = img.astype('float32') / 255.0

masked = (mask_stack * frame) + ((1-mask_stack) * mask_color)
masked = (masked * 255).astype('uint8')        
cv2.imshow("Foreground", masked)

cv2.waitkey(1)