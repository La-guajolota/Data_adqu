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
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_copy = np.copy(gray)
            smooth_img = cv2.medianBlur(gray, 19)
            _, bin_img = cv2.threshold(smooth_img,120,255,cv2.THRESH_BINARY_INV)
            #print(np.max(smooth_img))
            #print(np.min(smooth_img))
            cv2.imshow("Imagen suavizada", bin_img)
            edges = cv2.Canny(bin_img,10,40)
            contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            mask = np.zeros((256,256))

            for contour in contours:
                perimetro = cv2.arcLength(contour, True)
                epsilon = 0.16* perimetro 
                approx = cv2.approxPolyDP(contour, epsilon, True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.putText(gray_copy, f'Position:({x},{y})', (x + 50, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.rectangle(gray_copy,(x,y), (x+w,y+h), (255,0,0), 2)
            cv2.imshow("Forma encontrada", gray_copy)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  
    cap.release()
    cv2.destroyAllWindows()