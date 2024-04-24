import serial
import csv
from time import sleep

# Constructor
MCU = serial.Serial('COM22', 9600)
sleep(1)

# Cuenta la cantidad de datos
count = 0

# Lista que guarda los datos
lista = []

# Nombre del archivo para las tablas
doc_name = "E:\\Sexto_sem\\Adq_datos\\ADC_medidads\\doco.csv"

while True:
    try:
        raw_data = MCU.readline()
        string_data = raw_data.decode("utf-8").strip()
        m = string_data.split()
        sleep(0.05)

        # error = real - medido
        error = int(m[0]) - int(m[1])

        # Añadir datos a la lista
        lista.append([int(m[0]), int(m[1]), error])

        print(lista[-1])

        count += 1
        if count == 30:
            MCU.close()
            with open(doc_name, mode='w', newline='') as file:    
                writer = csv.writer(file)  # Especificar la coma como delimitador
                writer.writerows(lista)
            break  # Salir del bucle después de escribir en el archivo
    except Exception as e:
        print("Error:", e)
        break  # Salir del bucle si hay un error
