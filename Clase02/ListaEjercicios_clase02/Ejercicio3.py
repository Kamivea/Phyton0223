##### EJERCICIO 3
print("EJERCICIO 3")

a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
while a==b:
    print("--Ingrese números diferentes--")
    a=int(input("Ingrese un número: "))
    b=int(input("Ingrese otro número: "))
def MayorValor(a,b):
    if a>b:
        return a
    else:
        return b
 
x=MayorValor(a,b)
print("El mayor valor es -> ",x)