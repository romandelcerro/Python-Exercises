import random

# Solicitamos el límite mínimo
min = int(input('Ingresa el límite mínimo: '))

# Solicitamos el límite máximo
max = int(input('Ingresa el límite máximo: '))

# Generamos un número aleatorio entre el mínimo y el máximo
aleatorio = random.randint(min, max)

# Creamos un contador para los intentos
intentos = 0

# Pedimos al usuario que adivine
while True:
    numero = int(input("Adivina el número ("+str(min)+"-"+str(max)+"):"))
    intentos += 1

    # Comprobamos si el número es el correcto
    if numero == aleatorio:
        print("¡Has adivinado el número! Has necesitado {} intentos".format(intentos))
        break
    elif numero > aleatorio:
        print("Demasiado alto")
    elif numero < aleatorio:
        print("Demasiado bajo")