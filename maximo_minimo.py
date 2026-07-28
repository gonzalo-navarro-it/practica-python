# Maximo y minimo
n = int(input("Cuantos numeros vas a ingresar: "))
numero = int(input("Ingrese el primer numero: "))
maximo = numero
minimo = numero

for i in range(2, n+1):
    numero = int(input("Ingrese numero: "))
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print("Maximo: ", maximo)
print("Minimo: ", minimo)