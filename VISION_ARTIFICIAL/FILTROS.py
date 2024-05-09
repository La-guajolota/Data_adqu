"""
spectel
blanco negro
gises
"""
import cv2
import numpy as np

#genra kernels randoms
k = [[[0.1,0,0.1],[0,0.1,0],[0.1,0,0.1]],#spectel
     [[2,2,2],[2,2,2],[2,2,2]],#blanco
     [[3,3,3],[4,4,4],[4,4,4]]]#grises

def apply_filter(frame,k):
    kernel = np.ones((5,5))/5
    #kernel = np.array(k)

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
cap =  cv2.VideoCapture(0)
while True:
    
    # bool confirma si existe camara
    # frame -> 
    _,frame = cap.read()
    smooth = apply_filter(frame, k[cont])
    cv2.imshow("imagen",smooth)
    
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