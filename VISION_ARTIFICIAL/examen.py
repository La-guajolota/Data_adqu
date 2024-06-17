import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)

while True:
    _, img = video.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gauss = cv.GaussianBlur(gray, (7, 7), 0)
    
    #Para circulos
    circles = cv.HoughCircles(gauss, cv.HOUGH_GRADIENT, 1, 100, param1=40, param2=30, minRadius=40, maxRadius=100)

    #Para rectangulos
    # Aplicar umbralización binaria inversa
    # Detección de bordes con Canny
    # Encontrar contornos
    _, bin_img = cv.threshold(gauss, 150, 255, cv.THRESH_BINARY_INV)
    edges = cv.Canny(bin_img, 10, 40)
    contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #Calculamos dinero
    total = 0
    flag0 = False
    flag1 = False

    if circles is not None:
        circles = np.uint16(np.around(circles))
        flag0 = True

        for x, y, r in circles[0, :]:
            
            cv.circle(img, (x, y), r, (0, 255, 0), 2)
            cv.circle(img, (x, y), 2, (0, 0, 255), 3)

            #Si no encuentra ninguna moneda real
            lbl = "nan"

            if 58 < r < 65:
                total += 10
                lbl = "$10"
            elif 52 < r <= 57:
                total += 5
                lbl = "$5"
            elif 47 < r <= 52:
                total += 2
                lbl = "$2"
            elif r < 48:
                total += 1
                lbl = "$1"

            cv.putText(img, lbl, (x - r // 2, y - r), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA)

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
            area = w * h * 0.5
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Calcular y mostrar el área del rectángulo en la terminal
            print(f'Área: {area}')
            
            # Medir los lados en cm y mostrar en la imagen
            lados_cm = []
            
            for i in range(len(approx)):
                p1 = approx[i][0]
                p2 = approx[(i + 1) % len(approx)][0]

                distancia = np.linalg.norm(p1 - p2)

                lados_cm.append(distancia)

                pos = (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))

            #Si no encuentra ninguna moneda real
            lbl_ = "nan"

            if 58 < area < 65:
                total += 1000
                lbl_ = "$1000"
            elif 52 < area <= 57:
                total += 500
                lbl_ = "$500"
            elif 47 < area <= 52:
                total += 200
                lbl_ = "$200"
            elif area < 48:
                total += 100
                lbl_ = "$100"

            # Mostrar el área en la imagen
            cv.putText(img, lbl_, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA)

    #Mostrar dinero si hay varo
    if (flag0 or flag1) : 
        cv.putText(img, "El total es ${}".format(total), (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA)
    

    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()