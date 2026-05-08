def analizarParidad(lista_numeros):

    conteo_pares = 0
    conteo_impares = 0

    for numero in lista_numeros:
        if type(numero) == int:
            if numero % 2 == 0:
                conteo_pares += 1
            else:
                conteo_impares += 1

    return conteo_pares, conteo_impares


def ejecutarPrograma():
    print("-- BIENVENIDO AL ANALIZADOR DE NÚMEROS --")
    datos_usuario = []
    continuar = True

    while continuar:
        entrada = input("Ingrese un número entero (o 'fin' para terminar): ")

        if entrada.lower() == "fin":
            continuar = False
        else:
            try:
                valor = int(entrada)
                datos_usuario.append(valor)
            except ValueError:
                print("Error: ¡Ese no es un número válido!")

    if len(datos_usuario) > 0:
        pares, impares = analizarParidad(datos_usuario)

        print("-- REPORTE DE RESULTADOS --")
        print("Total de números ingresados:", len(datos_usuario))
        print("Números Pares encontrados  :", pares)
        print("Números Impares encontrados:", impares)
        print("Lista completa de datos    :", datos_usuario)
    else:
        print("No se ingresaron datos para analizar.")


if __name__ == "__main__":
    ejecutarPrograma()
