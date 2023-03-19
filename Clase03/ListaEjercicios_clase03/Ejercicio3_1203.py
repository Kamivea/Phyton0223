def Ej3(): 
    try:
        def dividir(a,b):
            try:
                c=a/b
                print("El resultado es :",c)
            except Exception as E:
                print(E)
        a=float(input("Ingrese un número: "))    
        b=float(input("Ingrese otro número: "))
        dividir(a,b)         
    except Exception as E:
                print(E)