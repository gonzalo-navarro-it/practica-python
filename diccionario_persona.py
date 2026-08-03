# Cargar datos de 3 personas
personas = []

for datos in range(0, 3):
    cliente = {}
    cliente["nombre"] = input("Ingrese nombre: ")
    cliente["edad"] = int(input("Ingrese edad: "))
    personas.append(cliente)

for persona in personas:
    print("Nombre:", persona["nombre"], " edad:", persona["edad"])
