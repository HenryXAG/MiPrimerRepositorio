cadena_ejercicio = "Python2026"

# esto verifica si el texto es alfanumérico
es_alfanumerico = cadena_ejercicio.isalnum()

## si lo es convierte a minúsculas y separa la palabra de los números
## reemplazando 2026 por una cadena vacía
if es_alfanumerico:
    texto_minusculas = cadena_ejercicio.lower()
    resultado_limpio = texto_minusculas.replace("2026", "")

print("RESULTADO EJERCICIO 10")
print("¿Es '", cadena_ejercicio, "' alfanumérico?:", es_alfanumerico)
print("Texto procesado final:", resultado_limpio)
