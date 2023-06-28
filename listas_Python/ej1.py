
lista1 = ["Mario", "Jesús", "Alejandro", "Alfonso"]
lista2 = ["Alejandro", "Alfonso"]

def eliminar_nombres(lista1, lista2):
    for nombre in lista2:
        if nombre in lista1:
            lista1.remove(nombre)
    return lista1


print(eliminar_nombres(lista1, lista2))

