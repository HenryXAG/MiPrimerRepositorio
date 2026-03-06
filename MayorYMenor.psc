Algoritmo MayorYMenor
	
	Definir num1, num2 Como Real
	
	Escribir "Ingrese el primer numero:"
	Leer num1
	
	Escribir "Ingrese el segundo numero:"
	Leer num2
	
	Si num1 > num2 Entonces
		Escribir "El mayor es: ", num1
		Escribir "El menor es: ", num2
	SiNo
		Si num2 > num1 Entonces
			Escribir "El mayor es: ", num2
			Escribir "El menor es: ", num1
		SiNo
			Escribir "Ambos numeros son iguales"
		FinSi
	FinSi
	
FinAlgoritmo