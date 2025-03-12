brayan = "brada"
password = "1234"
print(type(password))

usuario = input("Ingrese su usario ")
contraseña = int(input("Inregrese la contraseña "))
print(type(contraseña))

if usuario==brayan and password == contraseña:
    print(f"Bienbenido Sistema {brayan}")
else:
    print("Usuario o contraseña incorrectos")



