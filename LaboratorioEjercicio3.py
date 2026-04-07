def transformar_dinamico(texto_usuario, opcion_elegida):
    if opcion_elegida == 1:
        resultado = texto_usuario.upper()
    elif opcion_elegida == 2:
        resultado = texto_usuario.lower()
    elif opcion_elegida == 3:
        resultado = texto_usuario.title()
    else:
        resultado = "La opción no existe en el sistema."

    print("PROCESO COMPLETADO")
    print(f"Resultado: {resultado}")


# 2. Solicitud de datos osea que entrada de usuario

print("BIENVENIDO AL SISTEMA DE TRANSFORMACIÓN JOVEN")
frase = input("Pon una frase o nombre de serie: ")

print("Menu de opciones:")
print("1. Todo a Mayúsculas")
print("2. Todo a Minúsculas")
print("3. Formato Título")

seleccion = input("Elige el número de tu opción: ")


# 3. Esta es la ejecucion o validacion

if seleccion.isdigit():
    # texto a número entero para la función
    opcion_num = int(seleccion)
    transformar_dinamico(frase, opcion_num)
else:
    print("Error: Debes ingresar un número válido (1, 2 o 3).")
