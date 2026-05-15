from decimal import Decimal, getcontext

getcontext().prec = 10


def iniciarTerminal():
    print("-- TERMINAL DE COBRO SEGURO (BANCARIO) --")
    print("Instrucciones: Ingrese los precios. Presione '0' para totalizar.")

    total_acumulado = Decimal("0.00")
    activo = True

    while activo:
        entrada = input("Ingrese precio del producto: ")

        try:
            precio = Decimal(entrada)

            if precio == 0:
                activo = False
            elif precio < 0:
                print("Advertencia: No se permiten precios negativos.")
            else:
                total_acumulado += precio
                print("Monto registrado:", precio)

        except Exception:
            print("¡CUIDADO! Advertencia: El texto ingresado no es un número válido.")
            print("El sistema continuará operando...")

    print("\n-- CIERRE DE CAJA --")
    print(f"El total acumulado de la venta es: ${total_acumulado}")
    print("Gracias por usar el sistema de cobro seguro.")


if __name__ == "__main__":
    iniciarTerminal()
