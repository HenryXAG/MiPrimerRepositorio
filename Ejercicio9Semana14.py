def sumarSoloNumerosPares(arreglo):

    acumulador_suma = 0

    for numero in arreglo:
        if numero % 2 == 0:
            acumulador_suma += numero

    return acumulador_suma


def ejecutarProceso():
    print("-- CALCULADORA DE SUMATORIA FILTRADA --")
    numeros_usuario = []
    cantidad_elementos = 6

    i = 0
    while i < cantidad_elementos:
        try:
            print("Elemento #", i + 1)
            valor = int(input("Ingrese un número entero: "))
            numeros_usuario.append(valor)
            i += 1
        except ValueError:
            print("Error: Ingreso no válido. Debe ser un número entero.")

    total_par = sumarSoloNumerosPares(numeros_usuario)

    print("-- RESULTADO DE LA SUMATORIA --")
    print("Arreglo ingresado      :", numeros_usuario)
    print("Total suma (Solo pares):", total_par)

    if total_par == 0:
        print("Nota: No se encontraron números pares para sumar en la lista.")
    else:
        print("Proceso completado exitosamente.")


if __name__ == "__main__":
    ejecutarProceso()
