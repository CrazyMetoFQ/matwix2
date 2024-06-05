import cv2
import PIL
from PIL import Image
import os
import matplotlib.pyplot
import numpy as np
import random
import cv2
import os
import PIL.Image
import cv2
import PIL
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
import keras


def crop_bottom(image, crop_fraction=0.2):
    """Crop the bottom part of the image by the specified fraction."""
    height = image.shape[0]
    crop_height = int(height * crop_fraction)
    return image[:-crop_height, :]


def crop_image_percentages(image, percent_left, percent_right):

  (height, width, channels) = image.shape

  # Calculate the number of pixels to crop from each side
  crop_left_pixels = int(width * percent_left)
  crop_right_pixels = int(width * percent_right)

  # Define the new start and end points for cropping
  start_x = crop_left_pixels
  end_x = width - crop_right_pixels

  # Crop the image
  cropped_image = image[:, start_x:end_x, :]

  return cropped_image




img = cv2.imread(rf'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\nnmodel\triimgeq.png')


kernel = np.ones((3,3),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=4)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


ret, thresh = cv2.threshold(imgDialation, 0, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imgContours = img.copy()
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 1)
# cv2.imshow("Eroded Image",imgContours)

imgContours1 = img.copy()

lis = []

for s,c in enumerate(contours):
    rect = cv2.boundingRect(c)
    if cv2.contourArea(c) < 100: continue
    print (cv2.contourArea(c))
    x,y,w,h = rect
    cv2.rectangle(imgContours1,(x,y),(x+w,y+h),(0,255,0),1)
    
    ci = img[y:y+h, x:x+w]
    lis.append(ci)
    # cv2.imshow(f"img cont {s}",ci)
    


# cv2.imshow("Show",imgContours1)


bis = []
for s,i in enumerate(lis):
    
    i = cv2.resize(i,(64,64))
    
    ai = np.array(i)
    
    ai = ai//255
    # ai = np.round(ai,1)
    ai = ai*255

    bis.append(ai)
    # cv2.imshow(f"im ad {s}", ai)



# cv2.waitKey(0)
# cv2.destroyAllWindows()





print("load model")

model = keras.models.load_model(r'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\nnmodel\savedmodel.keras')

print("nig")

for img in bis:
    
    img = PIL.Image.fromarray(img)
    img = np.array(img.convert("L"))//255
    img = np.invert(img)
    img = img//255

    print("bis")
    img = img.reshape((1, 64, 64))
    print(img.shape)
    # print(model)

    prediction = model.predict(img)
    print("The number is probably a {}".format(np.argmax(prediction)))
    print(list(map(lambda x: np.round(x,2), prediction)))
    
    print("im")
    plt.imshow(img[0])
    plt.show()