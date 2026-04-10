texto_ejercicio = "Su nombre"

texto_normalizado = texto_ejercicio.casefold()

## esto verifica si el texto que da son solo letras
## como su nombre tiene un espacio entonces .isalpha() dará False
es_alfabetico = texto_normalizado.isalpha()

print("RESULTADO EJERCICIO 6")
print("Texto normalizado:", texto_normalizado)
print("¿Es puramente alfabético?:", es_alfabetico)
