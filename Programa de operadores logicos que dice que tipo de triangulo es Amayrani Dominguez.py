#Programa que te dice que tipo de triangulo es 
#Amayrani Dominguez Badillo 3°F

lado_1 = float(input("Introduce el valor numerico del lado 1: "))
lado_2 = float(input("Introduce el valor numerico del lado 2: "))
lado_3 = float(input("Introduce el valor numerico del lado 3: "))

if(lado_1==lado_2 and lado_1==lado_3 or lado_2==lado_3):
    print("El teiangulo es Equilatero")

elif(lado_1==lado_2 or lado_1==lado_3 or lado_2==lado_3):
    print("El triangulo es Isoceles")

else:
    print("El triangulo es Escaleno")
    