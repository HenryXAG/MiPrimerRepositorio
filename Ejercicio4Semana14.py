def encontrarValorMayor(arreglo):

    mayor = arreglo[0]
    for numero in arreglo:
        if numero > mayor:
            mayor = numero

    return mayor


def ejecutarCaptura():
    print("-- DETECTOR DE VALORES MÁXIMOS --")
    lista_datos = []
    limite_datos = 8

    i = 0
    while i < limite_datos:
        try:
            print("Entrada #", i + 1)
            valor = int(input("Ingrese un número entero: "))
            lista_datos.append(valor)
            i += 1
        except ValueError:
            print("Error: Ingreso inválido. Por favor, digite un número entero.")

    if len(lista_datos) > 0:
        el_mayor = encontrarValorMayor(lista_datos)

        print("-- RESULTADO DEL ANÁLISIS --")
        print("Arreglo analizado       :", lista_datos)
        print("El número mayor de la lista es:", el_mayor)
        print("Posición en el arreglo  :", lista_datos.index(el_mayor))
    else:
        print("No hay datos para procesar.")


if __name__ == "__main__":
    ejecutarCaptura()
