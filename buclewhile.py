# si tenemos una variable y necesitamos comprobar

clima = "caliente"  # clima por defecto
# entrada = input("¿Cómo está eñ clima? ")
##print("El clima es: ", entrada)

# 3 para igualar un valor vamos a tomar ==
numeroComparar = False
numer2 = 50

## if es para tomar una desicion

if numeroComparar >= False:
    print("debes de trabajar para comprar un terreno para que tus nietos construyan ")
else:
    print("Debes cuidar tus rodillas")

## if sera nuestro camino ninja
## else es por defecto en caso de que el if no sea true

# and -> dos true
# or -> si tenemos un solo true

if numer2 > 24 and numer2 < 30:
    print("El numero es mayor a 24 y menor a 30")
elif numer2 > 30 and numer2 < 35:
    print("El numero es mayor a 30")
elif numer2 > 35:
    print("El numero es mayor a 35 cliente vip")
else:
    print("El numero es menor a 24")
# verifica un camino si este camino no esta deduce una opcion por defecto

## en un rango de numeros entre 10 y 100 vamos a verificar
# 18 mayor de edad
# 25 adulto joven
# 40 adulto
# 60 adulto mayor

edad = int(input("Ingrese su edad: "))

edadNumero = 0  ## convertimos la edad a un numero entero


def cambiarFormato(edadnumero):

    if edad.isdigit():
        edadNumero = int(edad)
        return True
    else:
        return False


if cambiarFormato(edadNumero):
    if edadNumero >= 18 and edadNumero < 25:
        print("Eres mayor de edad")
    if edadNumero >= 25 and edadNumero < 40:
        print("Eres un adulto joven")
    if edadNumero >= 40 and edadNumero < 80:
        print("Eres un adulto")
    if edadNumero >= 100:
        print("Marciano")
    else:
        print("no encontrado")
