import cv2
import numpy as np

# Función para obtener el código RGB del color seleccionado
def obtener_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Obtener el color en el punto seleccionado
        bgr_color = frame[y, x]
        # Convertir de BGR a RGB
        rgb_color = tuple(reversed(bgr_color))
        # Mostrar el color RGB
        print(f"Color RGB en ({x}, {y}): {rgb_color}")

# Iniciar la cámara
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

# Mostrar un mensaje con instrucciones
print("Haz clic en la ventana de la cámara para obtener el código RGB del color en ese punto.")

# Bucle principal
while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()
    
    # Mostrar el frame en una ventana
    cv2.imshow('Camara', frame)

    # Configurar el manejo de eventos del mouse
    cv2.setMouseCallback('Camara', obtener_color)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
