#prueba Programa que dice si un alumno reprueba o aprueba
#Amayrani Dominguez Badillo 3F
print("programa de evaluacion de calificacion de alumnos")

calificacion_alumno=input("Introduce la calificacion del alumno:")

def evaluacion(calificacion):
    valoracion="aprobado"
    if calificacion<5:
        valoracion="reprobado"
    return valoracion


print(evaluacion(int(calificacion_alumno)))