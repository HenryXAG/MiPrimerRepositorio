Algoritmo bucle
	// bucle es algo que se repite asta que
	// una condicion logica la rompe 
	
	Definir contador Como Entero
	Escribir " numero del 0 al 100 "
	Leer numeroEntrada 
	contador = 0
	resultado = 0 
	anterior = 0
	sumar = 0
	
	Mientras contador <=  numeroEntrada // falso  // hull // unfined // none
		
		anterior = resultado
		contador = contador + 1
		resultado = contador + anterior  // 0, 1, 2,.....9,10
		
		Escribir  " resultado es ", contador , " + "  anterior, " = ", resultado
		
	FinMientras
	
	Escribir " password "
	leer pass 
	
	Mientras pass <> " nombre de ella + fecha especial " // ! =
		
		Escribir " romper bucle infinito 1 si 2 no "
		Leer respuesta
		si respuesta == "no"
			
		FinSi
		
		si respuesta == "si"
			
		FinSi
	FinMientras
	
	Escribir "final"
	// exponentes
	// radicales
	//  parentesis
	// di y mul 
	// suma y resta
	
	// contador i i++ i--  contador =+  contador  =  contador  +  contador
	
FinAlgoritmo
