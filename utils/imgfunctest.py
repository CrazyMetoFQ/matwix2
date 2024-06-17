import PIL.Image
import PIL._binary
import imgtoolscustum
import PIL
import os
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import cv2


mpath = "C:/Users/alima/Downloads/numstest/"
img_list_pth = os.listdir(mpath)

img = PIL.Image.open(mpath+img_list_pth[10]).convert("L")

img = imgtoolscustum.convert_img_2bw(img)

img = imgtoolscustum.blob2img(imgtoolscustum.find_all_islands(img)[0], 0)

print(img.shape)
plt.imshow(img)
plt.show()


ii = np.where(img.flatten() == 1)[0]


# plt.scatter(x=range(len(ii)), y=ii, color=[(0/255,255/255,255/255)])
plt.scatter(x=range(len(ii)), y=ii)
plt.show()

# img = np.array(PIL.Image.fromarray(img).resize((28,28), resample=PIL.Image.NEAREST))

# print(img.shape)
# plt.imshow(img)
# plt.show()