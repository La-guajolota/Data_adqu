import serial
from time import sleep
import csv

archivo_csv = 'datos.csv'
arduino = serial.Serial("/dev/ttyUSB0",9600)
sleep(2)

while(True):
    try:
        command = input("command: ")
        command = command
        arduino.write(bytes(command, 'utf-8'))
        sleep(.5)
        raw_data = arduino.readline()
        stringData = raw_data.decode('utf-8').strip()
        #print(stringData)
        v1, v2, v3 = stringData.split(":")[:-1] 
        v1 = v1.split(",")[1]
        v2 = v2.split(",")[1]
        v3 = v3.split(",")[1]
        if (v1 =="0" and v2 =="0" and v3 =="0"):
            continue
        else:
            print("v1:", v1)
            print("v2:", v2)
            print("v3:", v3)
            with open(archivo_csv, "a+", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([v1, v2, v3])
            print("datos guardados")
        # data.append(float(stringData))
        # if(len(data) > 10):
        #     print(data)
        #     data = []
        #     sleep(1)

    except Exception as e:
        arduino.close()