import csv

# Matriz de ejemplo
img = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

# Ruta del archivo CSV de salida
csv_file = "output.csv"

# Escribir la matriz en el archivo CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(img)
