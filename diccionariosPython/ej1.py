#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
#apariciones de cada carácter en la cadena.

# Función para contar apariciones de caracteres en una cadena
def contar_caracteres(cadena):
    # Crear un diccionario vacío para almacenar los resultados
    resultados = {}

    # Recorrer la cadena y contar las apariciones de cada carácter
    for caracter in cadena:
        if caracter in resultados:
            resultados[caracter] += 1
        else:
            resultados[caracter] = 1

    # Devolver el diccionario de resultados
    return resultados

# Leer una cadena del usuario
cadena = input("Introduce una cadena: ")

# Llamar a la función y guardar el resultado
resultados = contar_caracteres(cadena)

# Imprimir los resultados
print("Resultados:")
for caracter, conteo in resultados.items():
    print(f"{caracter}: {conteo}")