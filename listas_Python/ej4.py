lista = [1,2,0,5]

ordenada = True
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break
if ordenada:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")