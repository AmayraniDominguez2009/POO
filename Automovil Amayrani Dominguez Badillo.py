#programa de la clase automovil
#Amayrani Dominguez Badillo 3F

class Automovil:

    def __init__(self,modelo,color=True,placa=True):
        self.color = color
        self.placa = placa
        self.modelo = modelo
        self.arrancar()

    def arrancar(self):
        print (self.modelo,": ha arrancado")

    def acelerar(self):
        print (self.modelo,": ha acelerado")

    def frenar(self):
        print (self.modelo,": ha frenado")

chevrolet = Automovil("chevrolet",True,True)
chevrolet.acelerar()
chevrolet.frenar()
toyota = Automovil("toyota",True, False)
toyota.acelerar()
toyota.frenar()
