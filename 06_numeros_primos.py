def es_primo(numero):
    if numero < 2:
        return False
    ## aqui el for verifica si existe algún divisor entre 2 y la raíz del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def ejecutarPrimos():
    control = True

    while control:
        print("-- BUSCADOR DE PRIMOS (0 PARA SALIR) --")
        entrada = input("Ingrese el límite superior (n): ")

        try:
            n = int(entrada)

            if n == 0:
                print("Cerrando sesión de matemáticas... ¡Adiós!")
                control = False
            elif n < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                print("Números primos encontrados entre 1 y", n, ":")
                contador_primos = 0

                ## primer for: recorre de 1 hasta n
                for num in range(1, n + 1):
                    ## Segundo for dentro de la función que verifica si es primo
                    if es_primo(num):
                        print("->", num, "es primo")
                        contador_primos += 1

                print("Total de números primos encontrados:", contador_primos)

        except ValueError:
            print("Error: Ingrese un número entero válido.")


ejecutarPrimos()
