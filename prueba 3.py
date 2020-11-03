#prueba Programa que dice si un alumno reprueba o aprueba
#Amayrani Dominguez Badillo
print("programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno:")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion


print(evaluacion(int(nota_alumno)))