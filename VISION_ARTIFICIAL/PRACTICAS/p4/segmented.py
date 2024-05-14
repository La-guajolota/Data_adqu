import cv2
import numpy as np
from PIL import Image


img = Image.open("coins2.jpg")
img_array = np.array(img)

img_array = cv2.resize(img_array,(500,300))
gray_img = cv2.cvtColor(img_array,code=cv2.COLOR_BGR2GRAY)
median_filter = cv2.medianBlur(gray_img,7)

segmented_img = np.copy(median_filter)
print(np.max(segmented_img))

segmented_img[segmented_img<=30] = 255
segmented_img[segmented_img>=200] = 0

segmented_img[segmented_img>0] = 255

cv2.imshow('imagen original', cv2.cvtColor(img_array,code=cv2.COLOR_BGR2RGB))
cv2.imshow('imagen escala de grises', gray_img)
cv2.imshow('imagen suavizada', median_filter)
cv2.imshow('imagen segmentada', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()