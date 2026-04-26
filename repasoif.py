## con una funcon vamos a pedi un numero  y vamos
## a validar si es un numero o una letra

# 1 sera pedir nuemro
# 2 validar numero
# retornarlo

## 1 pedir numero
numero = input("ingrese un numero")
## validar que sea un numero
validarNumero = (
    numero.isdigit()
)  # isdigit es una funcion que valida si el string es un numero
## retornar un numero
numeroEnformatoInt = int(
    numero
)  # int es una funcion que convierte un string a un numero entero


# string sumar 2 + las esperanzas de que el usuario ingrese un numero
print(numeroEnformatoInt + 2)
# parse es converir una variable de un tipo a otro

## inidcar si el numero es par o impar
## while es un bucle
## necesitan algo que los rompa

# Booleanos  F o V
## true, false

control = True
turnos = 0
try:
    while control:
        numbers = int(input("ingrese un numero"))
        if numbers % 2 == 0:
            print("el numero es par")
        elif numbers % 2 != 0:
            print("el numero es impar")
        turnos += 1
        if turnos == 5:
            control = False
except ValueError:
    print("ingrese un numero valido")

## refectorizar
## creacion de funciones


# pedir numero
def pedirNumero():
    numero = input("ingrese un numero")
    return numero


def ValidarNumero(numero):
    validarNumero = numero.isdigit()
    return validarNumero


def parOImpar(numero):
    if numero % 2 == 0:
        print("el numero es par")
    elif numero % 2 != 0:
        print("el numero es impar")


def bucliwhile(intentos):
    control = True
    contador = 0
    while control:
        seleccion = pedirNumero()
        validado = ValidarNumero(seleccion)
        parOImpar(validado)
        contador += 1
        if contador == intentos:
            control = False


bucliwhile(3)

# Horario de la semana con variable para el día

dia_semana = "Lunes"
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

horario = {
    "Lunes": ["8:00 - Matemáticas", "10:00 - Lengua", "13:00 - Deporte"],
    "Martes": ["8:00 - Ciencias", "10:00 - Historia"],
    "Miércoles": ["8:00 - Inglés", "10:00 - Arte"],
    "Jueves": ["8:00 - Música", "10:00 - Física"],
    "Viernes": ["8:00 - Computación", "10:00 - Educación Física"],
}

print(f"Horario para {dia_semana}:")
for clase in horario[dia_semana]:
    print("-", clase)

# Mostrar toda la semana
print("\nHorario completo de la semana:")
for dia in semana:
    print(f"{dia}:")
    for clase in horario[dia]:
        print("  -", clase)

        semana = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
            "Sabamingo",
        ]

## un array es lo que lo que forma al tener variables dentro de una variable

seleccion = int(input("ingrese un numero del 1 al 7"))
for i in range(len(semana)):
    if seleccion == i + 1:
        print(semana[i])
        print(semana[0])

print(semana[1])
print(semana[2])
print(semana[3])
print(semana[4])
print(semana[5])
print(semana[6])
print(semana[7])
