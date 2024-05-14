import cv2
import numpy as np
from PIL import Image

#TOMAMOS LA IMAGEN
img = Image.open("VISION_ARTIFICIAL\PRACTICAS\p4\dog6.jpg")
img_array = np.array(img)
img_array = cv2.resize(img_array,(500,300))

#Separamos por forma de color 
rgb_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2RGB)
lab_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2LAB)
hsv_img = cv2.cvtColor(img_array, code=cv2.COLOR_BGR2HSV)

#Visualizamos por formas de color
cv2.imshow("imagen original", rgb_img)

#RGB
#cv2.imshow("canal R", rgb_img[:,:,0])
#cv2.imshow("canal G", rgb_img[:,:,1])
#cv2.imshow("canal B", rgb_img[:,:,2])

#LAB
#cv2.imshow("canal L", lab_img[:,:,0])
#cv2.imshow("canal A", lab_img[:,:,1])
#cv2.imshow("canal B", lab_img[:,:,2])

#HSV
#cv2.imshow("canal H", hsv_img[:,:,0])
cv2.imshow("canal S", hsv_img[:,:,1])
#cv2.imshow("canal V", hsv_img[:,:,2])

#Aplicamos filtro promediador
channel = np.copy(hsv_img[:,:,1])
smooth_h = cv2.medianBlur(channel,35)
cv2.imshow("canal A con filtro blur", smooth_h)

#Aplicamos segmentacion
all_segmented = np.copy(smooth_h)
all_segmented[all_segmented>100] = 255 #Negro el perro
all_segmented[all_segmented<255] = 0 
cv2.imshow("imagen segementada", all_segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()