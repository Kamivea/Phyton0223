###### EJERCICIO 1
print("EJERCICIO 1")
name=input("Nombre completo: ") # Karen Mishell Vera Arapa
edad= input("Edad:")
print("Tu nómbre es: ",name," y tu edad es: ",edad)
print(" ")

##### EJERCICIO 2 
print("EJERCICIO 2")
# Area of a circle
print(" Circle")
r=float(input("Radius of the circle: "))
pi=3.1416
AreaC=pi*r**2
print("Area of a circle is: ", AreaC)
# Area of a triangle
print(" Triangle")
b= float(input("Base of the triangle is: "))
h= float(input("Height of the triangle is: "))
AreaT=b*h/2
print("Area of a triangle is: ", AreaT)
# Area of a square
print(" Square")
s=float(input("Side of the square: "))
AreaS=s**2
print("Area of a square is: ", AreaS)
print(" ")

##### EJERCICIO 3
print("EJERCICIO 3")
k=float(input("k = "))
l=float(input("l = "))
m=float(input("m = "))
print("Suma:           k+l+m = ", k+l+m)   #suma
print("Resta:            k-m = ",k-m)        #resta
print("Multiplicación: k*l*m = ",k*l*m)    #multiplicación
print("División:         l/m = ",l/m)        #división
print("División entera: l//m = ",l//m)        #división
print(" ")

##### EJERCICIO 4
print("EJERCICIO 4")
dato=input("Ingrese un dato: ") #input guarda el dato como tipo cadena, str. Se debe añadir int, float, etc al inicio para cambiarlo
print("El tipo de dato es: ",type(dato))
print(" ")

##### EJERCICIO 5
print("EJERCICIO 5")
import sys
variable =sys.argv[0]
print(variable)
print(" ")

##### EJERCICIO 6
print("EJERCICIO 6")
x=int(input("El último término de la suma es: "))
sum=x*(x+1)/2
print("La suma de la serie aritmética es: ",sum)
print(" ")

##### EJERCICIO 7
print("EJERCICIO 7")
n1=int(input("n1= ")) #ingreso variable tipo entero
n2=int(input("n2= "))
if n1==n2:
    print("Los números son iguales")
else:
    print("Los números son diferentes")
    if n1>n2:
        print("n1={} es mayor que n2={}".format(n1,n2))
    else:
        print("n2={} es mayor que n1={}".format(n2,n1))
print(" ")

##### EJERCICIO 8
print("EJERCICIO 8")
contraseña= 'camino'
password=input("Ingrese la contraseña: ")
# verificamos si la contraseña es igual sin importar mayúsculas, minúculas o combinado
if password==contraseña or password==contraseña.title() or password==contraseña.upper() or password==contraseña.lower(): #uso métodos 
    print("Contraseña corecta")
else:
    print("Contraseña incorrecta")
print(" ")

##### EJERCICIO 9
print("EJERCICIO 9")
lista=[]
lista1=[("Ana",8,48781355),12,12,2014]      #lista y a la vez tuplas de 4 elementos
lista2=[("Pedro",16,52392546),18,10,2006]   #contiene [( ‘nombre’ ,’edad’, ‘dni’), día,mes,año de nacimiento]
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

##### EJERCICIO 10
print("EJERCICIO 10")      #Un diccionario
lista=[]    # daclaramos esta variable para luego facilitar ingresar valores y juntarlos en una lista
Escuela={"curso":"",     #todos empiezan con valor de inicialización
         "CantAlumnos":0,
        "Activo":True,
        "Profesor":"",
        "MaxNota":0,
        "Alumnos": lista}
Escuela["curso"]=input("Ingrese el curso: ")   #Se le da el valor  a lo que está dentro de corchetes
Escuela["CantAlumnos"]=int(input("Ingrese la cantidad de alumnos: "))
Escuela["Activo"]=bool(input("Ingrese true si está activo y false si no: "))
Escuela["Profesor"]=input("Ingrese el nombre del profesor: ")
Escuela["MaxNota"]=int(input("Ingrese la máxima nota: "))

name1=input("Ingrese el nombre de un alumno: ") #Ingresamos los nombres 1 a 1 para luego formar una lista
lista.append(name1)
preg=int(input("   Escriba 1 si desea añadir más alumnos y 0 si no : ")) 
while preg==1:              #En realidad para cualquier valor dif de 1 no cumple la condición
    name1=input("Ingrese el nombre de otro alumno: ")
    lista.append(name1)
    preg=int(input("   Escriba 1 si desea añadir más alumnos y 0 si no : "))
Escuela["Alumnos"]=lista

print(Escuela)
