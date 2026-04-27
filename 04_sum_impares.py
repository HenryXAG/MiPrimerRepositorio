def sumaImpares():
    lista_impares = []  ## este es el array para guardar los impares
    suma_total = 0
    control = True

    print("-- REGISTRO DE NÚMEROS IMPARES (0 PARA SALIR) --")

    while control:
        entrada = input("Ingrese un número: ")

        try:
            numero = int(entrada)

            if numero == 0:
                control = False
            else:
                if numero % 2 != 0:
                    suma_total += numero
                    lista_impares.append(numero)
                    print("El número", numero, "es impar y fue sumado.")
                else:
                    print("El número", numero, "es par, no se toma en cuenta.")

        except ValueError:
            print("Error: Eso no es un número, ingresa un valor válido.")

    print("---------------------------------")
    print("La suma total de los impares es:", suma_total)

    print("Los números impares ingresados fueron:")
    if len(lista_impares) > 0:
        for impar in lista_impares:
            print("-", impar)
    else:
        print("No se ingresaron números impares.")


## con esto arrancamos la función
sumaImpares()
