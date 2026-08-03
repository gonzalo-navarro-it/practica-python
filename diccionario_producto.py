# Mini ficha de producto
productos = {}
productos["nombre"] = input("Ingrese nombre de producto: ")
productos["precio"] = float(input("Ingrese precio: "))
productos["stock"] = int(input("Cuanto stock hay: "))

print("Precio por cantidad:", productos["precio"]*productos["stock"])