def procesar_palabra(palabra, tipo_cambio):

    if tipo_cambio == 1:
        # MAYÚSCULAS
        resultado = palabra.upper()

    elif tipo_cambio == 2:
        # minúsculas
        resultado = palabra.lower()

    elif tipo_cambio == 3:
        # formato titulo
        resultado = palabra.title()

    else:
        resultado = "Error: Opción no válida (usa 1, 2 o 3)"

    print("Si esta bien ing :) :", resultado)


# Ejemplo 1: queremos la palabra en mayúsculas
procesar_palabra("alphonse", 1)

# Ejemplo 2: queremos corregir una frase en mayúsculas a minúsculas
procesar_palabra("GASOLINA", 2)

# Ejemplo 3: queremos formato de título para un nombre
procesar_palabra("edward elric", 3)
