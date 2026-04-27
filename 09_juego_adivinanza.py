import random


def jugarAdivina():
    numero_secreto = random.randint(1, 50)
    intentos_realizados = []  ## array para guardar cada número que el usuario arriesga
    acerto = False

    print("-- BIENVENIDO AL DOJO DE ADIVINANZA --")
    print("He pensado un número entre 1 y 50. ¿Puedes encontrarlo?")

    while not acerto:
        entrada = input("Ingresa tu número: ")

        try:
            intento = int(entrada)
            intentos_realizados.append(intento)

            # el if para validar y dar pistas
            if intento == numero_secreto:
                print("¡LO LOGRASTE! Has dado en el blanco.")
                acerto = True
            elif intento < numero_secreto:
                print("Pista: El número secreto es MAYOR.")
            else:
                print("Pista: El número secreto es MENOR.")

        except ValueError:
            print(
                "Error: Ingresa un número válido, no engaños 'falsos como el para siempre'."
            )

    ## al final for para mostrar el resumen de la batalla
    print("-- RESUMEN DE TU PARTIDA --")
    print("Lograste acertar en", len(intentos_realizados), "intentos.")
    print("Este fue el orden de tus intentos:")

    for i, valor in enumerate(intentos_realizados):
        print("Tiro #", i + 1, ":", valor)


jugarAdivina()
