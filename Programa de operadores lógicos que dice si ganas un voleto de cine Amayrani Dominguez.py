#programa que decide si ganas un voleto de cine
#Amayeani Dominguez Badillo 3F

print("Premio de un boleto")

pelicula_Cenicienta = int(input("Introduce cuantas peliculas de la Cenicienta haz visto: "))
print(pelicula_Cenicienta)

pelicula_Sirenita = int(input("Introduce cuantas peliculas de la Sirenita haz visto: "))
print(pelicula_Sirenita)

pelicula_Frozen = int(input("Introduce cuantas peliculas de Frozen haz visto: "))
print(pelicula_Frozen)

if pelicula_Cenicienta==3 and pelicula_Sirenita==3 and pelicula_Frozen==2:

    print("Felicidades haz ganado el boleto")

else:

    print("Lo siento no haz ganado el boleto")
