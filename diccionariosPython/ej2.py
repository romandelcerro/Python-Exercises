#Vamos a crear un programa en Python, donde vamos a declarar un diccionario para guardar los
#precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha
#vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el
#diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos
#preguntará si queremos hacer otra consulta.

# Diccionario con precios de las frutas
precios = {
    "manzana": 0.5,
    "kiwi": 0.25,
    "pera": 0.75,
    "mandarina": 0.3
}

# Función para calcular el precio final de la fruta
def calcular_precio(nombre_fruta, cantidad):
    # Verificar si la fruta existe en el diccionario de precios
    if nombre_fruta in precios:
        precio_unitario = precios[nombre_fruta]
        precio_final = precio_unitario * cantidad
        return precio_final
    else:
        return "Fruta no encontrada"

# Bucle para hacer múltiples consultas
seguir_consultando = True
while seguir_consultando:
    # Pedir el nombre de la fruta y la cantidad
    nombre_fruta = input("Introduce el nombre de la fruta: ")
    cantidad = int(input("Introduce la cantidad: "))

    # Calcular el precio final de la fruta
    precio_final = calcular_precio(nombre_fruta, cantidad)

    # Mostrar el precio final
    print("Precio final: ", precio_final)

    # Preguntar si se quiere hacer otra consulta
    continuar = input("¿Deseas hacer otra consulta? (si/no) ")
    if continuar.lower() != "si":
        seguir_consultando = False