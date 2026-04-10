palabra_original = "CANTANDO"

# esto convierte toda la cadena a letras minúsculas
palabra_minus = palabra_original.lower()

# esto elimina el sufijo ando y encuentra el índice de la letra t
palabra_sin_sufijo = palabra_minus.removesuffix("ando")

# con .find() para buscar la posicion de la t
posicion_t = palabra_sin_sufijo.find("t")

print("RESULTADO EJERCICIO 4")
print("Palabra base:", palabra_minus)
print("Sin sufijo:", palabra_sin_sufijo)
print("La letra 't' está en el índice:", posicion_t)
