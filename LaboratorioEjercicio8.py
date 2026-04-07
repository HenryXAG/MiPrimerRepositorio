# aqui definimos la función de transformación osea la logica
def aplicar_transformacion(texto_entrada, opcion_entrada):
    """
    Función que decide la acción según el número recibido.
    """
    if opcion_entrada == 1:
        return texto_entrada.upper()
    elif opcion_entrada == 2:
        return texto_entrada.lower()
    elif opcion_entrada == 3:
        # aqui el formato titulo
        return texto_entrada.title()
    else:
        return "ERROR: Opción no válida."


## programa principal osea el menu

print("## BIENVENIDO AL PROCESADOR DE TEXTO ##")
print("-- Basado en Programación Lineal --")

# aqui es donde solicitamos el texto inicial como 'Serie'
texto_usuario = input("Ingresa el texto a procesar: ")

# aqui iniciamos el menú
print("¿Qué quieres hacer con tu texto?")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Formato de Título")
print("4. Salir del programa")

seleccion = input("Elige una opción (1-4): ")


## aqui la validación de memoria y ejecución

if seleccion.isdigit():
    opcion_num = int(seleccion)

    if opcion_num == 4:
        print("Saliendo del sistema... ¡Adiós!")
    elif opcion_num in [1, 2, 3]:
        # aqui llamamos a la función y guardamos el resultado osea el retorno
        resultado_final = aplicar_transformacion(texto_usuario, opcion_num)

        print("RESULTADO EN MEMORIA:")
        print(resultado_final)
    else:
        print("Esa opción no está en el índice del menú.")
else:
    print("Error: El sistema solo acepta números (isdigit = False).")

## ingeniero usted decía que va a tomar siempre el valor de la última modificación
## aquí el resultado final depende enteramente de la opción elegida.
