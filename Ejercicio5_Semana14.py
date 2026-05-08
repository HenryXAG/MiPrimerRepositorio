def filtrarSoloPositivos(arreglo_original):

    lista_positivos = []

    for numero in arreglo_original:
        if numero > 0:
            lista_positivos.append(numero)

    return lista_positivos


def ejecutarSistema():
    print("-- FILTRADOR DE DATOS NUMÉRICOS --")
    datos_mixtos = []
    cantidad = 7

    i = 0
    while i < cantidad:
        try:
            print("Dato #", i + 1)
            valor = int(input("Ingrese un número (positivo o negativo): "))
            datos_mixtos.append(valor)
            i += 1
        except ValueError:
            print("Error: Titán, recuerda ingresar solo números enteros.")

    resultado_positivos = filtrarSoloPositivos(datos_mixtos)
    print("-- RESULTADOS DEL PROCESAMIENTO --")
    print("Lista original completa :", datos_mixtos)

    if len(resultado_positivos) > 0:
        print("Nuevo arreglo generado  :", resultado_positivos)
        print("Total de positivos      :", len(resultado_positivos))
    else:
        print("Resultado: No se encontraron números positivos en la lista.")


if __name__ == "__main__":
    ejecutarSistema()
