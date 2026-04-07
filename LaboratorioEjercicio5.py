def transformador_seguro(texto, opcion):

    if opcion == 1:
        resultado = texto.upper()
        print("Acción 1 (Mayúsculas):", resultado)

    elif opcion == 2:
        resultado = texto.lower()
        print("Acción 2 (Minúsculas):", resultado)

    elif opcion == 3:
        # formato titulo
        resultado = texto.title()
        print("Acción 3 (Título):", resultado)

    else:
        # Si el número no es 1, 2 o 3, caemos en este espacio de memoria
        print("OPCIÓN INVÁLIDA")
        print("Por favor, elige un número que esté en el sistema (1, 2 o 3).")


## PRUEBAS DE VALIDACIÓN

serie_ejemplo = "Dragon Ball"

# Prueba con opción válida
print("Prueba 1")
transformador_seguro(serie_ejemplo, 1)

# Prueba con opción invalida que es 5
print("Prueba 2")
transformador_seguro(serie_ejemplo, 5)

# Prueba con otra opción invalida que es 0
print("Prueba 3")
transformador_seguro("Goku", 0)
