import string
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
numeros_enteros = []

# Nombre del archivo para las tablas
doc_name = "E:\\Sexto_sem\\Adq_datos\\ADC_medidads\\doco.csv"

while True:
    try:
        raw_data = MCU.readline()
        string_data = raw_data.decode("utf-8").strip()
        print(string_data)

    except Exception as e:
        print("Error:", e)
        break  # Salir del bucle si hay un error
