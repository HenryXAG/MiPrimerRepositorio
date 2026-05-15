def enmascararDatos():
    print("-- SISTEMA DE PRIVACIDAD DE DATOS --")

    nombre_completo = input("Ingrese su nombre y apellido: ")

    if nombre_completo.strip() == "":
        print("Error: No se ingresaron datos para procesar.")
        return

    lista_nombres = nombre_completo.split()
    lista_invertida = lista_nombres[::-1]

    print("\n-- FORMATO DE PRIVACIDAD APLICADO --")

    registro_ofuscado = ""

    for palabra in lista_invertida:
        palabra_formateada = ""

        for letra in palabra:
            palabra_formateada += letra + "."

        palabra_formateada = palabra_formateada[:-1]

        registro_ofuscado += palabra_formateada + "  -  "

    registro_ofuscado = registro_ofuscado[:-5]

    print("Resultado final:", registro_ofuscado)


if __name__ == "__main__":
    enmascararDatos()
