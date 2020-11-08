#Programa que dice si exentas de examen 
#Amayrani Dominguez Badillo 3°F

print("Exentar examen")

buenas_calificaciones = int(input("Introduce que calificacion tienes en total: "))
print(buenas_calificaciones)

tareas_entregadas = int(input("Introduce cuantas tareas entregaste en el parcial: "))
print(tareas_entregadas)

participaciones_clase = int(input("Introduce cuantas veces participaste en el parcial: "))
print(participaciones_clase)


if buenas_calificaciones>8 and tareas_entregadas>10 or participaciones_clase>5:

    print("Haz exentado examen")

else:

    print("No haz exentado examen")
