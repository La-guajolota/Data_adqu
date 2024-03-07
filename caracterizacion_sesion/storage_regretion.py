import csv

#ANALISIS DE INFO
def map(x, in_min, in_max, out_min, out_max):
    return float(x - in_min) * (out_max - out_min) / float(in_max - in_min) + out_min

def smoother(data,window_size):
    smoothed_data = []

    for i in range(len(data)):
        if i < window_size // 2:
            smoothed_data.append(sum(data[:i+window_size//2+1]) / (i + window_size//2 + 1))
        elif i >= len(data) - window_size // 2:
            smoothed_data.append(sum(data[i-window_size//2:]) / (len(data) - i + window_size//2))
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]) / window_size)
    
    return smoothed_data

def stor_cvs(nombre_archivo,celsius_values,voltage_values):
    # Escribir los datos en el archivo CSV
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir las etiquetas de las columnas
        escritor_csv.writerow(["Celsius", "Voltaje"])
        
        # Escribir los datos de las listas en el archivo CSV
        for celsius, voltaje in zip(celsius_values, voltage_values):
            escritor_csv.writerow([celsius, voltaje])