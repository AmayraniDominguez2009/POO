#programa de seleccion simple que evalua si la contraseña es correcta
#Amayrani Dominguez Badillo 3F

key = "contraseña"
password = input("Introduce la contraseña : ")
if  key == password.lower():
    print("La cantraseña coincide")
else:
    print("La contraseña no coincide")