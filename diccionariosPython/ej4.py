"""
Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y
números de teléfono. El programa nos dará el siguiente menú:
Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se
encuentra, debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres
comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.
"""

agenda = {}

def agregar_modificar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in agenda:
        print("El número de teléfono de", nombre, "es", agenda[nombre])
        opcion = input("¿Desea modificar el número de teléfono (s/n)? ")
        if opcion == 's':
            numero = input("Ingrese el nuevo número de teléfono: ")
            agenda[nombre] = numero
    else:
        numero = input("Ingrese el número de teléfono: ")
        agenda[nombre] = numero

def buscar_contacto():
    cadena = input("Ingrese la cadena de caracteres a buscar: ")
    resultados = []
    for nombre, numero in agenda.items():
        if nombre.startswith(cadena):
            resultados.append((nombre, numero))
    if resultados:
        print("Resultados de la búsqueda:")
        for nombre, numero in resultados:
            print(nombre, numero)
    else:
        print("No se encontraron resultados.")

def borrar_contacto():
    nombre = input("Ingrese el nombre del contacto a borrar: ")
    if nombre in agenda:
        confirmacion = input("¿Está seguro de que desea borrar a " + nombre + " (s/n)? ")
        if confirmacion == 's':
            del agenda[nombre]
            print("El contacto ha sido borrado.")
    else:
        print("El contacto no existe en la agenda.")

def listar_contactos():
    print("Contactos en la agenda:")
    for nombre, numero in agenda.items():
        print(nombre, numero)

while True:
    opcion = input("\nMenú de opciones:\n1. Añadir/modificar contacto\n2. Buscar contacto\n3. Borrar contacto\n4. Listar contactos\n5. Salir\nSeleccione una opción (1-5): ")
    if opcion == '1':
        agregar_modificar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        borrar_contacto()
    elif opcion == '4':
        listar_contactos()
    elif opcion == '5':
        break
    else:
        print("Opción inválida.")