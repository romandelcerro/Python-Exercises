pasajeros = []
ciudades = []

def agregar_pasajero(nombre, dni, destino):
    pasajeros.append((nombre, dni, destino))

def agregar_ciudad(nombre, pais):
    ciudades.append((nombre, pais))

def buscar_destino(dni):
    for pasajero in pasajeros:
        if pasajero[1] == dni:
            return pasajero[2]
    return None

def contar_pasajeros_por_ciudad(ciudad):
    contador = 0
    for pasajero in pasajeros:
        if pasajero[2] == ciudad:
            contador += 1
    return contador

def buscar_pais(dni):
    destino = buscar_destino(dni)
    if destino:
        for ciudad in ciudades:
            if ciudad[0] == destino:
                return ciudad[1]
    return None

while True:
    print("\n1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver destino por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Ver pais por DNI")
    print("6. Salir\n")

    opcion = int(input("Elige una opción (1-6): \n"))

    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        dni = input("Ingrese el DNI: ")
        destino = input("Ingrese el destino: ")
        agregar_pasajero(nombre, dni, destino)
    elif opcion == 2:
        nombre = input("Ingrese el nombre: ")
        pais = input("Ingrese el pais: ")
        agregar_ciudad(nombre, pais)
    elif opcion == 3:
        dni = input("Ingrese el DNI: ")
        destino = buscar_destino(dni)
        if destino:
            print("El destino es", destino)
        else:
            print("No se encontró el pasajero")
    elif opcion == 4:
        ciudad = input("Ingrese la ciudad: ")
        contador = contar_pasajeros_por_ciudad(ciudad)
        print("Hay", contador, "pasajeros viajando a", ciudad)
    elif opcion == 5:
        dni = input("Ingrese el DNI: ")
        pais = buscar_pais(dni)
        if pais:
            print("El dni:",dni,"viajará a", pais)
        else:
            print("No hay datos de viaje en el dni",dni)
    elif opcion == 6:
        exit(0)
    else:
        print("No has introducido una opcion correcta")