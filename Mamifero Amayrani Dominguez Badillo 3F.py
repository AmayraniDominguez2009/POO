#programa de la clase Mamifero
#Amayrani Dominguez Badillo 3F
class Mamifero:

    def __init__(self,tipo,cola=True,garras=True):
        self.cola = cola
        self.garras = garras
        self.tipo = tipo
        self.nacer()

    def nacer(self):
        print (self.tipo,": ha nacido")

    def comer(self):
        print (self.tipo,": ha comido")

    def rugir(self):
        print (self.tipo," ha rugido")

perro=Mamifero("perro",True,True)
perro.comer()
ballena =Mamifero ("ballena", True, False)
ballena.comer()

