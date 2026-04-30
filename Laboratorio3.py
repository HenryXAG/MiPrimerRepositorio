def ejecutarBanco():

    saldo = 500.0
    movimientos = []
    control_menu = True

    print(" >BIENVENIDO AL BANCO DIGITAL< ")

    while control_menu:
        print(" | MENÚ DE OPERACIONES |  ")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Efectivo")
        print("4. Ver Historial de Movimientos")
        print("5. Salir del Sistema")

        opcion = input("Seleccione una opción (1-5): ")

        ## SIMULACIÓN DE SELECT CASE (Estructura de Decisión)
        if opcion == "1":
            print("Su saldo actual es: $", saldo)

        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    movimientos.append(["Depósito", monto])
                    print("¡Éxito! Depósito de $", monto, "realizado.")
                else:
                    print("Error: El monto debe ser positivo.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                if monto > saldo:
                    print("Fondos insuficientes. Su saldo es de: $", saldo)
                elif monto <= 0:
                    print("Error: Monto no válido.")
                else:
                    saldo -= monto
                    movimientos.append(["Retiro", monto])
                    print("¡Éxito! Retire su dinero. Nuevo saldo: $", saldo)
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        elif opcion == "4":
            print(" >HISTORIAL DE MOVIMIENTOS< ")
            if len(movimientos) > 0:
                for i, item in enumerate(movimientos):
                    # item[0] es el tipo y item[1] es el valor
                    print(
                        "Movimiento #", i + 1, ":", item[0], "por valor de $", item[1]
                    )
            else:
                print("No hay movimientos registrados en esta sesión.")

        elif opcion == "5":
            print("Cerrando sesión segura... ¡Gracias por usar Banco Monopoly!")
            control_menu = False

        else:
            print("Opción no válida. Intente de nuevo.")


ejecutarBanco()
