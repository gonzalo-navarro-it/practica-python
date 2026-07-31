# Invertir arreglo
numer = []
invertidos = []

for i in range(0, 5):
    numer.append(int(input("Ingrese numero: ")))

for j in range (0, 5):
    invertidos.append(numer[4-j])

print("lista invertida: ")
for k in range (0, 5):
    print(invertidos[k])
