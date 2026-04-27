def pedirNumero():
    numero = input("Ingrese un número (o presione '0' para salir): ")

    if numero.isdigit():
        return int(numero)
    else:
        print("Error: Ingrese un número entero válido.")
        return None


# función para procesar y mostrar los pares
def mostrarPares(n):
    print("Números pares entre 1 y", n, ":")

    ## este es el camino del for que recorre de 1 hasta n
    for i in range(1, n + 1):
        if i % 2 == 0:
            print("-", i)
    print("---------------------------------")


# función principal para el control del bucle while
def ejecutarPrograma():
    control = True

    while control:
        n = pedirNumero()

        if n == 0:
            print("Saliendo del sistema... ¡Adiós, Vaquero!")
            control = False
        elif n is not None:
            mostrarPares(n)


# con esto ejecutamos la función principal
ejecutarPrograma()
