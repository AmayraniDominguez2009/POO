#Clase Celular con constructor y encapsulamiento
#Amayrani Dominguez Badillo 3F

class Celular:                
    def __init__ (self):
        self.__tamaño=15 #valor encapsulado
        self.memoria=32 #GB
        self.camaras=2 
        self.prender=False #constructor   
    
    def jugar(self, prendido):     
        self.prender=prendido

        if self.prender:
            print("El celular comunica cuando esta prendido")
        else:
            print("El celular esta apagado")

    def comunicar(self): 
        print("El celular tiene: ", self.__tamaño, "de tamaño, una memoria de:", self.memoria, "GB y contiene: ", self.camaras, "camaras")

Samsung = Celular()     
print("Analizando el celular Samsung")
print(Samsung.jugar(True)) 
print(Samsung.comunicar())                       

print ("*  *  *  *  Segundo objeto  *  *  *  *")

Huawei = Celular()
print("Analizando el celular Huawei")
print(Samsung.jugar(False))
print(Samsung.comunicar())
