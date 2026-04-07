def transformador_texto(frase, opcion):
    """
    funcion que recibe un texto  y un número.
    y aplica transformaciones según la opción elegida.
    """

    if opcion == 1:
        resultado = frase.upper()
        print("Transformación a Mayúsculas:")
        return resultado

    elif opcion == 2:
        resultado = frase.lower()
        print("Transformación a Minúsculas:")
        return resultado

    elif opcion == 3:

        resultado = frase.title()
        print("Transformación a Formato Título:")
        return resultado

    # Por si mandan un número que no existe
    else:
        return "Opción no válida. Elige 1, 2 o 3."


## Pruebas del ejercicio


serie_fav = "el alquimista de acero"


# aqui probamos la opción 1 de mayusculas
print(transformador_texto(serie_fav, 1))


# aqui probamos la opción 2 de minusculas
print(transformador_texto("SOLTALA, ERIKA", 2))


# aqui probamos la opción 3 de titulo
print(transformador_texto(serie_fav, 3))
