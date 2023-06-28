def separacion_miles(num):
    num = str(num)
    result = ""
    contador = 0
    for i in range(len(num)-1, -1, -1):
        result = num[i] + result
        contador += 1
        if contador == 3 and i != 0:
            result = "." + result
            contador = 0
    return result

print(separacion_miles(1234567890))