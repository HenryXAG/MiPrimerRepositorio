def generarTriangulo():
    control = True

    while control:
        print("-- CREADOR DE TRIÁNGULOS IMPARES (0 PARA SALIR) --")
        entrada = input("Ingrese la altura del triángulo: ")

        try:
            n = int(entrada)

            if n == 0:
                print("Limpiando la consola... ¡Hasta la próxima!")
                control = False
            elif n < 0:
                print("Error: El triángulo no puede tener altura negativa.")
            else:
                print("Dibujando patrón para n =", n, ":")

                ## el for recorre desde la fila 1 hasta la n
                for i in range(1, n + 1):
                    ## este if valida si la fila actual (i) es impar
                    if i % 2 != 0:
                        print("*" * i)
                    else:
                        continue

        except ValueError:
            print("Error: Ingrese un número entero, no letras 'falsas'.")


generarTriangulo()
