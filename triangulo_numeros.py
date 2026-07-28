# Triangulo de numeros
fila = 0
col = 0

for fila in range(1, 6):
    for col in range(1, fila+1):
        print(col, end=" ")
    print("")