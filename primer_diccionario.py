# Sintaxis de diccionario
personas = {}
personas["nombre"] = input("Ingresa nombre: ")
personas["edad"] = int(input("Ingrese edad: "))

print("Su nombre:", personas["nombre"], "Su edad:", personas["edad"] )

# Mostrar valores con un for
for clave in personas:
    print(clave,":", personas[clave])