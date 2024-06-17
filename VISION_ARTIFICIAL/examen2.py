import numpy as np
import cv2 as cv

# Definir la fuente y el tamaño del texto
fuente = cv.FONT_HERSHEY_SIMPLEX
escala = 0.5  # escala de la fuente
color_texto = (255, 0, 0)  # color del texto en BGR (azul, verde, rojo)
grosor = 1  # grosor del texto

# Color del contorno
color_contorno = (0, 0, 255)  # rojo en BGR

# Relación píxeles a centímetros (esto debe ser ajustado basado en la calibración de tu cámara)
pixel_cm_ratio = 0.013  # ejemplo: 1 pixel = 0.013 cm

# Abre la cámara
cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque gaussiano
    gauss = cv.GaussianBlur(gray, (5, 5), 0)
    
    # Aplicar umbralización binaria inversa
    _, bin_img = cv.threshold(gauss, 150, 255, cv.THRESH_BINARY_INV)
    
    # Detección de bordes con Canny
    edges = cv.Canny(bin_img, 10, 40)
    
    # Encontrar contornos
    contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Aproximar el contorno por un polígono
        perimetro = cv.arcLength(contour, True)
        epsilon = 0.02 * perimetro
        approx = cv.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Detectar rectángulos (4 vértices)
            x, y, w, h = cv.boundingRect(approx)
            area = w * h
            cv.rectangle(frame, (x, y), (x + w, y + h), color_contorno, 2)

            # Calcular y mostrar el área del rectángulo en la terminal
            print(f'Área: {area}')
            
            # Medir los lados en cm y mostrar en la imagen
            lados_cm = []
            for i in range(len(approx)):
                p1 = approx[i][0]
                p2 = approx[(i + 1) % len(approx)][0]
                distancia = np.linalg.norm(p1 - p2) * pixel_cm_ratio
                lados_cm.append(distancia)
                pos = (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))
                cv.putText(frame, f"{distancia:.2f} cm", pos, fuente, escala, color_texto, grosor)

            # Mostrar el área en la imagen
            cv.putText(frame, f"Área: {area}", (x, y - 10), fuente, escala, color_texto, grosor)

    # Mostrar la imagen con rectángulos y medidas
    cv.imshow("Medidas en cm", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()