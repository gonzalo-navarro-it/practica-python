# Tabla de multiplicar
n = int(input("Ingrese un numero: "))
resultado = 0

for i in range(1, 11):
    resultado = n*i
    print(n, "x", i,"=", resultado)

