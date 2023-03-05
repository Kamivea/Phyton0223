##### EJERCICIO 9
print("EJERCICIO 9")
lista=[]
#lista y a la vez tuplas de 4 elementos
#contiene [( ‘nombre’ ,’edad’, ‘dni’), día,mes,año de nacimiento]
lista1=[("Ana",8,48781355),("Pedro",16,52392546),18,10,2006]   #contiene [( ‘nombre’ ,’edad’, ‘dni’), día,mes,año de nacimiento]
lista3=[("Luis",7,82547589),20,9,2015]
lista4=[("Mia",19,69875074),25,11,2004]
dnis=[69875074,82547589,52392546,47856215,48781355]
if lista1[0][1]>=18 :                         #primero especifico posición general y luego dentro la tupla
    if lista1[0][2]in dnis:                   #uso in para verificar si se encuentra ese dato
        print("Es mayor de edad y se tiene su DNI: ", lista1[0][0])
        lista=lista1
if lista2[0][1]>=18 :
    if lista2[0][2]in dnis:
        print("Es mayor de edad y se tiene su DNI: ", lista2[0][0])
        lista=lista2
if lista3[0][1]>=18 :
    if lista3[0][2]in dnis:
        print("Es mayor de edad y se tiene su DNI: ", lista3[0][0])
        lista=lista3
if lista4[0][1]>=18 :
    if lista4[0][2]in dnis:
        print("Es mayor de edad y se tiene su DNI: ", lista4[0][0])
        lista=lista4
print("El elemento que cumplió todas las condiciones: ", lista)
print(" ")