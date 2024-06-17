import os
import PIL.Image
import cv2
import PIL
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
import keras
from sklearn.model_selection import train_test_split 

mpath = "C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw"
dimgs = {}

for sno,fold in enumerate(os.listdir(mpath)[:10]):
    
    dimgs[sno] = []
    for fl in os.listdir(mpath+"/"+fold)[:10]:
        
        img = np.array(PIL.Image.open(f"{mpath}/{fold}/{fl}").convert("L"))//255
        img = np.invert(img)
        img = img//255
        dimgs[sno].append(img)


# print(dimgs["5-n"][0].shape)
# print(dimgs["5-n"][0])

# for l in list(dimgs["5-n"][0]):
#     for p in l:
#         print(p,' ', end="")
#     print()
    
# plt.imshow(dimgs["5-n"][0])
# plt.show()

# reshape 
(y,X) = list(zip(*[h for g in [[(k,i) for i in v] for k,v in dimgs.items()] for h in g]))

y = np.array(y)

X = np.array(X)

# print(X[0], y[0])
# plt.imshow(X[20])
# plt.title(y[20])
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y , 
                                   random_state=104,  
                                   test_size=0.25,  
                                   shuffle=True)


# print(y_train[0])
# print(X_train[0].shape)
# plt.imshow(X_train[0])
# plt.show()


# print(np.array(X_train).shape)

# # Normalizing the data (making length = 1)
X_train =  keras.utils.normalize(X_train, axis=1)
X_test =  keras.utils.normalize(X_test, axis=1)

# print(X_train.shape)


# print(np.array(X_test).shape)

# Normalizing the data (making length = 1)
# X_train =  np.array(X_train).reshape((75,64*64))
# X_test =  np.array(X_test).reshape((25,64*64))

# print(X_train.shape)
# print(X_train[0])


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

model.add( keras.layers.Dense(units=10, activation=  keras.activations.softmax))

# Compiling and optimizing model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=5)

# Evaluating the model
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_loss)
print(val_acc)

# Saving the model
model.save(r'C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/nnmodel/savedmodel.keras')


# model = keras.models.load_model(r'C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/handwritten_digits.keras')


# img = cv2.imread(r'C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw/0-n/img_0-n_0.png')


# # img = np.invert(np.array([img]))
# print(img)
# print(model)

# prediction = model.predict(img)
# print("The number is probably a {}".format(np.argmax(prediction)))
# plt.imshow(img[0], cmap=plt.cm.binary)
# plt.show()
