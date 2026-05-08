def ordenarMenorAMayor(arreglo):

    n = len(arreglo)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arreglo[j] > arreglo[j + 1]:
                temporal = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = temporal

    return arreglo


def sistemaDeOrdenamiento():
    print("-- SISTEMA DE ORDENAMIENTO DE DATOS --")
    datos = []
    limite = 6

    i = 0
    while i < limite:
        try:
            print("Posición #", i + 1)
            num = int(input("Ingrese un número entero: "))
            datos.append(num)
            i += 1
        except ValueError:
            print("Error: Ingreso inválido. Solo números enteros.")
    print("Arreglo original  :", datos)

    lista_ordenada = ordenarMenorAMayor(datos[:])
    print("-- RESULTADO DEL ORDENAMIENTO --")
    print("Lista procesada   :", lista_ordenada)
    print("Estado            : Ordenado de menor a mayor correctamente.")


if __name__ == "__main__":
    sistemaDeOrdenamiento()
