#programa de seleccion simple  que consiste en controlar un acceso para mayores de edad
#Amayrani Dominguez Badillo 3F

print("verificacion de acceso") 

edad_usuario=int(input("Introducetu edad, por favor: "))

if edad_usuario<18:
    print("No puedes pasar")

else:
    print("Puedes pasar")
print("El programa ha finalizado")