def transformador_en_cadena(texto_base, lista_opciones):
    """
    funcion que recibe un string y un Array de números.
    pasa el resultado de una transformación a la siguiente.
    """

    resultado_actual = texto_base

    print(f"Texto inicial en memoria: '{resultado_actual}'")

    # con esto recorremos la lista de números
    for opcion in lista_opciones:

        if opcion == 1:
            ## mayusculas
            resultado_actual = resultado_actual.upper()
            print(f"-> Aplicando Mayúsculas: {resultado_actual}")

        elif opcion == 2:
            ## minusculas
            resultado_actual = resultado_actual.lower()
            print(f"-> Aplicando Minúsculas: {resultado_actual}")

        elif opcion == 3:
            ## formato titulo
            resultado_actual = resultado_actual.title()
            print(f"-> Aplicando Formato Título: {resultado_actual}")

        else:
            print(f"-> Opción {opcion} no reconocida. Saltando...")

    # aqui es donde retorna el estado final después de todas las modificaciones
    return resultado_actual


## ESPACIO DE PRUEBA


# como su ejemplo de FullmetalCapitalizer que hizo ing :)
mi_serie = "Dragon Ball"
secuencia_de_cambios = [1, 2, 3]  # aqui va de mayusculas a minusculas y formato titulo

print("-- INICIANDO CADENA DE TRANSFORMACIÓN --")
resultado_final = transformador_en_cadena(mi_serie, secuencia_de_cambios)

print("- RESULTADO FINAL EN MEMORIA -")
print(f"Variable final: {resultado_final}")
