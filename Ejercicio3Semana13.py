def calcularResultadoFinal(lista_notas):

    sumatoria = 0
    cantidad_estudiantes = len(lista_notas)

    for nota in lista_notas:
        sumatoria += nota

    promedio = sumatoria / cantidad_estudiantes

    if promedio >= 6.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return promedio, estado


def gestionarNotas():
    print("-- SISTEMA DE CONTROL DE CALIFICACIONES --")
    registro_notas = []
    total_alumnos = 45

    i = 0
    while i < total_alumnos:
        try:
            print("Calificación del alumno #", i + 1)
            nota = float(input("Ingrese la nota (0.0 - 10.0): "))

            if nota >= 0 and nota <= 10:
                registro_notas.append(nota)
                i += 1
            else:
                print("Error: La nota debe estar entre 0 y 10, máquina.")
        except ValueError:
            print("Error: Ingreso no válido. Use números (ejemplo: 8.5).")

    promedio_final, veredicto = calcularResultadoFinal(registro_notas)

    print("-- RESUMEN DE RENDIMIENTO --")
    print("Total de notas procesadas:", len(registro_notas))
    print("Promedio general del grupo:", round(promedio_final, 2))
    print("Estado del grupo          :", veredicto)

    if veredicto == "APROBADO":
        print("Mensaje: ¡Felicidades al grupo por el esfuerzo!")
    else:
        print("Mensaje: Se requiere reforzar los temas de la semana.")


if __name__ == "__main__":
    gestionarNotas()
