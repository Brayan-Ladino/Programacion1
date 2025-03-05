import math

base = float(input("Ingrese la base del terreno: "))
altura = float(input("Ingrese la altura del terreno - Triangulo: "))
altura_rectangulo = float(input("Ingrese la altura del terreno - Rectangulo: "))

triangulo = (base*altura)/2

rectangulo = base*altura_rectangulo

area_total = triangulo + rectangulo
print (f"El area total del terreno es: {area_total} mts2")

#Terreno circular
radio = float(input("Ingrese el radio del terreno - Circular: "))

circulo = math.pi = (radio**2)

print (f"Area total del circulo: {circulo}")