import cv2
import numpy as np
from PIL import Image


img = Image.open("PRACTICAS/p4/coins2.jpg")
img_array = np.array(img)
img_array = cv2.resize(img_array,(500,300))

rgb_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2RGB)
lab_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2LAB)
hsv_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2HSV)


cv2.imshow("imagen original", rgb_img)
# cv2.imshow("canal R", rgb_img[:,:,0])
# cv2.imshow("canal G", rgb_img[:,:,1])
# cv2.imshow("canal B", rgb_img[:,:,2])

# cv2.imshow("canal L", lab_img[:,:,0])
# cv2.imshow("canal A", lab_img[:,:,1])
# cv2.imshow("canal B", lab_img[:,:,2])

cv2.imshow("canal H", hsv_img[:,:,0])
cv2.imshow("canal S", hsv_img[:,:,1])
cv2.imshow("canal V", hsv_img[:,:,2])

h_channel = np.copy(hsv_img[:,:,0])

smooth_h = cv2.medianBlur(h_channel,15)
all_segmented = np.copy(smooth_h)
all_segmented[all_segmented>0] = 255
cv2.imshow("imagen suavizada", smooth_h)
cv2.imshow("imagen segementada todas las monedas", all_segmented)

s_channel = np.copy(hsv_img[:,:,1])
print(np.max(s_channel))

color_segmented = np.copy(s_channel)
color_segmented[color_segmented<110] = 0
color_segmented[color_segmented>0] = 255

cv2.imshow("imagen segmentada modenas color cobre", color_segmented)


cv2.waitKey(0)
cv2.destroyAllWindows()

