def obtener_nombres():
    """
    Solicita al usuario los nombres de los alumnos de primero y segundo de DAM
    y los almacena en dos conjuntos distintos. Finaliza la entrada de nombres
    cuando se introduce la letra 'X'.
    """
    primero = set()
    segundo = set()

    print("Introducir nombres de los alumnos de primero de DAM (introducir X para terminar):")
    while True:
        nombre = input()
        if nombre == 'X':
            break
        primero.add(nombre)

    print("Introducir nombres de los alumnos de segundo de DAM (introducir X para terminar):")
    while True:
        nombre = input()
        if nombre == 'X':
            break
        segundo.add(nombre)

    return primero, segundo

def mostrar_todos(primero, segundo):
    """
    Muestra los nombres de todos los alumnos de primero y de segundo sin repeticiones.
    """
    todos = primero.union(segundo)
    print("Nombres de todos los alumnos de primero y segundo:")
    for nombre in todos:
        print(nombre)
    
def mostrar_repetidos(primero, segundo):
    """
    Muestra los nombres que se repiten entre los alumnos de primero y de segundo.
    """
    repetidos = primero.intersection(segundo)
    print("Nombres que se repiten entre los alumnos de primero y segundo:")
    for nombre in repetidos:
        print(nombre)

def mostrar_no_repetidos(primero, segundo):
    """
    Muestra los nombres de los alumnos de primero que no se repiten en los de segundo.
    """
    no_repetidos = primero.difference(segundo)
    print("Nombres de los alumnos de primero que no se repiten en los de segundo:")
    for nombre in no_repetidos:
        print(nombre)

# Ejecución del programa
primero, segundo = obtener_nombres()
mostrar_todos(primero, segundo)
mostrar_repetidos(primero, segundo)
mostrar_no_repetidos(primero, segundo)