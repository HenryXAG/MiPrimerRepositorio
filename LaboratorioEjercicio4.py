def transformar_lista_palabras(lista_de_datos, opcion):
    """
    función que recibe un Array, y aplica cambios a cada índice.
    """
    # aqui pongo una lista vacía para guardar los resultados nuevos
    lista_transformada = []

    # Recorremos la lista
    for palabra in lista_de_datos:

        if opcion == 1:
            resultado = palabra.upper()

        elif opcion == 2:
            resultado = palabra.lower()

        elif opcion == 3:
            resultado = palabra.title()

        else:
            resultado = "Opción Inválida"

        # agrego el resultado a la nueva lista
        lista_transformada.append(resultado)

    # Retorno el arreglo completo ya modificado :)
    return lista_transformada


## DATOS DE PRUEBA

# Array con nombres de personajes o series
mis_series = ["fullmetal", "chapulin colorado", "song", "cristiano"]

print("LISTA ORIGINAL")
print(mis_series)

# toda la lista a formato título
resultado_final = transformar_lista_palabras(mis_series, 3)

print("Lista Transformada (Títulos)")
print(resultado_final)

# toda la lista a Mayusculas
resultado_mayus = transformar_lista_palabras(mis_series, 1)
print("LISTA TRANSFORMADA (Mayúsculas)")
print(resultado_mayus)
