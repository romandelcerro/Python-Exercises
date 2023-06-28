"""
Vamos a crear un programa en Python, que nos permita guardar los nombres de los alumnos de
DAM2 y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas.
Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los
valores serán listas con las notas de cada alumno.
El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá
pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos
mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
"""

# Diccionario para guardar los nombres de los alumnos y sus notas
alumnos = {}

# Preguntar el número de alumnos a introducir
num_alumnos = int(input("Introduce el número de alumnos: "))

# Bucle para introducir la información de cada alumno
for i in range(num_alumnos):
    # Pedir el nombre del alumno
    nombre = input("Introduce el nombre del alumno: ")

    # Verificar si el alumno ya existe en el diccionario
    if nombre in alumnos:
        print("Error: el alumno ya existe")
        continue

    # Inicializar la lista de notas del alumno
    notas = []

    # Pedir las notas del alumno hasta introducir un número negativo
    nota = float(input("Introduce la nota (negativo para terminar): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Introduce la nota (negativo para terminar): "))

    # Guardar las notas del alumno en el diccionario
    alumnos[nombre] = notas

# Mostrar la información de cada alumno y su nota media
for nombre, notas in alumnos.items():
    media = sum(notas) / len(notas)
    print("Alumno: ", nombre)
    print("Notas: ", notas)
    print("Media: ", media)