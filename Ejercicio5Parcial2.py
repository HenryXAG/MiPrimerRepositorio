lenguaje = "pYTHON"

lenguaje_invertido = lenguaje.swapcase()

# esto alinea a la izquierda en 15 caracteres rellenando con *
resultado_final = lenguaje_invertido.ljust(15, "*")

print("RESULTADO EJERCICIO 5")
print("Original:", lenguaje)
print("Invertido:", lenguaje_invertido)
print("Final (15 char):", resultado_final)
