#prueba programa que dice si una alumno esta aprobado o reprobado
#amayrani Dominguez Badillo
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion


print( evaluacion(8))