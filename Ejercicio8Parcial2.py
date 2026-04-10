poema_guia = """En el jardin de mi casa
las flores nacen con el sol
y el aroma llega al corazon"""

# esto sirve para contar cuántas veces aparece la letra a en todo el bloque
total_letras_a = poema_guia.count("a")

# 3. esto divide el bloque por sus saltos de línea para crear una lista
lista_oraciones = poema_guia.splitlines()

print("RESULTADO EJERCICIO 8")
print("Total de letras 'a' encontradas:", total_letras_a)
print("Lista de oraciones independientes:")
print(lista_oraciones)
