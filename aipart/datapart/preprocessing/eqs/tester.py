import cv2
import PIL
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt




# imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_1(23[multiply]6_goofrmv3.png'
# imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_904+933-2_goofrmv0.png'
# imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_68[divideforward]2[divideforward]5_goofrmv1.png'
imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_4)581=64_goofrmv2.png'

img = cv2.imread(imgpth)

img = cv2.resize(img, (img.shape[0]*15, img.shape[0]*6))

kernel = np.ones((1,3),np.uint8)

imgCanny = cv2.Canny(img,150,200)
imgEroded = cv2.erode(imgCanny,np.ones((1,1),np.uint8),iterations=1)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

ret, thresh = cv2.threshold(imgEroded, 0, 255, cv2.THRESH_BINARY)


# thersh = cv2.imread()

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
imgContour = img.copy()
cv2.drawContours(imgContour, contours, -1, (0,255,255), 1)


rectangleImg = img.copy()
for c in contours:
    
    rect = cv2.boundingRect(c)
    x,y,w,h = rect
    
    cv2.rectangle(rectangleImg, (x,y), (x+w,y+h), (0,255,0), 1)

cv2.imshow("c", imgCanny)
cv2.imshow("d", imgDialation)
cv2.imshow("e", imgEroded)
cv2.imshow("t", thresh)
cv2.imshow("Contour", imgContour)
cv2.imshow("rectanlge", rectangleImg)



    

    
        



cv2.waitKey(0)

cv2.destroyAllWindows()