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


mpath = "C:/Users/alima/OneDrive/Documents/GitHub/matwix2/aipart/datapart/datasets/setCOMBINED"


dimgs = []

dvals = {'(':0, ')':1, '+':2, '-':3, '0':4, '1':5,
         '2':6, '3':7, '4':8, '5':9, '6':10, '7':11,
         '8':12, '9':13, '=':14, '[divideforward]':15,
         '[multiply]':16}


print("starting imgload")

folds = os.listdir(mpath)
for fold in folds:
            
    imgs = os.listdir(f"{mpath}/{fold}")
    imgval = dvals[fold.split("_")[1]]

    print("on ", imgval)
    
    for imgname in imgs:
        
        img = np.array(PIL.Image.open(f"{mpath}/{fold}/{imgname}"))
        img = imgtools.convert_img_2bw(img)
        img = cv2.resize(img, (50,50), interpolation=cv2.INTER_NEAREST)
        
        dimgs.append((img, imgval))
           

print(len(dimgs))

X, y = zip(*dimgs)

print(len(X))
print(len(y))

X = np.array(X)
y = np.array(y)


# plt.imshow(x[10])
# plt.title(y[10])
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y , 
                                #    random_state=104,  
                                   test_size=0.15,  
                                   shuffle=True)




# Create a neural network model
# Add one flattened input layer for the pixels
# Add two dense hidden layers
# Add one dense output layer for the 10 digits
model =  keras.models.Sequential()
model.add( keras.layers.Flatten())
model.add( keras.layers.Dense(units=128, activation=  keras.activations.relu))
model.add( keras.layers.Dense(units=128, activation=  keras.activations.relu))
# model.add( keras.layers.Dense(units=64, activation=  keras.activations.relu))
# model.add( keras.layers.Dense(units=1000, activation=  keras.activations.relu))
# model.add( keras.layers.Dense(units=100, activation=  keras.activations.relu))

model.add( keras.layers.Dense(units=17, activation=  keras.activations.softmax))

# Compiling and optimizing model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=5)

# Evaluating the model
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_loss)
print(val_acc)

# Saving the model
model.save('C:/Users/alima/OneDrive/Documents/GitHub/matwix2/aipart/nnmodel/take2/savedmodel.keras')


# # model = keras.models.load_model(r'C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/handwritten_digits.keras')


# # img = cv2.imread(r'C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw/0-n/img_0-n_0.png')


# # # img = np.invert(np.array([img]))
# # print(img)
# # print(model)

# # prediction = model.predict(img)
# # print("The number is probably a {}".format(np.argmax(prediction)))
# # plt.imshow(img[0], cmap=plt.cm.binary)
# # plt.show()
