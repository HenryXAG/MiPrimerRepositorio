# aqui la entrada del año a evaluar
anio = int(input("Ingrese un año para verificar: "))


# Un año es bisiesto si es divisible entre 4 Y no entre 100 O es divisible entre 400
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año:", anio, "es un año BISIESTO")
else:
    print("El año:", anio, "es un año NORMAL")

## por cierto ingeniero , usé "anio" porque investigando me di cuenta que algunos
## programadores no usan la ñ porque puede dar bugs
