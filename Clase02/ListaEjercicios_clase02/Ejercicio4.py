##### EJERCICIO 4
print("EJERCICIO 4")

import sys
variable=sys.argv

def func_argumento(*args):
    for i in args:
        print(i)

func_argumento({"Colores":{"blue":"azul","yellow":"amarillo"}},22,"Mi planta de naranja lima",[7,"luck",True])