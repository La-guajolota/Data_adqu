import cv2
import numpy as np

# Función para redimensionar una imagen manteniendo la proporción
def resize_image(image, width=None, height=None):
    if width is None and height is None:
        return image
    h, w = image.shape[:2]
    if width is None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))
    return cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

# Función para aplicar suavizado a un canal de color
def apply_smoothing(channel):
    channel_copy = np.copy(channel)
    smoothed_channel = cv2.medianBlur(channel_copy, 1)
    return smoothed_channel

# Abrir la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un frame de la cámara
    _, frame = cap.read()

    # Convertir la imagen a diferentes espacios de color
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lab_img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Redimensionar las imágenes para que se ajusten a la pantalla
    resized_rgb = resize_image(rgb_img, width=300)
    resized_lab = resize_image(lab_img, width=300)
    resized_hsv = resize_image(hsv_img, width=300)

    # Aplicar suavizado a los canales RGB
    smooth_rgb_r = apply_smoothing(resized_rgb[:, :, 0])
    smooth_rgb_g = apply_smoothing(resized_rgb[:, :, 1])
    smooth_rgb_b = apply_smoothing(resized_rgb[:, :, 2])

    # Aplicar suavizado a los canales LAB
    smooth_lab_l = apply_smoothing(resized_lab[:, :, 0])
    smooth_lab_a = apply_smoothing(resized_lab[:, :, 1])
    smooth_lab_b = apply_smoothing(resized_lab[:, :, 2])

    # Aplicar suavizado a los canales HSV
    smooth_hsv_h = apply_smoothing(resized_hsv[:, :, 0])
    smooth_hsv_s = apply_smoothing(resized_hsv[:, :, 1])
    smooth_hsv_v = apply_smoothing(resized_hsv[:, :, 2])

    # Organizar las imágenes en un mosaico con nombres descriptivos
    stacked_image = np.vstack((
        np.hstack((smooth_rgb_r, smooth_rgb_g, smooth_rgb_b)),
        np.hstack((smooth_lab_l, smooth_lab_a, smooth_lab_b)),
        np.hstack((smooth_hsv_h, smooth_hsv_s, smooth_hsv_v))
    ))

    # Mostrar el mosaico con nombres descriptivos
    cv2.imshow("Mosaico de Canales de Color con Suavizado", stacked_image)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
