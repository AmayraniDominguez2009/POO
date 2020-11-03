#programa de la clase Mamifero
#Amayrani Dominguez Badillo 3F
class Electronicos:

    def __init__(self,tamaño,color=True,marca=True):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.prender()

    def prender(self):
        print(self.tamaño,": ha prendido")

    def apagar(self):
        print(self.tamaño,": ha apagado")

    def procesarinformacion(self):
        print(self.tamaño," ha procesadoinformacion")

telefono=Electronicos("telefono",True,True)
telefono.apagar()
telefono.procesarinformacion()
computadora =Electronicos ("computadora", True, False)
computadora.apagar()
computadora.procesarinformacion()