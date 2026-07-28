# Validacion de edad

while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 0 and edad <= 120:
        print("Edad valida: ", edad)
        break
    else: 
        print("Edad no valida")