import cv2
import numpy as np

# Definir la fuente y el tamaño del texto
fuente = cv2.FONT_HERSHEY_SIMPLEX
escala = 1  # escala de la fuente
color = (255, 0, 0)  # color del texto en BGR (azul, verde, rojo)
grosor = 2  # grosor del texto

#Abren la camara
cap =  cv2.VideoCapture(0)
while True:
    
    _,frame = cap.read()

    #Tomamos canales rgb
    rgb_img = cv2.cvtColor(frame, code=cv2.COLOR_BGR2RGB)

    #Filtramos
    channel = np.copy(rgb_img[:,:,0])
    smooth_h = cv2.medianBlur(channel,21)
    #cv2.imshow("canal R con filtro blur", smooth_h)

    #Aplicamos segmentacion
    all_segmented = np.copy(smooth_h)
    all_segmented[all_segmented > 100] = 255
    all_segmented[all_segmented < 255] = 0
    #cv2.imshow("imagen segementada", all_segmented)

    #Filtro Canny
    edges = cv2.Canny(all_segmented,20,40)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Aproximar el contorno por un polígono
        # ARCLENGTH calcula la longitud de un una serie de puntos o contorno
        # El parametro True sirve para especificar si el contorno esta cerrado o no.
        perimetro = cv2.arcLength(contour, True)
        epsilon = 0.16* perimetro #afecta la sensibilidad de la aproximacion
        # El parametro True sirve para especificar si el contorno esta cerrado o no.
        approx = cv2.approxPolyDP(contour, epsilon, True)
        print(f"lados: {len(approx)} Perimetro: {perimetro}")

    #l_vertice = np.uint8(len(approx[0])/2)
    #x = approx[0][l_vertice]
    #y = x
    posicion = (250,250)

    # Dibujar el texto en la imagen
    cv2.putText(edges, "hola", posicion, fuente, escala, color, grosor)
    cv2.imshow("imagen canny", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(contours)
