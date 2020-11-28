#Programa Orientado a Objetos
#Amayrani Dominguez Badillo 3F

class Celular:                
    tamaño=15         #centimetros
    memoria=32         #GB
    camaras=2              
    internet=False          
    
    def jugar(self):     
        self.internet=True  
        
    def comunicar(self):       
        if self.internet:     
           print("El celular comunica cuando tiene internet")
        else:
           print("El celular no comunica")
           

Samsung = Celular()     
print("El  Celular tiene un tamaño de: ", Samsung.tamaño, "centimetros") 
print("El Celular tiene una memoria de: ", Samsung.memoria, "GB") 
print("El Celular tiene:  ", Samsung.camaras, "camaras")   
Samsung.jugar()                      
print (Samsung.comunicar())   


print ("*  *  *  * A continuación creamos el segundo objeto  *  *  *  *")

Huawei = Celular()
print("El Celuular tiene un tamaño de: " , Huawei.tamaño -2, "centimetros")
print("El Celular tiene una memoria de : " , Huawei.memoria +32, "GB")
print("El Celular tiene: ", Huawei.camaras +1, "camaras")
Samsung.jugar()
print (Samsung.comunicar())