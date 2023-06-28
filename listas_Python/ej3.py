lista_1 = ['Jesús', 'Mario', 'Alfonso', 'Alejandro', 'Humberto']
lista_2 = ['Jesús', 'Mario', 'Marisa', 'Ruben', 'Natalia']

# Eliminar los elementos repetidos de cada lista
lista_1_sin_repeticiones = list(dict.fromkeys(lista_1))
lista_2_sin_repeticiones = list(dict.fromkeys(lista_2))

# Lista de palabras que aparecen en las dos listas
lista_palabras_iguales = list(set(lista_1_sin_repeticiones) & set(lista_2_sin_repeticiones))
print("Palabras que aparecen en las dos listas:", lista_palabras_iguales)

# Lista de palabras que aparecen en la primera lista, pero no en la segunda
lista_palabras_1 = list(set(lista_1_sin_repeticiones) - set(lista_2_sin_repeticiones))
print("Palabras que aparecen en la primera lista, pero no en la segunda:", lista_palabras_1)

# Lista de palabras que aparecen en la segunda lista, pero no en la primera
lista_palabras_2 = list(set(lista_2_sin_repeticiones) - set(lista_1_sin_repeticiones))
print("Palabras que aparecen en la segunda lista, pero no en la primera:", lista_palabras_2)

# Lista de palabras que aparecen en ambas listas
lista_todas_palabras = list(set(lista_1_sin_repeticiones) | set(lista_2_sin_repeticiones))
print("Palabras que aparecen en ambas listas:", lista_todas_palabras)