## quiero que si es lunes dormir hasta las 8
## si es martes dormir hasta las 7
## si es miercoles dormir hasta las 6
## si es jueves dormir hasta las 5
## si es viernes dormir hasta las 4
## si no tengo tareas hacer ejercicio.

dia = input("Seleicione el dia de la semana ")

# Las funciones
# las funciones son constantes de codigo
# la funciones que tiene la posibilidad de introducir parametros
# def nombre():
#    print("Hola mundo") esto es lo que  realizara la funcion


def selecionarDia(dia):
    if dia == "Lunes":
        print("Dormir hasta las 8")
    if dia == "Martes":
        print("Dormir hasta las 7")
    if dia == "Miercoles":
        print("Dormir hasta las 6")
    if dia == "Jueves":
        print("Dormir hasta las 5")
    if dia == "Viernes":
        print("Dormir hasta las 4")
    else:
        print("despertar a las 3 am")


## las funciones logicas son las que tiene solo 2 estados
# verdadero como el amor de mama  ( true)
# falso como el para siempre que se dedican.(false)

# if una sola evaluacion
# else que por defecto del if
# elif para evaluar multiples accione
