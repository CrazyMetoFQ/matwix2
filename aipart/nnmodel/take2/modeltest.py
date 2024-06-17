import os
import PIL.Image
import cv2
import PIL
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
import keras
from sklearn.model_selection import train_test_split 

import sys
sys.path.insert(1, "C:/Users/alima/OneDrive/Documents/GitHub/matwix2/")
import helperlibs.imgtoolscustum as imgtools


dvals = {'(':0, ')':1, '+':2, '-':3, '0':4, '1':5,
         '2':6, '3':7, '4':8, '5':9, '6':10, '7':11,
         '8':12, '9':13, '=':14, '[divideforward]':15,
         '[multiply]':16}

dvals = {v: k for k, v in dvals.items()}

print("load model")
model = keras.models.load_model("C:/Users/alima/OneDrive/Documents/GitHub/matwix2/aipart/nnmodel/take2/savedmodel.keras")

while True:
    
    print("load image")


    # img = PIL.Image.open(rf'C:\Users\alima\OneDrive\Documents\GitHub\matwix2\aipart\nnmodel\take2\triimgeq.png').convert("L")
    img = PIL.Image.open(rf'C:\Users\alima\OneDrive\Documents\GitHub\matwix2\aipart\nnmodel\take2\paint1.png').convert("L")
    img = imgtools.convert_img_2bw(img)
    subimgs = imgtools.split_img_woDuplicate(img)
    # imgtools.show_subimgs_onRow(subimgs)






    print("nig")

    for imgn in subimgs:
        
        imgn1 = cv2.resize(imgn, (50,50), interpolation=cv2.INTER_NEAREST)
        
        timg = np.expand_dims(imgn1, axis=0)
        
        prediction = model.predict(timg)
        print("The number is probably a {}".format(dvals[np.argmax(prediction)]))
        print(sorted([(dvals[s],np.round(i, 2)) for s,i in enumerate(prediction[0])], key = lambda i: i[1], reverse=True)[:5])
        
        print("im")
        
        plt.imshow(imgn)
        plt.show()
        
    input()