#lista = [1, 2, 3]
#estado = lista[2]

a = [2, "a", "David", 3.14, True, 100, "@"]
print(a[3])

#Individual elemento
decimal = a[3]
print(decimal)
#Tamaño de la lista
tamaño = len(a)
print(f"Tamaño de la lista: {tamaño}")
estado = a[4]
print(estado)
#Capturar la pocision comenzando por atras
dato=a[-4]
print(dato)
#Recorrer una lista
print(a[0:3])
print(a[2:6]) #Imprimir del 0 al 3
print(a[:])
print(a[2:])
print(a[:-5])
print(a[-5:-1])
#Lista vacia
numeros = []
#Añadir valores
numeros.append(10)
numeros.append(1)
numeros.append(5)
numeros.append(False)
print(numeros)
tamaño_n = len(numeros)
print(f"Tamaño de la lista: {tamaño_n}")
#Agregamos datos a una lista
numeros.insert(0, "Brayan")
print(numeros)
numeros.insert(2, "Unisanguil")
print(numeros)
tamaño_n = len(numeros)
print(f"Tamaño de la lista: {tamaño_n}")
numeros.append(2006)
numeros.append(2025)
numeros.insert(1, "Ladino")
print(numeros)
numeros.insert(-2, "Chiquinquira")
print(numeros)
#Eliminar lista
numeros.remove("Unisanguil")
print(numeros)
numeros.remove(1)
print(numeros)
tamaño_n = len(numeros)
print(f"Tamaño de la lista: {tamaño_n}")
#Para elimar el ultimo dato de la lista
numeros.pop()
print(numeros)
numeros[2:4] = [] #Elimina del 2 al 3
print(numeros)
#Separar datos de la lista con for
for dato in numeros:
    print(f"Datos: {dato}")
#----------------------------------------------------------------
materias = []

p = (int(input("Cuantas materias cursa: ")))

for i in range (p):
    materias.append(input("Ingre las asiganutas: "))
    materias.append(float(input("Ingre las notas: ")))
print(materias)

#Invertir lista
lista1 = [1, 2, 3, 4, 5]
lista1.reverse()
print(lista1)
#Ordenar una lista
lista1.sort()#de menor a mayor
print(lista1)

lista1.sort(reverse=True)#de mayor a menor
print(lista1)





