animal = "  elefante  "

# con esto liminamos los espacios de los extremos
animal_limpio = animal.strip()

# con esto ontamos las repeticiones de la letra "e"
repeticiones = animal_limpio.count("e")

# aqui mostramos resultados
print("Palabra original:", animal)
print("Palabra limpia:", animal_limpio)
print("La letra 'e' se repite:", repeticiones, "veces")
