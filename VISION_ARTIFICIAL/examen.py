import numpy as np
import cv2 as cv

video = cv.VideoCapture(1)

while True:
    _, img = video.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gauss = cv.GaussianBlur(gray, (41, 41), 0)
    
    # Para círculos
    circles = cv.HoughCircles(gauss, cv.HOUGH_GRADIENT, 1, 100, param1=40, param2=30, minRadius=20, maxRadius=60)

    # Para rectángulos
    _, bin_img = cv.threshold(gauss, 150, 255, cv.THRESH_BINARY_INV)
    edges = cv.Canny(bin_img, 10, 40)
    contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Calcular dinero
    total = 0
    flag0 = False
    flag1 = False

    if circles is not None:
        circles = np.uint16(np.around(circles))
        flag0 = True

        for x, y, r in circles[0, :]:
            cv.circle(img, (x, y), r, (255, 0, 0), 2)  # Cambiar a color azul
            cv.circle(img, (x, y), 2, (0, 255, 255), 3)  # Cambiar a color amarillo

            # Etiquetas de monedas
            lbl = "nan"

            if 44 < r < 50:
                total += 10
                lbl = "$10"
            elif 40 < r <= 44:
                total += 5
                lbl = "$5"
            elif 37 < r <= 40:
                total += 2
                lbl = "$2"
            elif r <= 36:
                total += 1
                lbl = "$1"

            cv.putText(img, lbl, (x - r // 2, y - r), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)  # Cambiar fuente y color

            # Mostrar el radio de la moneda en la terminal
            print(f'Radio: {r}')
    
    for contour in contours:
        # Aproximar el contorno por un polígono
        perimetro = cv.arcLength(contour, True)
        epsilon = 0.02 * perimetro
        approx = cv.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Detectar rectángulos (4 vértices)
            flag1 = True

            x, y, w, h = cv.boundingRect(approx)
            area = int(w * h * 0.0025)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Cambiar a color cyan

            # Calcular y mostrar el área del rectángulo en la terminal
            print(f'Área: {area}')
            
            # Mostrar el área en la imagen
            #cv.putText(img, str(area), (x, y - 10), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 2, cv.LINE_AA)  # Cambiar fuente y color

            # Etiquetas de dinero
            lbl_ = "nan"

            if 120 < area < 150:
                total += 500
                lbl_ = "$1000"
            elif 95 < area <= 115:
                total += 250
                lbl_ = "$500"
            elif 80 < area <= 90:
                total += 100
                lbl_ = "$200"
            elif area < 71:
                total += 50
                lbl_ = "$100"

            cv.putText(img, lbl_, (x + w // 2, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,(255, 0, 255)Q, 2, cv.LINE_AA)  # Cambiar fuente y color

    # Mostrar el total de dinero si hay monedas o rectángulos detectados
    if flag0 or flag1:
        cv.putText(img, "Total: ${}".format(total), (20, 50), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)  # Cambiar fuente y color

    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
