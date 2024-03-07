import serial
from time import sleep


arduino = serial.Serial("/dev/ttyUSB0",9600)
sleep(2)

while(True):
    try:
        command = input("press [a] to get data...")
        command = command+"\n"
        arduino.write(bytes(command, 'utf-8'))
        sleep(.5)
        raw_data = arduino.readline()
        stringData = raw_data.decode('utf-8').strip()
        print(stringData)
        # data.append(float(stringData))
        # if(len(data) > 10):
        #     print(data)
        #     data = []
        #     sleep(1)

    except Exception as e:
        arduino.close()
