import os
import PIL.Image
import cv2
import PIL
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
import keras



model = keras.models.load_model(r'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\nnmodel\savedmodel.keras')


while True:
    
    inp = input("NIG")
    img = PIL.Image.open(rf'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\nnmodel\tridata\img{inp}.png')
    img = np.array(img.convert("L"))//255
    img = np.invert(img)
    img = img//255

    img = img.reshape((1, 64, 64))
    print(img.shape)
    # print(model)

    prediction = model.predict(img)
    print("The number is probably a {}".format(np.argmax(prediction)))
    print(list(map(lambda x: np.round(x,2), prediction)))
    plt.imshow(img[0])
    plt.show()