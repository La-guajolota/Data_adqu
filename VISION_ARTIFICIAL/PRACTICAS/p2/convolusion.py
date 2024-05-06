import numpy as np
from matplotlib import pyplot as plt

# matriz de 10x10 con valores aleatorios entre 0 y 1 en cada celda
#random_array = np.random.rand(10, 10) * np.random.rand()
random_array = np.array([np.tile(i + 1, 10) for i in range(10)])
print(random_array)
print(" ")

#print(random_array)

#matriz de nxn con 1/n en cada celda
n = 3 
#kernel = np.ones((n, n)) * (1/n)
kernel = np.ones((n, n))
print(kernel)
print(" ")

#print(kernel)

#ALgortmo de la convolusion
    
    #np.dot(matriz1, matriz2)

M_nueva = np.zeros((8,8))

for punto_ver in range(0,10-2): #columnas
    for punto_der in range(0,10-2): #renglon
        
                                #filas               #columnas                           
        M = random_array[punto_der:punto_der+n , punto_ver:punto_ver+n] #submatriz
        rslt = np.dot(M.flatten(), kernel.flatten())

        M_nueva[punto_der][punto_ver] = rslt

print(M_nueva)