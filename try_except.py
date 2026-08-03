# Generar validacion en el programa
while True:
    try:
        print("Division de dos digitos")
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese segundo numero: "))
        print("El resultado es:",num1/num2)
        break
    except:
        print("Eso no es un numero valido")