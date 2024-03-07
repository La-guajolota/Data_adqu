import serial
from time import sleep

#Create Serial Object
mcu = serial.Serial('COM5', 9600)
sleep(2)

data = []

while(True):
    try:
        raw_data = mcu.readline()
        stringData = raw_data.decode('utf-8').strip()
        print(stringData)
        sleep(0.5)

        command = input("Send command\n:")
        mcu.write(bytes(command, 'utf-8'))
        sleep(.5)
    except Exception as e:
        mcu.close()