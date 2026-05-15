def procesarEtiqueta():
    print("-- SISTEMA DE CLASIFICACIÓN DE ENVÍOS PRO --")

    etiqueta = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ").strip()

    if etiqueta == "" or etiqueta is None:
        print("Error: La entrada está vacía o nula. Programa finalizado.")
        return

    categoria = etiqueta[5:-3]

    print("Sección central extraída:", categoria)

    tipo_ruta = "Ruta Local" if etiqueta[-2:].upper() == "SV" else "Ruta Internacional"
    print("Destino final:", tipo_ruta)


if __name__ == "__main__":
    procesarEtiqueta()
