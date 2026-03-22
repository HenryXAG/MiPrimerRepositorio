def saludo(nombres):
    print(nombres)


nombre = input("Escribe tu nombre completo: ")


nombre_Mayusculas = nombre.upper()
saludo(nombre_Mayusculas)


nombre_minuscula = nombre.lower()
saludo(nombre_minuscula)


saludo(len(nombre))
