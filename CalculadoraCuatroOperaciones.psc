Algoritmo CalculadoraCuatroOperaciones
	Escribir "Ingrese el primer número:"
	Leer numero1
	Escribir "Ingrese el segundo número:"
	Leer numero2
	Escribir "Suma: ", numero1 + numero2
	Escribir "Resta: ", numero1 - numero2
	Escribir "Multiplicación: ", numero1 * numero2
	Si numero2 <> 0 Entonces
		Escribir "División: ", numero1 / numero2
	Sino
		Escribir "División: No es posible (divisor es 0)"
	FinSi
FinAlgoritmo