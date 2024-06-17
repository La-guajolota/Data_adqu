import cv2
import mediapipe as mp #Modelo de google, mapea el cuerpo

view = cv2.VideoCapture(0)
mpHands = mp.solutions.hands#modelo hands
hands = mpHands.Hands()#constructor
mpDraw = mp.solutions.drawing_utils#Utilidad para dibujar el articulado 

#Contadores de dedos
finger_1_up = False
finger_2_up = False
finger_3_up = False
finger_4_up = False

while True:
    _,cap = view.read()
    
    imgRGB = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)#procesa la imagen
    
    if results.multi_hand_landmarks:#coordenadas de las manos
        for handlms in results.multi_hand_landmarks:
            if (handlms.landmark[8].y<.6):#Los landmarks son los verices de los dedos 
                finger_1_up = True
            else:
                finger_1_up = False
            if(handlms.landmark[12].y<.6):
                finger_2_up = True
            else:
                finger_2_up = False
            if(handlms.landmark[16].y<.6):
                finger_3_up = True
            else:
                finger_3_up = False
            if(handlms.landmark[20].y<.6):
                finger_4_up = True
            else:
                finger_4_up = False
            fingerCount = [finger_1_up,finger_2_up,finger_3_up,finger_4_up]
            cv2.putText(cap,f'{fingerCount.count(True)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX
                        ,1,(0,255,0),4)    
            for id, lm in enumerate(handlms.landmark):
                h,w,c = cap.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(cap,(cx,cy),15,(139,0,0),cv2.FILLED)
            mpDraw.draw_landmarks(cap,handlms,mpHands.HAND_CONNECTIONS)
    cv2.imshow("hand skeleton",cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
