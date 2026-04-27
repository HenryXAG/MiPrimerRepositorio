def sistemaSeguridad():
    clave_maestra = "Henry123"
    intentos_fallidos = []  ## este es un array para guardar los errores
    acceso_concedido = False

    print("-- SISTEMA DE SEGURIDAD ACTIVADO --")

    while not acceso_concedido:
        password = input("Ingrese su contraseña: ")

        ## esto para validar si coincide con el if
        if password == clave_maestra:
            print("¡Acceso permitido! Bienvenido al sistema.")
            acceso_concedido = True
        else:
            print("Acceso denegado. Intente de nuevo.")
            ## con esto guardamos el intento fallido en nuestro arreglo
            intentos_fallidos.append(password)

    print("-- REPORTE DE SEGURIDAD --")
    print("Total de intentos fallidos:", len(intentos_fallidos))

    if len(intentos_fallidos) > 0:
        print("Historial de contraseñas incorrectas ingresadas:")
        for i, fallo in enumerate(intentos_fallidos):
            print("Intento #", i + 1, ":", fallo)
    else:
        print("No hubo fallos. ¡Qué buena memoria tienes!")


sistemaSeguridad()
