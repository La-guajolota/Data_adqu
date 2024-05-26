import cv2
import numpy as np
from matplotlib import pyplot as plt

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

def create_square(matrix_size, center, size):
    matrix = np.zeros(matrix_size)
    rows, cols, channels = matrix_size
    x_center, y_center = center

    medium_size = size/2
    initial_cornerx = int(x_center - medium_size)
    initial_cornery = int(y_center - medium_size)
    end_cornerx = int(x_center + medium_size)
    end_cornery = int(y_center + medium_size)
    #matrix[10:10,10:10] = 255
    matrix[initial_cornerx:end_cornerx,initial_cornery:end_cornery, :] = 255
    return matrix


circle_img1 = create_cicle((256,256),(127,127), 40)
circle_img2 = create_cicle((256,256),(40,40), 10)

circle_img = circle_img1+circle_img2
circle_img = np.uint8(circle_img)
print(circle_img)


# image: Es la imagen de entrada en escala de grises (debe ser una imagen de un solo canal) en la que se buscarán los círculos.
# method: Es el método de detección de círculos. En este caso, se utiliza cv2.HOUGH_GRADIENT, que representa el método de detección basado en gradiente.
# dp: Es la resolución inversa del acumulador de Hough. Controla la resolución del parámetro r (radio del círculo). Un valor más pequeño significa una mayor resolución en el círculo detectado. Por ejemplo, dp=1 implica la resolución original, dp=2 significa la mitad de la resolución.
# minDist: Es la distancia mínima entre los centros de los círculos detectados. Si la distancia entre los centros de dos círculos es menor que minDist, solo se mantiene el círculo más grande.
# param1: Es un parámetro específico del método de detección. En el caso de HOUGH_GRADIENT, param1 representa el umbral de detección de bordes (umbral de Canny). Un valor más pequeño significa una mayor sensibilidad en la detección de bordes.
# param2: Es otro parámetro específico del método de detección. Para HOUGH_GRADIENT, param2 representa el umbral mínimo para la detección de círculos. Un valor más pequeño significa más círculos detectados (aumenta la sensibilidad).
# minRadius: Es el radio mínimo de los círculos a ser detectados. Debe ser un entero positivo.
# maxRadius: Es el radio máximo de los círculos a ser detectados. Debe ser un entero positivo mayor que minRadius.

circles = cv2.HoughCircles(circle_img,cv2.HOUGH_GRADIENT,1,20, param1=50, param2=10,minRadius=4,maxRadius=40)
xx = np.copy(circle_img)
print(circles)

for i in circles[0, :]:
    # Extraer coordenadas y radio del círculo
    x, y, radius = int(i[0]), int(i[1]), int(i[2])
    print(x)
    print(y)
    # Dibujar el círculo detectado
    cv2.circle(xx, (x, y), radius+10, (255, 0, 255), 1)
   
    # Mostrar el radio del círculo en la imagen
    #cv2.putText(circle_img, f'Radio: {radius}', (x - 40, y - 20),
    cv2.putText(xx, f'Radio: {radius}', (x + 50, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

plt.subplot(1,2,1)
plt.axis("off")
plt.title("original image")
plt.imshow(circle_img)

plt.subplot(1,2,2)
plt.axis("off")
plt.title("circles founded")
plt.imshow(xx)

plt.show()