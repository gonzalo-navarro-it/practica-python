# Uso funcion primo
def esPrimo(n):
    esPrimo = 1
    i = 2
    while i < n:
        if n % i == 0:
            esPrimo = 0
        i=i+1
    return esPrimo

n = int(input("Ingrese un numero: "))
resultado = esPrimo(n)
if resultado == 1:
    print("Es primo")
else:
    print("No es primo")
