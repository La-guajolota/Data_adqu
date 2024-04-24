import nidaqmx
from time import sleep
import threading
import numpy as np
from matplotlib import pyplot as plt

voltages = []
def genVoltage():
    with nidaqmx.Task() as genVoltage:
        genVoltage.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        for i in range(0,6):
            genVoltage.write(i)
            sleep(1)
        currentvoltage=4
        for j in range(0,5):
            sleep(1)
            genVoltage.write(currentvoltage)
            currentvoltage -= 1
        genVoltage.stop()

def readVoltage():
    with nidaqmx.Task() as readVoltage:
        readVoltage.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        for i in range(0,10):
            sleep(1)
            voltage_value = np.round(readVoltage.read())
            voltages.append(voltage_value)
            print(voltage_value)

        readVoltage.close()
        print("End of the program")

#mutitheads
t1 = threading.Thread(target = genVoltage)
t2 = threading.Thread(target = readVoltage)

t1.start()
t2.start()

t1.join()
t2.join()

#plot
plt.plot(voltages)
plt.plot("Voltage values")
plt.show()