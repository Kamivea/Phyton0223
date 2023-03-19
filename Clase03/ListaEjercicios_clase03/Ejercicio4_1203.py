def Ej4(): 
    class Producto:
        nombre=""
        codigo=""
        def __init__(self,nombre,codigo):
            self.listaProducto=[]
            self.nombre=nombre
            self.codigo=codigo
        
        def __str__(self)->str:
            return f"El nombre del producto es {self.nombre} y el código es {self.codigo}"
        
        def identificarPaisLote(self):
            cod=self.codigo.split(sep="-")
            print("País de origen:",cod[0],"y Lote:",cod[1])
    p1=Producto('Televisor','ARGENTINA-0043-2020') #Otro ejemplo: p2=Producto('Celular','BRASIL-0574-2021')

    print(p1)
    p1.identificarPaisLote()
