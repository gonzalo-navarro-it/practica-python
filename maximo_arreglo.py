# Maximo de Arreglo
nums = []
i = 0
maximo = 0

for i in range(0, 5):
    nums.append(int(input("Ingrese numeros: ")))

maximo = nums[0]

for j in range(0, 5):
    if nums[j] > maximo:
        maximo = nums[j]

print("El maximo es: ", maximo)