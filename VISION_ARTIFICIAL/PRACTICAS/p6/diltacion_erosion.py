"""
La dilatación y erosión son dos operaciones morfológicas 
fundamentales en el procesamiento de imágenes, que se utilizan
para transformar y analizar imágenes. Estas operaciones se basan en 
la idea de “elementos estructurantes” que se utilizan para “sondear” 
la imagen y extraer características.

Dilatación

La dilatación es una operación que añade píxeles a los límites de los 
objetos de una imagen. Se puede entender como un proceso de “expansión” 
de los objetos de la imagen. La dilatación se utiliza comúnmente para:

Aumentar la tamaño de los objetos de la imagen
Eliminar pequeños objetos de la imagen
Unir objetos separados
Erosión

La erosión es una operación que elimina píxeles de los límites de los 
objetos de una imagen. Se puede entender como un proceso de “contracción” 
de los objetos de la imagen. La erosión se utiliza comúnmente para:

Reducir el tamaño de los objetos de la imagen
Eliminar objetos pequeños de la imagen
Separar objetos unidos
Algoritmo

El algoritmo para la dilatación y erosión en imágenes es el siguiente:

Seleccionar un elemento estructurante (por ejemplo, un disco o un cuadrado)
Iterar sobre cada píxel de la imagen
Si el píxel se encuentra dentro del elemento estructurante, se considera como parte del objeto
Si el píxel se encuentra fuera del elemento estructurante, se elimina
Repetir los pasos 2-4 hasta que se complete la iteración sobre toda la imagen
Ejemplos

Dilatación: Se puede utilizar la dilatación para aumentar el tamaño de un
objeto en una imagen, por ejemplo, para hacer que un objeto sea más visible.
Erosión: Se puede utilizar la erosión para reducir el tamaño de un objeto en 
una imagen, por ejemplo, para eliminar objetos pequeños o separar objetos unidos.
En resumen, la dilatación y erosión son operaciones morfológicas fundamentales 
en el procesamiento de imágenes que se utilizan para transformar y analizar imágenes. 
Estas operaciones se basan en la idea de “elementos estructurantes” que 
se utilizan para “sondear” la imagen y extraer características.
"""
from pickle import TRUE
import numpy as np

#imagen
imagen_test1 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

#Elementos estrucutales
struct_1 = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

struct_2 = [
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

struct_3 = [
    [0,1,0],
    [1,1,1],
    [0,1,0]
]

# Crear una función que reciba como parámetros la estructura 
#y la imagen y regrese la erocion o dilatacion. 
def conv(img, struct, dil_ero):
    # Convertir la lista de listas a un array NumPy
    img = np.array(img)

    #dimensiones de la imagen
    num_filas, num_col = img.shape

    #nueva matriz de resultado 
    M_nueva = np.zeros((num_filas, num_col))

    N = np.sum(struct)
    for col in range(0, num_col - 2): #columnas
        for reng in range(0, num_filas - 2): #renglon
            
            M = img[reng:reng+3 , col:col+3] #submatriz
            #print(M)
            
            if dil_ero:
                #La estrucutura toca algun 1??
                if np.sum(np.multiply(M, struct)) >= 1 : 
                    M_nueva[reng+1][col+1] = 1
            else:
                #La estructura toca todos 1??
                if np.sum(np.multiply(M, struct)) == N : 
                    M_nueva[reng+1][col+1] = 1

    print(M_nueva)

#Corremos la aplicacion
# true ->> dilatacion
# flase ->> erocion
conv(imagen_test1,struct_1,TRUE)