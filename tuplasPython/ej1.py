from collections import Counter

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __repr__(self):
        return f"{self.valor}{self.palo}"


def leer_carta():
    valor = input("Inserta el valor de la carta (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A): ")
    palo = input("Inserta el palo de la carta (C, D, T, P): ")
    return (valor, palo)

def es_color(mano):
    return len(set([carta.palo for carta in mano])) == 1

def es_escalera_color(mano):
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valores_mano = [valores.index(carta.valor) for carta in mano]
    valores_mano.sort()
    escalera = all(valores_mano[i] == valores_mano[i-1] + 1 for i in range(1, 5))
    mismo_palo = len(set([carta.palo for carta in mano])) == 1
    return escalera and mismo_palo

def es_escalera(mano):
    valores = [carta.valor for carta in mano]
    valores.sort()
    return all(valores[i] == str(10 + i) for i in range(5))

def es_poker(mano):
    contador = Counter([carta.valor for carta in mano])
    return 4 in contador.values()

def es_full(mano):
    contador = Counter([carta.valor for carta in mano])
    valores_unicos = set(contador.values())
    return len(valores_unicos) == 2 and 3 in valores_unicos and 2 in valores_unicos

def es_trio(mano):
    contador = Counter([carta.valor for carta in mano])
    return 3 in contador.values()

def es_doble_pareja(mano):
    contador = Counter([carta.valor for carta in mano])
    return len(contador.values()) == 3 and 2 in contador.values()

def es_pareja(mano):
    contador = Counter([carta.valor for carta in mano])
    return 2 in contador.values()

mano = [Carta(*leer_carta()) for _ in range(5)]
for i, carta in enumerate(mano):
    print(f"Carta {i+1}: {carta}")
if es_escalera_color(mano):
    print("Escalera de color")
elif es_color(mano):
    print("Color")
elif es_escalera(mano):
    print("Escalera")
elif es_poker(mano):
    print("Póker")
elif es_full(mano):
    print("Full")
elif es_trio(mano):
    print("Trío")
elif es_doble_pareja(mano):
    print("Doble Pareja")
elif es_pareja(mano):
    print("Pareja")
else:
    print("Carta Alta")