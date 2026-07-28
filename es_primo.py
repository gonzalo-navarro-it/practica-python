# Es primo/no es primo
n = int(input("Ingrese numero: "))
i=2
esPrimo=1

while i < n:
    if n % i == 0:
        esPrimo=0
    i=i+1
if esPrimo==1:
    print("Es primo")
else:
    print("No es primo")