import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

img = Image.open("VISION_ARTIFICIAL\PRACTICAS\p4\coins.jpg")
img_array = np.array(img)

rows, cols, _ = img_array.shape
noise = np.random.rand(rows,cols)
noise *= 1.2
gaussian = np.random.normal(0, 1, (rows, cols))
#print(np.max(gaussian))

noisy_image = np.zeros_like(img_array)

noisy_image[:,:,0] = img_array[:,:,0]+noise
noisy_image[:,:,1] = img_array[:,:,1]+noise
noisy_image[:,:,2] = img_array[:,:,2]+noise

#k = np.ones((3,3))/9
#x = cv2.filter2D(noisy_image,-1,k)
noisy_image = gray_img = cv2.cvtColor(noisy_image,code=cv2.COLOR_BGR2GRAY)
blur_filter = cv2.blur(noisy_image, (7, 7))  # Tamaño del kernel: 5x5

# Aplicar el filtro de mediana
median_filter = cv2.medianBlur(noisy_image, 7)  # Tamaño del kernel: 5x5


img_array = cv2.resize(img_array, (500,300))
noisy_image = cv2.resize(noisy_image, (500, 300))  # Redimensionar a 400x300
blur_filter = cv2.resize(blur_filter, (500, 300))
median_filter = cv2.resize(median_filter, (500, 300))


#median_filter = cv2.blur(median_filter,(7,7))

# Mostrar las imágenes originales y filtradas

# cv2.imshow('Imagen original', cv2.cvtColor(noisy_image,code=cv2.COLOR_BGR2RGB))
# cv2.imshow('Filtro de media', cv2.cvtColor(blur_filter,code=cv2.COLOR_BGR2RGB))
# cv2.imshow('Filtro de mediana', cv2.cvtColor(median_filter,code=cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray_img = cv2.cvtColor(img_array,code=cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(gray_img, (500, 300))


#los valores del filtro canny son umbrales, siendo el umbral inferior y umbral superior
#respectivamente, estos permiten modificar la sensibilidad del filtro
#los valores por debajo del umbral inferior no son considerados bordes fuertes
#Los valores por encima del umbral superior son considerados bordes
#Los valores entre ambos umbrales son considerados bordes debiles y estos solo seran bordes
#si estan conectados a bordes fuertes.
canny = cv2.Canny(median_filter,100,190)
cv2.imshow("Imagen original", img_array)
cv2.imshow("Imagen con ruido", noisy_image)
cv2.imshow('Imagen escala de grises', img_resized)
cv2.imshow('Filtro de mediana', cv2.cvtColor(median_filter, code=cv2.COLOR_BGR2RGB))
cv2.imshow('Bordes', cv2.cvtColor(canny,code=cv2.COLOR_BGR2RGB))
cv2.imshow('Filtro de media', cv2.cvtColor(blur_filter,code=cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()

