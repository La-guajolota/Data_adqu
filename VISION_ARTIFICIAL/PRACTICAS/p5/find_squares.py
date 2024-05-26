import cv2
import numpy as np
from matplotlib import pyplot as plt

def create_square(matrix_size, center, size):
    matrix = np.zeros(matrix_size)
    #rows, cols, channels = matrix_size
    x_center, y_center = center

    medium_size = size/2
    initial_cornerx = int(x_center - medium_size)
    initial_cornery = int(y_center - medium_size)
    end_cornerx = int(x_center + medium_size)
    end_cornery = int(y_center + medium_size)
    #matrix[10:10,10:10] = 255
    #Canales de la matriz para darle color al rectangulo
    matrix[initial_cornerx:end_cornerx,initial_cornery:end_cornery, 0] = 255
    matrix[initial_cornerx:end_cornerx,initial_cornery:end_cornery, 1] = 0
    matrix[initial_cornerx:end_cornerx,initial_cornery:end_cornery, 2] = 255
    return matrix

def create_cicle(matrix_size, center, radius):
    matrix = np.zeros(matrix_size)
    rows, cols = matrix_size
    x_center, y_center = center

    #calcular la distancia euclidiana de cada uno de los puntos al centro
    for row in range(rows):
        for col in range(cols):
            #calculo de la distancia eucludiana 
            # d = sqr((x1-x2^2)+(y1-y2^2))
            distance = np.sqrt((row-x_center)**2 + (col-y_center)**2)
            if distance  <= radius:
                matrix[row][col] = 255
    return matrix

circle_img = create_cicle((256,256),(40,40), 10)
square_img = create_square((256,256,3),(100,100),40)
#square_img2 = create_square((256,256,3),(160,160),40)
#square_img[:,:,0] = square_img[:,:,0] + circle_img + square_img2[:,:,0]
square_img[:,:,0] = square_img[:,:,0] + circle_img 
square_img = np.uint8(square_img)

edges = cv2.Canny(square_img,20,40)
#contours contine una serie de puntos representativos de cada contorno encontrado.
#cada contorno esta representado como una lista de lista.
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros((256,256))


for contour in contours:
    # Aproximar el contorno por un polígono
    # ARCLENGTH calcula la longitud de un una serie de puntos o contorno
    # El parametro True sirve para especificar si el contorno esta cerrado o no.
    perimetro = cv2.arcLength(contour, True)
    epsilon = 0.16* perimetro #afecta la sensibilidad de la aproximacion
    # El parametro True sirve para especificar si el contorno esta cerrado o no.
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Si el contorno aproximado tiene 4 vértices, es probablemente un rectángulo
    if len(approx) == 4:
        # Obtener las coordenadas del rectángulo delimitador
        x, y, w, h = cv2.boundingRect(approx)
        print(x)
        # Dibujar un rectángulo alrededor del contorno aproximado
        #cv2.rectangle(square_img, (x, y), (x + w-1, y + h-1), (0, 255, 0), 1)
        mask[x:x+h,y:y+w] = True


#estas lineas de codigo sirven para filtar lo que no sea un rectangulo de la escena 
inverted_mask = np.logical_not(mask)
filtered_img = np.copy(square_img)
# Usar la máscara invertida para asignar 0 a los valores que cumplen la condición
filtered_img[inverted_mask] = 0 



plt.subplot(1,3,1)
plt.imshow(square_img)
plt.title("imagen original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(edges)
plt.title("imagen bordes")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(filtered_img)
plt.title("imagen filtrada")
plt.axis("off")


plt.show()