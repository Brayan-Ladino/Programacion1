import math
while True:
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Rais cuadrada")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    numero1 =float(input("Ingrese el primer numero: "))
    numero2 =float(input("Ingrese el segundo numero: "))

    if opcion == 1:
        print(numero1+numero2)
    elif opcion == 2:
        print(numero1-numero2)
    elif opcion == 3:
        print(numero1*numero2)
    elif opcion == 4:
        print(numero1/numero2)
    elif opcion == 5:
        print(numero1 ** numero2)
    elif opcion == 6:
        raiz= math.sqrt(numero1)
        print(f"Raiz cuadrada = {raiz}")

    elif opcion == 7:
        break
    else:
        print("Opcion erronea")
print("Gracias por usar la Calculadora")
    
    





