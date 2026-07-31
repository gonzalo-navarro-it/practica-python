# Uso de Funciones
def es_par(n):
    return n % 2 == 0

n = int(input("Ingrese un numero: "))
resultado = es_par(n)
if resultado:
    print("Es par")
else:
    print("Es impar")