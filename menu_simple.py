# Menu simple
opcion1 = int(input("1) Sumar  2) Restar  3) Salir: "))

if opcion1 == 1:
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))
    print("Resultado: ", num1 + num2)
elif opcion1 == 2:
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))
    print("resultado: ", num1 - num2)
elif opcion1 == 3:
    print("Saliste del sistema")
else:
    print("Opcion no valida.")