def buscarEnInventario(lista_productos, producto_buscado):

    objetivo = producto_buscado.strip().lower()
    encontrado = False

    for producto in lista_productos:
        if producto.strip().lower() == objetivo:
            encontrado = True
            break

    return encontrado


def gestionarInventario():
    print("-- SISTEMA DE CONTROL DE BODEGA --")
    catalogo = [
        "Procesador",
        "Memoria RAM",
        "Disco Duro",
        "Tarjeta Madre",
        "Fuente Poder",
    ]

    print("Productos disponibles en sistema:", len(catalogo))
    print("Catálogo:", catalogo)

    busqueda = input("Ingrese el nombre del producto que desea buscar: ")

    if busqueda.strip() == "":
        print("Error: No ingresó ningún término de búsqueda.")
    else:
        resultado = buscarEnInventario(catalogo, busqueda)

        print("-- RESULTADO DE LA CONSULTA --")
        if resultado:
            print("El producto", busqueda, "se encuentra registrado en bodega.")
        else:
            print("AVISO: El producto", busqueda, "no existe en nuestro inventario.")


if __name__ == "__main__":
    gestionarInventario()
