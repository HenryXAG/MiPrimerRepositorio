Algoritmo CalificacionEstudiante
	
	Definir nota Como Real
	
	Escribir "Ingrese la nota del estudiante (0 a 10):"
	Leer nota
	
	Si nota >= 6 Entonces
		Escribir "Aprobado"
	SiNo
		Si nota <= 4 Entonces
			Escribir "Reprobado"
		SiNo
			Escribir "Recuperacion"
		FinSi
	FinSi
	
FinAlgoritmo