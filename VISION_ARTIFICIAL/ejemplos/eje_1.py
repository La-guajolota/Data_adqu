import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

#carga la imagen
img = Image.open("ejemplos/nadeko.png")
print(img)

#imagen a arreglo
img_array = np.array(img)
print(img_array.shape)

#Separamos los colores
#:,:,0  el cero es el primer canal
red = img_array[:,:,0]
green = img_array[:,:,1]
blue = img_array[:,:,2]

#Dimenciones por color
# ctl+k+c ctl+k+u
# print("Forma de canal rojo: ",red.shape)
# print("Forma de canal blue: ",blue.shape)
# print("Forma de canal green: ",green.shape)

img_modificada = np.zeros_like(img_array)
img_modificada[:,:,0] = red
img_modificada[:,:,1] = green *0.5
img_modificada[:,:,2] = blue

#
img_array[:,100:150,:] = 0

img_modificada[:,0:100,:] = 0
img_modificada[:,150:,:] = 0

plt.imshow(img_array+img_modificada)
plt.show()

#plt.imshow(img_modificada)

# plt.subplot(1,4,1)
# plt.imshow(red, cmap="grey")
# plt.title("Imagen a rojo")
# plt.axis("off")

# plt.subplot(1,4,2)
# plt.imshow(green, cmap="grey")
# plt.title("Imagen a blue")
# plt.axis("off")

# plt.subplot(1,4,3)
# plt.imshow(blue, cmap="grey")
# plt.title("Imagen a green")
# plt.axis("off")

# plt.subplot(1,4,4)
# plt.imshow(img_array, cmap="grey")
# plt.title("Imagen")
# plt.axis("off")

#plt.show()