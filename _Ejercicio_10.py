usuario_maestro = "admin"
clave_maestra = "Ever123"

# aqui pedimos los datos al usuario
print("-LOGIN DE SISTEMA -")
usuario_ingresado = input("Ingrese su usuario: ")
clave_ingresada = input("Ingrese su contraseña: ")


# aqui casefold() por si el usuario escribe en mayúsculas por error
if usuario_ingresado.casefold() == usuario_maestro and clave_ingresada == clave_maestra:
    print("Resultado:", "Acceso permitido. Bienvenido al sistema.")
else:
    # si alguno de los dos falla, el and devuelve False
    print("Resultado:", "Acceso denegado. Usuario o clave incorrectos.")

## en la clave no usé casefold porque las contraseñas
## suelen ser sensibles a mayúsculas y minúsculas.
