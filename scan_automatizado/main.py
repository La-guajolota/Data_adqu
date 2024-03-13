import serial
import funcs as scan
from time import sleep

print("---holaaaaa inicio del escanner---\n")

doc_name = "doco"
doc_name += ".cvs"

#Constructor
MCU = serial.Serial('COM17',9600)
sleep(1)

while(True):
    try:
            
        array_horizonral = [] # Almacena las celdas de cada fila
        array = [] # Contiene subarrays

        #Recolecta y almacena
        latch = 1
        print("scaneando...")
        count = 0             
        while(latch):
            raw_data = MCU.readline()
            string_data = raw_data.decode("utf-8").strip()
            print(string_data)
            sleep(0.5)

            if('v' in string_data):#salto de renglon
                array.append(array_horizonral[-count:]) #[inicio:final:paso]
                count = 0                

            if('h' in string_data):#horizonta inf0 data
                array_horizonral.append(int(string_data[0]))
                count = count + 1 

            if(string_data == "fin"): #Terminamos de recolectar y ahora almacenamos

                #ultimo renglon
                array.append(array_horizonral[-count:]) #[inicio:final:paso]
                count = 0  
                
                #Almacena en documento
                scan.storage(array,doc_name)
                
                latch = 0
            
        #Imprime matriz
        print("IMPRESION DE ESCANEO:")       
        print(array)
        scan.print_scan(array)
        array.clear()

    except Exception as e:
        MCU.close()