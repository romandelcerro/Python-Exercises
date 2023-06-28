def n1(numero):
    decimal = 0
    for digito in numero:
        decimal = decimal*2 + int(digito)
    return decimal

print(n1("1100"))