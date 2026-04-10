numero_texto = "42"

# rellenalo con ceros a la izquierda hasta alcanzar longitud de 5
numero_relleno = numero_texto.zfill(5)

# esto verifica con un booleano si termina con 2
termina_en_dos = numero_relleno.endswith("2")

print("RESULTADO EJERCICIO 7")
print("Texto original:", numero_texto)
print("Texto con zfill(5):", numero_relleno)
print("¿Termina con el número '2'?:", termina_en_dos)
