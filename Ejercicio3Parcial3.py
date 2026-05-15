def monitorearTemperaturas():
    print("-- SISTEMA DE CONTROL DE SENSORES TÉRMICOS --")
    lecturas = []
    limite = 5

    i = 0
    while i < limite:
        try:
            print("Lectura del sensor #", i + 1)
            temp = int(input("Ingrese temperatura (número entero): "))
            lecturas.append(temp)
            i += 1
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    print("\n-- REPORTE DE ALERTAS DEL SISTEMA --")

    for t in lecturas:
        match t:
            case 0:
                print("Temperatura", t, "-> Alerta: Punto de Congelación")
            case 100:
                print("Temperatura", t, "-> Alerta: Punto de Ebullición")
            case _:
                estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
                print("Temperatura", t, "->", estado)


if __name__ == "__main__":
    monitorearTemperaturas()
