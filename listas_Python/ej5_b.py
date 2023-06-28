
def lista_aleat():
    import random
    lista = []
    while (len(lista) < 23):
        i = random.randrange(1,101)
        if i not in lista:
            lista.append(i)
    return lista

def comprobar_duplicados(lista):

    if len(lista) == len(set(lista)):
        print('No hay elementos duplicados')
    else:
        print('Hay elementos duplicados')

lista = lista_aleat()

print(lista)
comprobar_duplicados(lista)