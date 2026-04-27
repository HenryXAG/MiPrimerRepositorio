def ejecutarContador():
    positivos = 0
    negativos = 0
    control = True

    print("-- INGRESO DE DATOS (0 PARA TERMINAR) --")

    while control:
        dato = input("Ingrese un número: ")

        # aqui validamos que no sea una letra falsa como el amor de ella
        try:
            numero = int(dato)

            if numero == 0:
                control = False
            elif numero > 0:
                positivos += 1
                print("Registrado: Positivo (+)")
            else:
                negativos += 1
                print("Registrado: Negativo (-)")

        except ValueError:
            print("Error: Eso no es un número válido, intenta de nuevo.")

    resumen = [["Positivos", positivos], ["Negativos", negativos]]

    print("-- RESUMEN FINAL --")

    for item in resumen:
        print("Total de", item[0], ":", item[1])


ejecutarContador()
