## aqui la entrada de datos (Números y Operación)
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")


if operacion == "+":
    resultado = num1 + num2
    print("Resultado de la suma:", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("Resultado de la resta:", resultado)
elif operacion == "*":
    resultado = num1 * num2
    print("Resultado de la multiplicación:", resultado)
elif operacion == "/":
    # Verificamos que no se divida por cero
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado de la división:", resultado)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida, por favor intente de nuevo")

## Cada elif evalúa un símbolo diferente
## y el else atrapa cualquier error de escritura
