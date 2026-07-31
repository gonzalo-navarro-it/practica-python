# Contar Ocurrencias
numer = []

for i in range(0, 6):
    numer.append(int(input("Ingrese numero: ")))

buscado = int(input("Que numero queres contar? "))
contador = 0

for i in range (0, 6):
    if numer[i] == buscado:
        contador = contador+1

print("Aparece", contador, "veces.")