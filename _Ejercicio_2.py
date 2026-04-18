## Solicitamos la edad al usuario
edad = int(input("Ingrese su edad: "))

## El camino para clasificar la edad
if edad < 18:
    print("Resultado: ", "Usted es menor de edad")
elif edad >= 18 and edad < 60:
    print("Resultado: ", "Usted es mayor de edad")
elif edad >= 60:
    print("Resultado: ", "Usted es un adulto mayor (Platino)")
else:
    print("Resultado: ", "Edad no válida")
