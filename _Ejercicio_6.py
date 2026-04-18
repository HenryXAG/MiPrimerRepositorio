dia_numero = int(input("Ingrese un número del 1 al 7: "))


if dia_numero == 1:
    print("Día correspondiente:", "Lunes")
elif dia_numero == 2:
    print("Día correspondiente:", "Martes")
elif dia_numero == 3:
    print("Día correspondiente:", "Miércoles")
elif dia_numero == 4:
    print("Día correspondiente:", "Jueves")
elif dia_numero == 5:
    print("Día correspondiente:", "Viernes")
elif dia_numero == 6:
    print("Día correspondiente:", "Sábado")
elif dia_numero == 7:
    print("Día correspondiente:", "Domingo")
else:
    # esta es una opcion por defecto para errores de rango
    print("Error:", "Número no válido. Debe ser del 1 al 7")
