def Ej2():    
    class Producto_AP:
        name=""
        code=""
        marca=""
        precio=0.0
        def __init__(self,name,code,marca,precio):
            self.name=name
            self.code=code
            self.marca=marca
            self.precio=precio

        def __str__(self) -> str:
            return f'El producto {self.name} con código {self.code} de marca {self.marca}, cuesta {self.precio} soles'
    class Catálogo:
        ListaProdAutoPartes=[]
        def __init__(self):
            self.ListaProdAutoPartes=[]
        def agregarprod(self,producto):
            self.ListaProdAutoPartes.append(producto)
        def motrarlista(self):
            for i in self.ListaProdAutoPartes:
                print(i)

    ap1=Producto_AP("Filtro","4336","FILPOWER",200.0)
    ap2=Producto_AP("Bujía","4562","CHAMPION",150.0)

    list=Catálogo()
    list.agregarprod(ap1)
    list.agregarprod(ap2)
    print("---Lista de productos de autopartes ---")
    list.motrarlista()
