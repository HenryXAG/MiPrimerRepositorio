def auditarEdades(lista_edades):

    contador_adultos = 0
    MAYORIA_EDAD = 18

    for edad in lista_edades:
        if edad >= MAYORIA_EDAD:
            contador_adultos += 1

    return contador_adultos


def iniciarValidacion():
    print("-- SISTEMA DE REGISTRO DE CIUDADANÍA --")
    registro_edades = []
    total_personas = 6

    i = 0
    while i < total_personas:
        try:
            print("Persona #", i + 1)
            edad_ingresada = int(input("Ingrese la edad: "))

            if edad_ingresada >= 0 and edad_ingresada <= 120:
                registro_edades.append(edad_ingresada)
                i += 1
            else:
                print("Error: Ingrese una edad coherente (0-120).")
        except ValueError:
            print("Error: Solo se permiten números enteros para la edad.")

    adultos_encontrados = auditarEdades(registro_edades)
    menores_encontrados = len(registro_edades) - adultos_encontrados

    print("-- RESUMEN DE AUDITORÍA --")
    print("Edades procesadas     :", registro_edades)
    print("Total personas mayores:", adultos_encontrados)
    print("Total personas menores:", menores_encontrados)

    if adultos_encontrados > menores_encontrados:
        print("Resultado: El grupo está compuesto mayormente por adultos.")
    else:
        print("Resultado: El grupo tiene una carga mayor de menores de edad.")


if __name__ == "__main__":
    iniciarValidacion()
