palabra = "reconocer"


palabra2 = palabra[::-1]

#Verificamos si la palabra es un palíndromo
if palabra == palabra2:
    print("La palabra '" + palabra + "' es palíndromo")
else:
    print("La palabra '" + palabra + "' no es palíndromo")