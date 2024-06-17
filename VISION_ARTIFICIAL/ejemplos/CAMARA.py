from unittest import result
import cv2
import numpy as np

def apply_filter(frame):
    #kernel = np.ones((5,5))/25
    k = [[1,1,1],[0,0,0],[-1,-1,-1]]
    kernel = np.array(k)

    #result = cv2.filter(frame,-1,kernel)

    channels = cv2.split(frame)
    # el segundo argumento es la profundidad del pixel
    # profundidad de pixel es con cunatos bits construyes un color
    # Filter2d es la convolusion 
    conv_channel = [cv2.filter2D(ch,-1,kernel) for ch in channels]
    
    result= cv2.merge(conv_channel)
    return result


#Abren la camara
cap =  cv2.VideoCapture(0)
while True:
    
    # bool confirma si existe camara
    # frame -> 
    _,frame = cap.read()
    smooth = apply_filter(frame)
    cv2.imshow("imagen",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()