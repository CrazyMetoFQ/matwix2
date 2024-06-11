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

# img = cv2.resize(img, (img.shape[0]*15, img.shape[0]*6))
img = cv2.resize(img, (200,100))


img_splited = []

c = 0
for col in img.transpose():
    
    if sum(col) > 0:
        
        img_splited.append(c)
        
    else: 

l=[]


    

    
        



cv2.waitKey(0)

cv2.destroyAllWindows()