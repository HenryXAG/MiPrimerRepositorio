def sumaAcumulativa():
    lista_numbers = []
    suma_total = 0
    limite = 100

    print("-- INGRESO DE DATOS (OBJETIVO: SUPERAR", limite, ") --")

    ## el while se ejecuta mientras la suma sea menor o igual al límite
    while suma_total <= limite:
        print("Suma actual:", suma_total)
        entrada = input("Ingrese un número para sumar: ")

        try:
            numero = int(entrada)

            if numero < 0:
                print("Los números negativos no se suman en este dojo.")
            else:
                suma_total += numero
                lista_numbers.append(numero)

                falta = limite - suma_total
                if falta < 0:
                    falta = 0

                print("¡Sumado! Faltan", falta, "para el objetivo.")

        except ValueError:
            print("Error: Eso no es un número. Ingresa un valor real.")

    print("-- ¡OBJETIVO ALCANZADO! --")
    print("La suma final fue de:", suma_total)

    print("Los números que conformaron la suma son:")
    for i, num in enumerate(lista_numbers):
        print("Ingreso", i + 1, ":", num)


sumaAcumulativa()
