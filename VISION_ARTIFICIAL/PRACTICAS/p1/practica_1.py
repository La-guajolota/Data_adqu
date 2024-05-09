#   3 imagenes distintas
#   Menu con opciones 
#                    -franjas horizontales
#                           *img1 
#                           *img2
#                           *img3
#                   -franjas verticales   
#                   -Collage 

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import random

from pyparsing import col

#imagenes para usar
pic_1 = Image.open("nadeko.jpeg")
pic_2 = Image.open("portada.jpg")
pic_3 = Image.open("ononoki.jpg")

pics = [pic_1,pic_2,pic_3]

#info de las imagenes
#print(pic_1)
#print(pic_2)
#print(pic_3)

#pa arreglos 
pics_arrs = [np.array(pic) for pic in pics]

#########
#tMAÑOS
##########

"""
(A,B,C)
A -> HORIZONTAL izq-der
B -> VERTICAL aba-arr
C -> Canales

(3757, 2844, 3)
(2024, 1434, 3)
(410, 728, 3)
"""
#print(pic_1_arr.shape)
#print(pic_2_arr.shape)
#print(pic_3_arr.shape)

###########################
#Funciones para cada opcion
###########################

#FRANJAS
def franjas_horizontales():
    for pic_arr in pics_arrs:

        pic_copy = pic_arr.copy()

        #tamaños
        height = pic_copy.shape[0]
        top = random.randint(0, height // 2)
        bottom = random.randint(height // 2, height)
        
        #Recortamos y pegamos
        pic_copy[top:bottom, :, 1] = pic_copy[top:bottom, :, 1] * 0.5  # Reducimos a la mitad la intensidad del canal verde

        plt.imshow(pic_copy)
        plt.show()
def franjas_vertical():
    for pic_arr in pics_arrs:
        
        pic_copy = pic_arr.copy()
        
        #Tmaños
        width = pic_copy.shape[1]
        left = random.randint(0, width // 2)
        right = random.randint(width // 2, width)
        
        #Recortamos y pegamos
        pic_copy[:, left:right, 1] = pic_copy[:, left:right, 1] * 0.5  # Reducimos a la mitad la intensidad del canal verde
        
        plt.imshow(pic_copy)
        plt.show()
#COLLAGE
def collage():
    
    images = [np.array(pic) for pic in pics]

    #Tmaños
    max_height = max(image.shape[0] for image in images)
    total_width = sum(image.shape[1] for image in images)

    collage_image = np.zeros((max_height, total_width, 3), dtype=np.uint8)

    current_col = 0

    # "Superponer" las imágenes en el collage
    for image in images:
        height, width, _ = image.shape
        collage_image[:height, current_col:current_col+width, :] = image
        current_col += width

    plt.imshow(collage_image)
    plt.show()

#MENU:
while(1):
    print("OPCIONES: ")
    print("opcion1")
    print("opcion2")
    print("opcion3\n")

    opc = int(input("Escriba el numero de la opcion: "))

    print("Escogio: \n", opc)

    if opc == 1:
        print("Franjas horizontales\n")
        franjas_horizontales()
    elif opc == 2:
        print("Franjas verticales\n")
        franjas_vertical()
    elif opc == 3:
        print("Collage\n")
        collage()
    else:
        print("Escoja una opcion valida:\n")  