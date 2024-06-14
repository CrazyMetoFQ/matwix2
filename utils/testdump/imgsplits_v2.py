import cv2
import PIL
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt




imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_1(23[multiply]6_goofrmv3.png'
imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_904+933-2_goofrmv0.png'
imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_68[divideforward]2[divideforward]5_goofrmv1.png'
imgpth = rf'C:\Users\alima\OneDrive\Documents\GitHub\mthwix2\aipart\datapart\preprocessing\eqs\img_4)581=64_goofrmv2.png'

img = cv2.imread(imgpth)


def get_ext_bbox_imgs(img):
    
    # img = cv2.resize(img, (img.shape[0]*5,int(img.shape[1]*1))) # resize to get better eidth across
    img = cv2.resize(img, (512, 512)) # resize to get better eidth across


    kernel = np.ones((3,3),np.uint8)

    imgCanny = cv2.Canny(img,150,200)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=2)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


    ret, thresh = cv2.threshold(imgEroded, 0, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    imgContours = cv2.drawContours(img.copy(), contours, -1, (0,255,0), 1)
    
    cv2.imshow("thresh", thresh)
    cv2.imshow("conoutrs og", imgContours)
    
        
    contours = sorted(contours, key = lambda c: cv2.boundingRect(c)[0]) # sort left 2 right  
    allBBoxes = [cv2.boundingRect(c) for c in contours]
    
    rectangledImg = img.copy()
    for bbox in allBBoxes:
        
        x,y,w,h = bbox
        cv2.rectangle(rectangledImg, (x,y), (x+w,y+h), (0,255,0))
        
    cv2.imshow("rectangled Img 1", rectangledImg)
    
    
    prev_box = allBBoxes[0]
    for bbox in allBBoxes:
        
        x,y,w,h = bbox
        x2,y2,w2,h2 = prev_box
            
        if (x2==x and w==w2 and y2!=y):
            
            print(prev_box)
            allBBoxes.remove(prev_box)
            pass
            
        prev_box = bbox
                



                             
    rectangledImg = img.copy()
    for bbox in allBBoxes:
        
        x,y,w,h = bbox
        cv2.rectangle(rectangledImg, (x,y), (x+w,y+h), (0,255,0))
        
    cv2.imshow("rectangled Img Final", rectangledImg)
            
        
        
    
 

get_ext_bbox_imgs(img)



cv2.waitKey(0)

cv2.destroyAllWindows()