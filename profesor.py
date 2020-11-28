#Programa Orientado a Objetos
#Amayrani Dominguez Badillo 3F

class Profesor:                #Clase Coche
    materias=4         #Atributos
    alumnos=150         #Atributos
    grupos=6                #Atributos
    enlinea=False          #Atributos
    
    def enseñar(self):     #Método enseñar
        self.enlinea=True  #llamar al atributo con nomenclatura del punto 
        
    def evaluar(self):       #Método evaluar
        if self.enlinea:     #llamar al atributo con nomenclatura del punto 
           print("El profesor evalua en línea")
        else:
           print("El profesor no evalúa en línea")
           

Profmate = Profesor()     #Instancia una clase
print("El profesor imparte: ", Profmate.materias, "materias diferentes") #Mostrar en pantalla
print("El profesor atiende: ", Profmate.alumnos, "alumnos") #Mostrar en pantalla
print("El profesor tiene:  ", Profmate.grupos, "grupos de diferentes carreras")   #Mostrar en pantalla
Profmate.enseñar()    #Activar el método mediante la nomenclatura del punto                  
print (Profmate.evaluar())   #Imprimir mediante la nomenclatura del punto


print ("*  *  *  * A continuación creamos el segundo objeto  *  *  *  *")

profsubm = Profesor()
print("El profesor imparte. " , profsubm.materias + 5, "materias diferentes")
print("El profesor atiende: " , profsubm.alumnos + 17, "alumnos")
print("El profesor tiene: ", profsubm.grupos -2, "grupos de diferentes carreras")
profsubm.enseñar()
print (profsubm. evaluar())
