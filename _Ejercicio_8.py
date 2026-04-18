## aqui la entrada de datos de los tres lados
lado1 = float(input("Ingrese la medida del primer lado: "))
lado2 = float(input("Ingrese la medida del segundo lado: "))
lado3 = float(input("Ingrese la medida del tercer lado: "))


if lado1 == lado2 and lado2 == lado3:
    # Si todos los lados son iguales
    print("El triángulo es: ", "EQUILÁTERO")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    # Si por lo menos dos lados coinciden
    print("El triángulo es: ", "ISÓSCELES")
else:
    # Si ningún camino es igual que es por defecto
    print("El triángulo es: ", "ESCALENO")

## usé and para que se cumplan todas las igualdades
## y or para verificar si al menos una pareja de lados es igual
