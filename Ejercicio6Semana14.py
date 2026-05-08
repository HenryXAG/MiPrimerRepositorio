import random


def contarMayoresAlUmbral(lista_numeros, umbral):

    contador = 0
    for n in lista_numeros:
        if n > umbral:
            contador += 1
    return contador


def ejecutarSimulacion():
    print("-- GENERADOR Y AUDITOR DE DATOS ALEATORIOS --")
    numeros_generados = []
    cantidad_datos = 10
    valor_referencia = 50

    print("Generando", cantidad_datos, "números aleatorios...")
    for i in range(cantidad_datos):
        numero_azar = random.randint(1, 100)
        numeros_generados.append(numero_azar)

    total_mayores = contarMayoresAlUmbral(numeros_generados, valor_referencia)
    print("-- REPORTE DE AUDITORÍA --")
    print("Arreglo generado :", numeros_generados)
    print("Umbral de medida :", valor_referencia)
    print(
        "Resultado        :", total_mayores, "números son mayores a", valor_referencia
    )

    if total_mayores > (cantidad_datos / 2):
        print("Tendencia: La mayoría de los números son altos.")
    else:
        print("Tendencia: La mayoría de los números son bajos o equilibrados.")


if __name__ == "__main__":
    ejecutarSimulacion()
