import random
import numpy as np

imagen_test1= [
    [1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5,5],
    [6,6,6,6,6,6,6,6,6,6],
    [7,7,7,7,7,7,7,7,7,7],
    [8,8,8,8,8,8,8,8,8,8],
    [9,9,9,9,9,9,9,9,9,9],
    [10,10,10,10,10,10,10,10,10,10]
]

imagen_test2 = [
    [1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5],
    [6,6,6,6,6,6,6,6]
]

imagen_test3 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5,5,5,5,5]
]

#Crear dos kernels de 3x3 (filtro promediador y filtro identidad(lleno de  unos))
Filtro_identidad = np.ones((3,3))
Filtro_promediador = np.ones((3,3))*(1/9)
#print(Filtro_identidad)
#print(Filtro_promediador)

# Crear una función que permita crear cuadrados/rectángulos en cualquier posición de la imagen y con cualquier tamaño.
def cuadrilatero(largo, ancho):
    matriz = [[None]*ancho for _ in range(largo)]

    for fila in range(0, largo):
        for col in range(0, ancho):
            
            #matriz[fila][col] = int(input(f"valor del elemento [{fila}][{col}] "))
            matriz[fila][col] = random.randint(0,9)

    print(matriz)
    return matriz

# Crear una función que reciba como parámetros el kernel y la imagen y regrese la convolución de ambas. 
def conv(img, kernel):
    # Convertir la lista de listas a un array NumPy
    img = np.array(img)

    num_filas, num_col = img.shape

    M_nueva = np.zeros((num_filas-2, num_col-2))

    for punto_ver in range(0, num_col - 2): #columnas
        for punto_der in range(0, num_filas - 2): #renglon
            M = img[punto_der:punto_der+3 , punto_ver:punto_ver+3] #submatriz
            rslt = np.sum(np.multiply(M, kernel))

            M_nueva[punto_der][punto_ver] = rslt

    print(M_nueva)

#Corremos la aplicacion

print("\n Cuadrilatero: \n")
imagen = cuadrilatero(5, 5)

print("\n kernel identidad:\n")
conv(imagen, Filtro_identidad)

print("\n kernel promediador:\n")
conv(imagen, Filtro_promediador)
