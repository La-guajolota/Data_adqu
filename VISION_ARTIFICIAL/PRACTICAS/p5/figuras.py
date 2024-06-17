import cv2
import numpy as np

#Modificar indice de la funcion para 
#cambiar entre camaras
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

if not cap.isOpened():
    print("Error al abrir la camara")
else:
    while(True):

        ret, frame = cap.read()

        if not ret:

            print("error al capturar el fotograma")
            break
        else:

            #Aplicamos filtro
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_copy = np.copy(gray)
            smooth_img = cv2.medianBlur(gray, 21)
            _, bin_img = cv2.threshold(smooth_img,150,255,cv2.THRESH_BINARY_INV)
            #print(np.max(smooth_img))
            #print(np.min(smooth_img))
            cv2.imshow("Imagen suavizada", bin_img)

            #Encontramos bordes
            edges = cv2.Canny(bin_img,10,40)
            contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            mask = np.zeros((256,256))

            #Encontramos las figuras

            #Cuadrados
            for contour in contours:
            
                perimetro = cv2.arcLength(contour, True)
                epsilon = 0.16* perimetro 
                approx = cv2.approxPolyDP(contour, epsilon, True)

                #Identifica que si es un cuadrilatero
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)

                    #CHECAMOS CUAL ES
                    if abs(w-h)<5:
                        fig = "Cuadrado"
                    else:
                        fig = "rectangulo"

                    cv2.putText(gray_copy, f'Position:({x},{y}) {fig} de {w}X{h}', (x + 50, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.rectangle(gray_copy,(x,y), (x+w,y+h), (255,0,0), 2)

            #Circulos
            circles = cv2.HoughCircles(bin_img,cv2.HOUGH_GRADIENT,1,20, param1=50, param2=25,minRadius=10,maxRadius=300)

            #Mostramos cuantos duraznos hay
            try:
                for i in circles[0, : ] :
                    # Extraer coordenadas y radio del círculo
                    x, y, radius = int(i[0]), int(i[1]), int(i[2])
                    
                    # Dibujar el círculo detectado
                    #cv2.circle(gray_copy, (x, y), radius+10, (255, 0, 255), 1)
                    #Dibujamos un cuadrado
                        # Start coordinate, here (5, 5) 
                        # represents the top left corner of rectangle 
                        #start_point = (5, 5) 
                        # Ending coordinate, here (220, 220) 
                        # represents the bottom right corner of rectangle 
                        #end_point = (220, 220) 
                    cv2.rectangle(gray_copy,(x-radius-10,y+radius+10),(x+radius+10,y-radius-10),(255, 255, 255),2)

                    # Mostrar el radio del círculo en la imagen
                    cv2.putText(gray_copy, f'Ciruclo de R: {radius}', (x + 50, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

            except TypeError as error:
                pass

            cv2.imshow("Formas encontradas", gray_copy)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()