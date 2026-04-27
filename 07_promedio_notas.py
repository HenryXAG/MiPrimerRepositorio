def calcularPromedio():
    notas_validas = []
    control = True

    print("-- INGRESO DE NOTAS (NOTAS DE 0 A 10 | -1 PARA TERMINAR) --")

    while control:
        entrada = input("Ingrese la nota: ")

        try:
            nota = float(entrada)  # uso float para notas como 8.5

            if nota == -1:
                control = False
            ## con esto filtramos las notas inválidas con un if
            elif nota < 0 or nota > 10:
                print("Nota no válida. Debe estar entre 0 y 10.")
            else:
                notas_validas.append(nota)
                print(f"Nota {nota} registrada con éxito.")

        except ValueError:
            print("Error: Eso no es una nota válida, ninja.")

    ## con esto calculamos el promedio usando un for para recorrer las notas válidas
    if len(notas_validas) > 0:
        suma_notas = 0
        print("-- RESUMEN DE NOTAS REGISTRADAS --")

        for n in notas_validas:
            print(f"- Nota: {n}")
            suma_notas += n

        promedio = suma_notas / len(notas_validas)
        print(f"El promedio final es: {round(promedio, 2)}")

        if promedio >= 6:
            print("Resultado: APROBADO")
        else:
            print("Resultado: REPROBADO")
    else:
        print("No se ingresaron notas para calcular el promedio.")


calcularPromedio()
