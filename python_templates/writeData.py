import serial
from time import sleep


arduino = serial.Serial("/dev/ttyUSB0",9600)
sleep(2)

data = []


while(True):
    try:
        command = input("[a] encender \n[b] apagar\n:")
        arduino.write(bytes(command, 'utf-8'))
        sleep(.5)
    except Exception as e:
        arduino.close()


