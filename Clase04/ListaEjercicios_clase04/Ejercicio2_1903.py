import random
class Sorteo:
    
    def __init__(self):
        self.cantidadValores=0
        self.listaValores=[] 
    def ingresarValores(self,cantidadValores):
        for i in range(1,cantidadValores+1):
            elementos=input(f"Dato {i} a sortear: ")
            self.listaValores.append(elementos)   
    def mostrarLista(self):
        if len(self.listaValores)>0:
            for i in self.listaValores:
                print(i)
        else:
            print("---Lista vacía---")
    def sortear(self):
        if len(self.listaValores)>0:
            print("Elegido: ",random.choice(self.listaValores))
        else:
            print("---No hay datos para sortear---")

message="""
    1) Ingresar valores para sortear
    2) Mostrar valores
    3) Sortear aleatoriamente
    4) Salir
    """
sorteoo=Sorteo()
while True:
    print(message)
    op=int(input("Ingrese la opción que desea realizar: "))
    if op==1:
        try:
            n=int(input("Ingrese la cantidad valores a sortear: "))
            sorteoo.ingresarValores(n)
        except Exception as E:
                print("!!!Sucedió un error: ",E)
        else:
            print("--Agregando valores--")
    if op==2:
        sorteoo.mostrarLista()
    if op==3:
        sorteoo.sortear()
    if op==4:
        break

        
        
    
    