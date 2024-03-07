# Modificar "img" con las dimensiones necesarias para 
# la practica 
img = [
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1]
]


black = "\u001b[30m" #codigo ANSI para el color negro
white = "\u001b[37m" #codigo ANSI para el color blanco

# El codigo:u"\u25A0" es el codigo que dibuja un cuadrado en consola. 
square = u"\u25A0"  

# Itera sobre la img e imprime los cuadros
for row in img:
    for element in row:
        if element == 0:
            print(black+square, end=" ")  # Imprime cuadro negro si el elemento es 0
        else:
            print(white+square, end=" ")  # Imprime cuadro blanco si el elemento es 1
    print()  # Salta a la siguiente línea después de cada fila
