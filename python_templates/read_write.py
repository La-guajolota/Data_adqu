import serial
from time import sleep

#Create Serial Object
mcu = serial.Serial('COM17',9600)
sleep(0.5)

data = []

while(True):
    try:
        raw_data = mcu.readline()
        stringData = raw_data.decode('utf-8').strip()
        print(stringData)
        sleep(0.5)

        command = input("Send features:\n:")
        mcu.write(bytes(command, 'utf-8'))
        sleep(1)
    except Exception as e:
        mcu.close()