def transformar_y_contar(texto, opcion):
    """
    función que transforma el texto y retorna el número de caracteres.
    """

    # 1. aqui va la lógica de transformación
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        # aqui formato titulo
        resultado = texto.title()
    else:
        # Si la opción es inválida, devolvemos un mensaje y longitud 0
        print("Opción inválida en el sistema.")
        return 0

    ## 2. Mostramos el resultado transformado osea acción
    print(f"Texto procesado: {resultado}")

    ## 3. ahora retornamos la cantidad de caracteres
    # recordando que el string es una lista de caracteres en memoria
    cantidad = len(resultado)
    return cantidad


## PRUEBAS DE EJECUCIÓN

# Ejemplo con Dragon Ball
serie = "Dragon Ball"

print("--INICIANDO PROCESO --")
total_caracteres = transformar_y_contar(serie, 1)

# aqui muestro el valor retornado
print(f"La cantidad de caracteres es: {total_caracteres}")

# y aqui un ejemplo con una frase con espacios
frase_larga = "  Son Goku  "
conteo_goku = transformar_y_contar(frase_larga, 3)
print(
    f"La frase '{frase_larga.strip()}' tiene {conteo_goku} espacios de memoria ocupados."
)
