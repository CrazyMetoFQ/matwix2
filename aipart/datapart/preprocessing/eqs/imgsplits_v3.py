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


def get_img_contours(img):
    kernel = np.ones((1,3),np.uint8)

    imgCanny = cv2.Canny(img,150,200)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

    ret, thresh = cv2.threshold(imgEroded, 0, 255, cv2.THRESH_BINARY)
    
    
    # thersh = cv2.imread()
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.imshow("c", imgCanny)
    cv2.imshow("d", imgDialation)
    cv2.imshow("e", imgEroded)
    cv2.imshow("t", thresh)
    
    
    return contours

def remove_internal_bbox(bboxes: list):
    
    for bbox in bboxes:
        
        x,y,w,h = bbox
        
        for bbox2 in bboxes:
            
            x2,y2,w2,h2 = bbox2
            
            if x2>x and (x2+w2)<(x+w):# and y2>y and y2+h2<y+h:
                
                bboxes.remove(bbox2)
        
    
    return bboxes


def show_bboxedImg(bboxes, img, wname = "bboxed img"):
    
    for bbox in bboxes:
        
        x,y,w,h = bbox
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0))
        
    cv2.imshow(wname, img)
    

def single_bbox_4x(bboxes):
    """
    keeps only one bbox pre x asix lenght
    """
    
    prev_box = bboxes[0]
    for bbox in bboxes:
        
        x,y,w,h = bbox
        x2,y2,w2,h2 = prev_box
            
        if (x2==x and w==w2 and y2!=y):
            
            bboxes.remove(prev_box)
            pass
            
        prev_box = bbox
        
    
    return bboxes


def get_subImages(img, bboxes):
    """
    only x element, no y distinktion
    """
    
    # return [img[y:y+h, x:x+w] for (x,y,w,h) in bboxes]
    return [img[0:, x:x+w] for (x,y,w,h) in bboxes]


def get_ext_bbox_imgs(img):
    
    img = cv2.resize(img, (512, 512)) # resize to get better eidth across
    
    contours = get_img_contours(img)
    
    imgContours = cv2.drawContours(img.copy(), contours, -1, (0,255,0), 1)
    
    cv2.imshow("conoutrs og", imgContours)
    
        
    contours = sorted(contours, key = lambda c: cv2.boundingRect(c)[0]) # sort left 2 right  
    allBBoxes = [cv2.boundingRect(c) for c in contours]
    

    show_bboxedImg(allBBoxes, img.copy(),"rectangled Img og")
    
    
    allBBoxes = remove_internal_bbox(allBBoxes)
    allBBoxes = remove_internal_bbox(allBBoxes)  # calling multiple times to remove remaining bboxes
    allBBoxes = remove_internal_bbox(allBBoxes)
    
    show_bboxedImg(allBBoxes, img.copy(),"rectangled Img int removed")
    
    
    allBBoxes = single_bbox_4x(allBBoxes)                               
    show_bboxedImg(allBBoxes, img.copy(),"rectangled Img under rmcved")

    subimgs = get_subImages(img, allBBoxes)
    
    # for s,img in enumerate(subimgs):   cv2.imshow(f"subimg {s}", img)
        
    return (allBBoxes, subimgs)
        
    


(BBoxes, subimgs)  = get_ext_bbox_imgs(img)

avg_width = np.mean([w for x,y,w,h in BBoxes])

# for sno, (bbox,img) in enumerate(zip(BBoxes, subimgs)):
    
#     x,y,w,h = bbox
    
#     if w > avg_width:
        
#         (sBBoxes, ssubimgs)  = get_ext_bbox_imgs(img)
        
#         for ssno, im in enumerate(ssubimgs):
            
#             cv2.imshow(f"sub subimg {ssno}", im)        
        



cv2.waitKey(0)

cv2.destroyAllWindows()