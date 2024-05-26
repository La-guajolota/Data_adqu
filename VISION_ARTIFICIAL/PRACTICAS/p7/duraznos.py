import cv2
import numpy as np
from PIL import Image

num = 0
#imagenes para usar
pic_1 = Image.open("PRACTICAS/p7/D0.jpg") #B
pic_2 = Image.open("PRACTICAS/p7/D1.jpg") #S
pic_3 = Image.open("PRACTICAS/p7/D2.jpg")
pic_4 = Image.open("PRACTICAS/p7/D3.jpg")
pic_5 = Image.open("PRACTICAS/p7/D4.jpg")
pic_6 = Image.open("PRACTICAS/p7/D5.jpg")

pics = [pic_1,pic_2,pic_3,pic_4,pic_5,pic_6]
pics_arrs = [np.array(pic) for pic in pics] #para arrays

print(pics_arrs[num].shape)
pics_arrs = [cv2.resize(pic,(500,300)) for pic in pics_arrs]

#Separamos por forma de color 
#rgb_img = cv2.cvtColor(pics_arrs[1], code=cv2.COLOR_BGR2RGB)
lab_img = cv2.cvtColor(pics_arrs[num], code=cv2.COLOR_BGR2LAB)
#hsv_img = cv2.cvtColor(pics_arrs[1], code=cv2.COLOR_BGR2HSV)
#RGB
#cv2.imshow("canal R", rgb_img[:,:,0])
#cv2.imshow("canal G", rgb_img[:,:,1])
#cv2.imshow("canal B", rgb_img[:,:,2])
#LAB
#v2.imshow("canal L", lab_img[:,:,0])
#v2.imshow("canal A", lab_img[:,:,1])
#cv2.imshow("canal B", lab_img[:,:,2])
#HSV
#cv2.imshow("canal H", hsv_img[:,:,0])
#cv2.imshow("canal S", hsv_img[:,:,1])
#cv2.imshow("canal V", hsv_img[:,:,2])

#Suavisamos
channel = np.copy(lab_img[:,:,2])
smooth_h = cv2.medianBlur(channel,51)
#cv2.imshow("canal B con filtro blur", smooth_h)

#Aplicamos segmentacion
all_segmented = np.copy(smooth_h)
all_segmented[ all_segmented > 110] = 0
all_segmented[ all_segmented > 0] = 255
cv2.imshow("imagen segementada", all_segmented)

# image: Es la imagen de entrada en escala de grises (debe ser una imagen de un solo canal) en la que se buscarán los círculos.
# method: Es el método de detección de círculos. En este caso, se utiliza cv2.HOUGH_GRADIENT, que representa el método de detección basado en gradiente.
# dp: Es la resolución inversa del acumulador de Hough. Controla la resolución del parámetro r (radio del círculo). Un valor más pequeño significa una mayor resolución en el círculo detectado. Por ejemplo, dp=1 implica la resolución original, dp=2 significa la mitad de la resolución.
# minDist: Es la distancia mínima entre los centros de los círculos detectados. Si la distancia entre los centros de dos círculos es menor que minDist, solo se mantiene el círculo más grande.
# param1: Es un parámetro específico del método de detección. En el caso de HOUGH_GRADIENT, param1 representa el umbral de detección de bordes (umbral de Canny). Un valor más pequeño significa una mayor sensibilidad en la detección de bordes.
# param2: Es otro parámetro específico del método de detección. Para HOUGH_GRADIENT, param2 representa el umbral mínimo para la detección de círculos. Un valor más pequeño significa más círculos detectados (aumenta la sensibilidad).
# minRadius: Es el radio mínimo de los círculos a ser detectados. Debe ser un entero positivo.
# maxRadius: Es el radio máximo de los círculos a ser detectados. Debe ser un entero positivo mayor que minRadius.
circles = cv2.HoughCircles(all_segmented,cv2.HOUGH_GRADIENT,1,20, param1=50, param2=25,minRadius=10,maxRadius=300)

#Copia de la imagen segmentada
xx = np.copy(pics_arrs[num])

#Mostramos cuantos duraznos hay
try:
    print(f"N durazns: {len(circles[0, : ])}")

    for i in circles[0, : ] :
        # Extraer coordenadas y radio del círculo
        x, y, radius = int(i[0]), int(i[1]), int(i[2])
        print(f"x: {x} y: {y} radio: {radius}")
        
        # Dibujar el círculo detectado
        cv2.circle(xx, (x, y), radius+10, (255, 0, 255), 1)
    
        # Mostrar el radio del círculo en la imagen
        cv2.putText(xx, f'Radio: {radius}', (x + 50, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow("FOTO",xx)
except TypeError as error:
    print("Ocurrió un error:", error)
    print("No hay duraznos")


cv2.waitKey(0)
cv2.destroyAllWindows()