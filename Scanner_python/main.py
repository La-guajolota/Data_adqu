import serial
import metodos_scnanner as scan
from time import sleep

print("---holaaaaa inicio del escanner---\n")

#Constructor
MCU = serial.Serial('COM5',9600)
sleep(1)

while(True):
    try:
        #Calibra y da inicio a la rutina
        print("calibrando...")
            
        raw_data = MCU.readline()
        string_data = raw_data.decode("utf-8").strip()
        print(string_data)
        sleep(0.5)

        if(string_data == "all_ok"): #Terminamos de calibrar
            
            doc_name = input("Ingresa nomre de la seción: ")
            doc_name += ".cvs"    

            array_horizonral = [] # Almacena las celdas de cada fila
            array = [] # Contiene subarrays

            #Le avisamos al MCU que pase a scanear
            MCU.write(bytes("n", 'utf-8'))

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

                sleep(0.5) #Le avisamos al MCU que pase a scanear
                MCU.write(bytes("n", 'utf-8'))
                
                latch = 0
            
        #Imprime matriz
        print("IMPRESION DE ESCANEO:")       
        print(array)
        scan.print_scan(array)
        array.clear()

    except Exception as e:
        MCU.close()