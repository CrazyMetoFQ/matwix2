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
    
    img = cv2.resize(img, (img.shape[0]*5,int(img.shape[1]*1))) # resize to get better eidth across

    kernel = np.ones((3,3),np.uint8)

    imgCanny = cv2.Canny(img,150,200)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=2)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


    ret, thresh = cv2.threshold(imgEroded, 0, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key = lambda c: cv2.boundingRect(c)[0]) # sort left 2 right

    bboxed_ext_imgs_list = []

    for c in contours:

        rect = cv2.boundingRect(c)
        x,y,w,h = rect    
        ci = img[y:y+h, x:x+w]
        bboxed_ext_imgs_list.append(ci)

    return bboxed_ext_imgs_list


cv2.imshow("og img", img)

boxedImgs = get_ext_bbox_imgs(img)

# for s,i in enumerate(boxedImgs):
    
    # cv2.imshow(f"img {s}", i)
    
for s,bimg in enumerate(boxedImgs):
    
    if bimg.shape[0] > 60:
        doubleboxedImgs = get_ext_bbox_imgs(bimg)
        
        for s2,i in enumerate(doubleboxedImgs):

            i = cv2.resize(i,(32,32))
            cv2.imshow(f"img {s} {s2}", i)
    else:
        cv2.imshow(f"img {s}",cv2.resize(bimg,(32,32)))



# bis = []
# for s,i in enumerate(lis):
    
#     # i = cv2.resize(i,(64,64))
    
#     ai = np.array(i)
    
#     ai = ai//255
#     # ai = np.round(ai,1)
#     ai = ai*255

#     bis.append(ai)
#     cv2.imshow(f"im ad {s}", ai)



cv2.waitKey(0)
cv2.destroyAllWindows()






# for img in bis:
    
#     img = PIL.Image.fromarray(img)
#     img = np.array(img.convert("L"))//255
#     img = np.invert(img)
#     img = img//255

#     print("bis")
#     img = img.reshape((1, 64, 64))
#     print(img.shape)
#     # print(model)


    
#     print("im")
#     plt.imshow(img[0])
#     plt.show()

# for s,bbox in enumerate(bboxesdup):
        
#         x,y,w,h = bbox
        
#         for s2,bbox2 in enumerate(bboxesdup):
            
#             x2,y2,w2,h2 = bbox2
            
#             if x2>x and y2>y :
                
#                 try:
#                     # bboxes.remove(bbox2)
#                     pass
#                 except:
#                     pass