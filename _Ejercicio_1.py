# Recordando que se usa int(input()) para convertir el texto a número
numero_usuario = int(input("Ingrese un número para evaluar: "))

# El camino ninja de las decisiones
if numero_usuario > 0:
    print("El número:", numero_usuario, "es POSITIVO")
elif numero_usuario < 0:
    print("El número:", numero_usuario, "es NEGATIVO")
else:
    print("El número es CERO")
