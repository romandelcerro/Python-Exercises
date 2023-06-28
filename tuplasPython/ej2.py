def diaSiguienteE(dia, mes, anio):

    # Determina si el año es bisiesto
    bisiesto = False
    if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0):
        bisiesto = True

    # Determina el número de días en el mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dia = 31
    elif mes in [4, 6, 9, 11]:
        max_dia = 30
    elif bisiesto and mes == 2:
        max_dia = 29
    else:
        max_dia = 28

    # Calcula el día siguiente
    if dia < max_dia:
        dia += 1
    else:
        dia = 1
        if mes < 12:
            mes += 1
        else:
            mes = 1
            anio += 1

    # Devuelve el día siguiente en el formato (día, mes, año)
    return dia, mes, anio


dia_siguiente = diaSiguienteE(13,2,2023)
print("El día siguiente al 13,2,2023 es", dia_siguiente)
