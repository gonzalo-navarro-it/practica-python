# Uso funcion en suma arreglo
def SumarArreglo(arr):
    suma = 0
    for j in range(0, 5):
        suma = suma+arr[j]
    return suma

numer = []
for i in range(0, 5):
    numer.append(int(input("Ingrese numero: ")))

total = SumarArreglo(numer)
print("El total es: ", total)
