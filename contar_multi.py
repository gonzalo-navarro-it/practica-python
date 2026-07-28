# Contar multiplos
n = int(input("Ingrese un numero limite: "))
contador = 0

for i in range(1, n+1):
    if i % 3 == 0:
        contador = contador+1

print("Cantiedad de multiplos de 3: ", contador)