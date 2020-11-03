#programa que verifica si es un correo electronico
#Amayrani Dominguez Badillo 3F

email=False
email = input("Introduce tu correo electronico:")
for i in (email):
  if (i=="@"):
        email=True
if email==True:
    print("email es correcto")
else:
    print("email no es correcto")