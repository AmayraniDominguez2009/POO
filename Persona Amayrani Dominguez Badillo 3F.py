#programa de la clase Persona
#Amayrani Dominguez Badillo 3F

class Persona:

    def __init__(self,nombre,nacionalidad=True,genero=True):
        self.nacionalidad = nacionalidad
        self.genero = genero
        self.nombre = nombre
        self.escuchar()
        
    def escuchar(self):
        print (self.nombre,": ha escuchado")

    def caminar(self):
        print (self.nombre,": ha caminado")

    def jugar(self):
        print (self.nombre,": ha jugado")

Amayrani = Persona("Amayrani",True,True)
Amayrani.caminar()
Amayrani.jugar()
Julissa = Persona("Julissa",True, False)
Julissa.caminar()
Julissa.jugar()