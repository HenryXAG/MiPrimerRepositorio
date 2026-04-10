archivo_original = "ING. Sunombre.txt"

sin_extension = archivo_original.removesuffix(".txt")
sin_prefijo = sin_extension.removeprefix("ING. ")

# esto toma el texto que quede limpio, convertido a minúsculas
resultado_final = sin_prefijo.lower()

print("RESULTADO EJERCICIO 12")
print("Nombre de archivo base:", archivo_original)
print("Paso 1 (sin extensión):", sin_extension)
print("Paso 2 (sin prefijo):", sin_prefijo)
print("Resultado final (limpio):", resultado_final)
