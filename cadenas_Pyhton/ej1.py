def posiciones(cadena,fragmento):
    posiciones = []
    for i in range(len(cadena)):
        if cadena.startswith(fragmento,i):
            posiciones.append(i)
    return posiciones

print(posiciones("Mario Roman del Cerro","o"))