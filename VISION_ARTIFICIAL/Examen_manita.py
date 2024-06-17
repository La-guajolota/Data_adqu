#PARA VISION ARTIFICIAL
import cv2
import mediapipe as mp #Modelo de google, mapea el cuerpo
#PARA MANIPULAR COSAS DEL WINDOWS
import subprocess
import os
import platform

view = cv2.VideoCapture(0)
mpHands = mp.solutions.hands#modelo hands
hands = mpHands.Hands()#constructor
mpDraw = mp.solutions.drawing_utils#Utilidad para dibujar el articulado 

#Contadores de dedos
finger_1_up = False
finger_2_up = False
finger_3_up = False
finger_4_up = False

"""
Nueva carpeta
"""
cont_carpetas = 0
name = "Carpeta_" + str(cont_carpetas)
def caprte_neuva() :
    
    global cont_carpetas
    name = f'Carpeta_{cont_carpetas + 1}'  # Nombre de la próxima carpeta a crear
    
    if platform.system() == 'Windows':
        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        ruta_carpeta = os.path.join(escritorio, name)

        # Comando CMD para crear la carpeta
        comando = f'mkdir "{ruta_carpeta}"'

        # Ejecutar el comando CMD
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proceso.communicate()

        if proceso.returncode == 0:
            # Carpeta creada exitosamente
            cont_carpetas += 1
            print(f'Se creó la carpeta "{name}" en el escritorio.')
        else:
            # Error al crear la carpeta
            print(f'Error al crear la carpeta "{name}": {stderr.decode("utf-8").strip()}')

    else:
        print('Este script está diseñado para ejecutarse en Windows.')

while True:
    _,cap = view.read()
    
    imgRGB = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)#procesa la imagen
    
    if results.multi_hand_landmarks:#coordenadas de las manos

        for handlms in results.multi_hand_landmarks:

            if (handlms.landmark[8].y<.6):#Los landmarks son los verices de los dedos 
                finger_1_up = True

                #nueva carpeta
                caprte_neuva()

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
