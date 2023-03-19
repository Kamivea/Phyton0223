def Ej5(): 
    try:
        from Ejercicio4_1203 import Ej4
    except Exception as E:
        print(E)
    else:
        import os
        print("La ruta del directorio",os.getcwd())
    finally:
        print("--Proceso terminado--")
 