def filtrarNombresLargos(lista_nombres):

    nombres_filtrados = []

    for nombre in lista_nombres:
        nombre_limpio = nombre.strip()

        if len(nombre_limpio) > 5:
            nombres_filtrados.append(nombre_limpio)

    return nombres_filtrados


def iniciarSistema():
    print("-- SISTEMA DE GESTIÓN DE NOMBRES --")
    directorio_completo = []
    limite = 10

    i = 0
    while i < limite:
        print("Registro #", i + 1)
        nombre_ingresado = input("Ingrese un nombre: ")

        if nombre_ingresado.strip() == "":
            print("Error: El nombre no puede estar vacío.")
        else:
            directorio_completo.append(nombre_ingresado)
            i += 1

    resultados = filtrarNombresLargos(directorio_completo)

    print("-- REPORTE DE FILTRADO (Nombres > 5 letras) --")
    if len(resultados) > 0:
        print("Se encontraron", len(resultados), "nombres que cumplen el criterio:")
        for n in resultados:
            print("->", n)
    else:
        print("Ninguno de los nombres ingresados es mayor a 5 caracteres.")


if __name__ == "__main__":
    iniciarSistema()
