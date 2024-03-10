import serial
import time

#Create Serial Object
arduino = serial.Serial('COM17',9600)
time.sleep(0.25)

"""
try:
    command = input("INCIO DE PUENTE UART\n")
    arduino.write(bytes(command, 'utf-8'))
    time.sleep(.5)
except Exception as e:
    arduino.close()    
"""
    
while(True):
    try:
        #Read Arduino raw data bytes
        raw_data = arduino.readline()
        #transform data into string
        #use strip to remove spaces and newline jumps
        stringData = raw_data.decode('utf-8').strip()
        print(stringData)
        time.sleep(0.025)
    except Exception as e:
        arduino.close()
