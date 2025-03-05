#Actividad 1: descuento de un producto

precio =float(input("Ingresa el precio de un producto"))
descuento =float(input("El porcentaje de descuento a aplicar"))
propina =float(input("Ingrese la propina"))

total1= ((precio * descuento)/100)
total2= precio - total1
print(total2)
print(propina)
print(total2 + propina)

#Actividad 2: Cambio de unidades

tiempo = int(input("Ingrese el numero de segundos"))

horas = tiempo / 3600
minutos = tiempo / 60

print(f"El cambio de {tiempo} segundos a horas es:  {horas}")
print(f"El cambio de {tiempo} segundos a minutos es: {minutos}")



