Algoritmo Sucesion_Fibonacci
	
	Definir NumeroFinal, NumeroAnterior, NumeroActual, Siguiente, contador Como Entero
	
	Escribir "¿Cuantos numeros de Fibonacci desea ver?"
	Leer NumeroFinal
	
	NumeroAnterior = 0
	NumeroActual = 1
	contador = 1
	
	Mientras contador <= NumeroFinal Hacer
		
		Escribir NumeroAnterior
		
		Siguiente = NumeroAnterior + NumeroActual
		NumeroAnterior = NumeroActual
		NumeroActual = Siguiente
		
		contador = contador + 1
		
	FinMientras
	
FinAlgoritmo