import cv2
import PIL
from PIL import Image
import os
import matplotlib.pyplot
import numpy as np
import random
import cv2


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




img = cv2.imread(rf'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\data\htmlsynthdata_sym_raw\a-l\img_{random.randint(0,13)}.png')


kernel = np.ones((3,3),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
ret, thresh = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY)

# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# imgContours = img.copy()
# cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)


cv2.imshow("og img", img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

# cv2.imshow("Eroded Image",imgContours)



cv2.waitKey(0)
cv2.destroyAllWindows()

