
def duplicado(lista):

    for i in lista:
        if lista.count(i) > 1:
            return True
    return False

print(duplicado([1,2,3,4,3]))