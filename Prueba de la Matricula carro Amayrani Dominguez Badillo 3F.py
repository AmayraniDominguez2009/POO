#programa de seleccion simple que dice si la matricula del carro es verdadera
#Amayrani Dominguez Badillo 3F

key = "matricicula carro"
password = input("Introduce tu matricula carro : ")
if  key == password.lower():
    print("La matricula carro coincide")
else:
    print("La matricula carro no coincide")