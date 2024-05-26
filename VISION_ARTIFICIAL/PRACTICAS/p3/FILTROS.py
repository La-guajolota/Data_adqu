"""
spectel
blanco negro
gises
"""
import cv2
import numpy as np

"""
Funcion de chatgtp
"""
salt_probability = 0.025
pepper_probability = 0.025
# Función para aplicar efecto de espejuelo con ruido de sal y pimienta
def apply_especkle_effect(frame, salt_prob, pepper_prob):
    noisy_image = np.copy(frame)
    
    # Aplicar ruido de sal y pimienta
    salt_mask = np.random.random(frame.shape) < salt_prob
    pepper_mask = np.random.random(frame.shape) < pepper_prob
    
    noisy_image[salt_mask] = 255
    noisy_image[pepper_mask] = 0
    
    return noisy_image

"""
Funcion para pasar a blanco y negro
"""
def black_white(frame):
    filtro_ints = np.copy(frame)


#genra kernels randoms
k = [[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],               # 1. Filtro de enfoque
     [[0,0,0],[0,1,0],[0,0,0]],                       # 2. Filtro de identidad
     [[0,-1,0],[-1,5,-1],[0,-1,0]],                   # 3. Filtro de realce de bordes
     [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],               # 4. Filtro de detección de bordes
     [[0.0625,0.124,0.0625],[0.125,0.25,0.125],[0.0625,0.124,0.0625]], # 5. Filtro de suavizado gaussiano
     [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]],     # 6. Filtro de suavizado promedio
     [[1,4,1],[0,5,0],[-3,-4,-3]],                    # 7. Filtro de detección de bordes tipo Sobel
     [[1/3,1/3,1/3],[0,0,0],[1/3,1/3,1/3]],           # 8. Filtro de desenfoque horizontal
     [[1/3,0,0],[0,0,0],[0,0,1/3]],                   # 9. Filtro de desenfoque vertical
     [[1/3,0,0],[0,0,0],[0,0,0]],                     # 10. Filtro de desenfoque diagonal
     [[1/10,1/10,1/10],[-1/10,-1/10,-1/10],[1/10,1/10,1/10]], # 11. Filtro de realce de bordes más suave
     [[-1,0,1],[-2,0,2],[-1,0,1]],                   # 12. Filtro de detección de bordes tipo Prewitt horizontal
     [[-1,-2,-1],[0,0,0],[1,2,1]],                    # 13. Filtro de detección de bordes tipo Prewitt vertical
     [[-1,-1,2],[-1,2,-1],[2,-1,-1]],                 # 14. Filtro de realce de bordes diagonales
     [[-1,0,0],[0,2,0],[0,0,-1]],                     # 15. Filtro de realce de bordes verticales
     [[0,0,-1],[0,2,0],[-1,0,0]],                     # 16. Filtro de realce de bordes horizontales
     [[-1,2,-1],[2,-4,2],[-1,2,-1]],                  # 17. Filtro de realce de bordes tipo Laplaciano
     [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]],               # 18. Filtro de realce de bordes más agudo
     [[-1,0,1],[-1,0,1],[-1,0,1]],                   # 19. Filtro de detección de bordes tipo Sobel horizontal
     [[-1,-1,-1],[0,0,0],[1,1,1]]]                   # 20. Filtro de detección de bordes tipo Sobel vertical


def apply_filter(frame,k):
    #kernel = np.ones((5,5))/5
    kernel = np.array(k)

    #result = cv2.filter(frame,-1,kernel)

    channels = cv2.split(frame)
    # el segundo argumento es la profundidad del pixel
    # profundidad de pixel es con cunatos bits construyes un color
    # Filter2d es la convolusion 
    conv_channel = [cv2.filter2D(ch,-1,kernel) for ch in channels]
    
    result= cv2.merge(conv_channel)
    return result

cont = 0
cont_max = len(k)
#Abren la camara
cap =  cv2.VideoCapture(1)
while True:
    
    # bool confirma si existe camara
    # frame -> 
    _,frame = cap.read()
    
    #smooth = apply_filter(frame, k[cont])
    especkle_image = apply_especkle_effect(frame, salt_probability, pepper_probability)

    cv2.imshow("imagen",especkle_image)
    
    if cv2.waitKey(1) & 0xFF == ord("a"):
        #movemos al siguiente kernel
        if cont == cont_max-1:
            pass
        else:
            cont = cont + 1
            print(cont)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        #movemos al kernel anterior
        if cont == -cont_max+1:
            pass
        else:
            cont = cont - 1
            print(cont)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        

cap.release()
cv2.destroyAllWindows()