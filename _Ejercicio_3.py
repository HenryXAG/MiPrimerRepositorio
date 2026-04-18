nota = int(input("Ingrese su nota (0-10): "))


## aqui evaluamos de mayor a menor para mantener el orden lógico
if nota >= 9 and nota <= 10:
    print("Resultado:", "Excelente - ¡Eres nivel VIP!")
elif nota >= 7 and nota <= 8:
    print("Resultado:", "Bueno")
elif nota == 6:
    print("Resultado:", "Aprobado")
elif nota >= 0 and nota <= 5:
    print("Resultado:", "Reprobado - Debes estudiar más")
else:
    print("Resultado:", "Nota no válida, debe ser entre 0 y 10")
