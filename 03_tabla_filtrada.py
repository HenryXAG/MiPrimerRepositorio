def generarTabla():
    control = True

    while control:
        print("-- GENERADOR DE TABLAS (MAYORES A 20) --")
        entrada = input("Ingrese un número (o '-1' para salir): ")

        ## aqui validamos la entrada para que sea verdadera
        try:
            numero = int(entrada)

            if numero == -1:
                print("Cerrando el laboratorio... ¡Hasta pronto!")
                control = False
            else:
                print("Resultados de la tabla del", numero, "que son mayores a 20:")
                encontrados = False

                ## aqui el for genera la tabla del 1 al 10
                for i in range(1, 11):
                    resultado = numero * i

                    ## El if filtra solo los que superan el 20
                    if resultado > 20:
                        print(numero, "x", i, "=", resultado)
                        encontrados = True

                if not encontrados:
                    print("Ningún resultado de esta tabla es mayor a 20.")

        except ValueError:
            print("Error: Ingrese un número entero válido.")


## esto es para ejecutar un motor de tablas
generarTabla()
