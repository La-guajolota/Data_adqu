import matplotlib.pyplot as plt
import storage_regretion as stg_funcs
import serial
import re
from time import sleep

#Create Serial Object
mcu = serial.Serial('COM5',9600)
sleep(1)


mediciones = [] #lm35
valores_x = [] #termistor

while(True):
    try:
        #capturamos fato del mcu
        raw_data = mcu.readline()
        string_Data = raw_data.decode('utf-8').strip()
        print(string_Data)

        if  not("fin" in string_Data) :
            # Separamos los números en la cadena
            numeros_separados = string_Data.split()
            # Convertimos los números a enteros y los agregamos a las listas correspondientes
            mediciones.append(int(numeros_separados[0]))
            valores_x.append(int(numeros_separados[1]))
            
            # Imprimimos los números capturados
            """
            print("LM35:", mediciones[-1])
            print("THERMISTOR: ", valores_x[-1])
            """
        else:
            print("fin_de_muestreo")

            latch = 0

            #convertimos a enteros las muestras
            med_int = [int(num) for num in mediciones]
            x_int = [int(num) for num in valores_x]

            #de binario a decimal
            celcius = [num*(5/65535)/0.001  for num in med_int]# C/10mv 
            v_termistor = [num*(5/65535) for num in x_int]

            stg_funcs.stor_cvs("sesion_uno.csv",celcius,v_termistor)

            # Crear el gráfico
            plt.plot(v_termistor, celcius, marker='o', linestyle='-', color='b', label='Celcius')
            plt.xlabel('volts')
            plt.ylabel('celcius')
            plt.title('Gráfico de volt vs celcius')
            plt.legend()
            plt.show()

            mcu.close()

    except Exception as e:
        mcu.close()

