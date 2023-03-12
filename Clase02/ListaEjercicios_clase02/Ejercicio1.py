###### EJERCICIO 1
print("EJERCICIO 1")

def preg():
    item=int(input("""Ingresar el número de lo que desea realizar:
    1. Dibujar un cuadrado
    2. Identificar múltiplos de 2
    3. Seleccionar mayores de edad
        ->   """) )   
    if item==1:
        x=int(input("Ingrese el número de filas para el cuadrado: "))
        for n in range(x):
            print("*    " * x)
            print(" ")

    elif item==2:
        numbers=[1,201,8,953,4,54841,16,628240,4882,45,4896,11]
        for i in numbers:
            if i%2==0: #Condición múltiplo de 2
                print(i)
    elif item==3:
        nameAge=[["luis",20],["ana",16],["marta",7],["arturo",18]]
        for name,age in nameAge:
            if age>=18:  #Filtramos a los mayores de edad
                print(f"{name}->{age}")
    else:
        print(" Número inválido ")
        preg()
preg()

