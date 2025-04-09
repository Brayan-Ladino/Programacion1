for i in range(2): #Muestra un estado anterior
    print(i)

#Estructuta con range
for i in range(9, 10): #Muestra los numero indicados
    print(i)

#Estructura 
for i in range(3,10, 2): #Muestra los numero indicados
    print(i)


#Variable
x = "Python"

#Separar caracteres
for letra in x:
    if letra == "h":
        break
    else:
        print(letra)



for mul in range(1, 11):
    print(f"2 x {mul} = {2 * mul}")
numero = int(input("Ingrese un numero de tabla de multiplicacion: "))


for mul in range(1, 11):
    print(f"{numero} x {mul} = {numero * mul}")

for l in range(1, 11):
    if l % 2 == 0:
        print(f"Es par {l}")
    else:    
        print(f"Es impar {l}")




