# {} objeto ---> Atributos y datos
diccionario ={
    "nombre": "Brayan David Ladino Rodriguez",
    "celular": 12342341,
    "universidad": "Unisangil",
    "Estado": True,
    "Estatura": 1.73,
    "Edad": 18,
    "lista": ["Python", "Java", "C++"]
}

print(diccionario)

#Ejercicio 1 
programacion = {
    "Docente" : {
        "nombre": "Jesus",
        "Apellido": "...",
        "Cargo": "Profesor",
        "Telefono": 123,
        "Correo": "Jesusgmail.com"
    },
    "Estudiantes":[
        {
            "nombre": "Brayan",
            "apellido": "Rodriguez",
            "cedula": 12369241,
            "Correo": "Brayladino11gmail.com"
        },
        {
            "nombre": "Andres",
            "apellido": "Ramirez",
            "cedula": 12369241,
            "Correo": "Andres11gmail.com"
        }
    ],
    "Codigos" : "PROG",
    "Creditos": 3,
    "Estado": 1
}
for Estudiantes in programacion["Estudiantes"]:
    print(Estudiantes["nombre"])

#Items dentro del dicionario
print(programacion["Docente"].items())
#Kheys dentro de los dicionarios
print(programacion.keys())
print(programacion["Docente"].keys())

#Lsita de los estudiantes
for estudiantes in programacion["Estudiantes"]:
    print(Estudiantes.keys())

#Valores dentro de los dicionarios
print(programacion.values())

#Lista de los estudiantes
for estudiante in programacion["Estudiantes"]:
    print(estudiante.values())

#Get dentro los dicsionarios
print(programacion.get("creditos"))

#Agregar informacion 
programacion["Docente"]["nombre"] = "Jesus Caro"
print(programacion["Docente"]["nombre"])
#Agregar un atributo dentro de los diccionarios
programacion["programa"]="Ingeniera de sistemas"
print(programacion)
#Eliminar un atributo
del programacion["programa"]
print(programacion)


#Voleibol-------------------------------------

voleibol = {
    "Presidente":
    {
        "Nombre": "Maria",
        "Años de servicio": 18,
        "Cargo": "Organizador del partido"
    },
    "Jugadores":[
    {
        "nombre": "Juan Pablo",
        "años": 27,
        "Posicion": "Libero"
    },
    {
        "nombre": "Liberman",
        "años": 40,
        "Posicion": "Central"
    },
    {
        "nombre": "Humberto",
        "años": 35,
        "Posicion": "Levantador"
    }
    ],
    "Asistentes":[
    {
        "nombre": "Jose",
        "Ip": 352,
        "Sector": "Entrada"
    },
    {
        "nombre": "Daniel",
        "Ip": 201,
        "Sector": "Cafeterias"
    }
    ],
    "Nomble del equipo": "Big Boll",
    "Paiz": "Colombia",
    "Sitio": "Bogota"
}







