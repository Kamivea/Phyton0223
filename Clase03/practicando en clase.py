"""n=int(input("Introduce un número: "))
m=7
print({}/{}=)
#Bloque
try:
    n=int(input("Introduce un número: "))
    m=7
    print({}/{}=)"""

"""listaGloblas=[]
listaGlobalv2=[1,2,32,4,45,42]
def retirarElementos(listaParametro:list):
    try:
        listaParametro.pop()
        print(listaParametro)
    except:
        print("vacía")
retirarElementos(listaGloblas)
retirarElementos(listaGlobalv2)"""
"""
listaGlobal1=[1,25,5445,12,25,69,885]
def IndexOfList(lista:list):
    try:
        print(lista[12])
    except:
        print("esta fuera de rango")

IndexOfList(listaGlobal1)
##mejoramos erroeres


listaGlobal12=[1,25,5445,12,25,69,885]
listaempty=[]
def IndexOfListv2(lista:list):
    try:
        print(lista[12])
    except Exception as E:
        print(E)

IndexOfList(listaGlobal1)
##mejoramos erroeres"""

class Costumer:
    def _init_(self,edad,numCompras):
        self.edad=edad
        self.numCompras=numCompras
    pass
luis=Costumer
ana=Costumer




class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"El producto {self.nombre} con id {self.id}  de {self.precio} soles, cuenta con {self.stock} und en stock"
    def updateStock(self,stock):
        self.stock=stock
    def updateID(self,id):
        self.id = id
    
class CarritoCompra: 
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProduct(self,id):
        for index in self.listaProductos:
            if index.id==id:
                self.listaProductos.remove(index)
                print("--Producto eliminado--")
                for a in self.listaProductos:
                    if a.id>id:
                        a.updateID(a.id-1) 
            else:
                print("--No existe producto con ese id--")

    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
        print(f"Precio total: {self.precioTotal}")
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print("Hay ",len(self.listaProductos)," productos en el carrito")
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar producto
    4)Mostrar el precio total
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del producto:")
            stock=int(input("ingrese el stock del producto:"))
            release=int(input("ingrese el release del producto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print(Error)
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        if len(carrito.listaProductos)>0:
            id_=int(input("Ingrese el id del producto que quiere quitar: "))
            carrito.quitarProduct(id_)
        else:
            print("No hay productos en el carrito para quitar")
    if opcion==4:
        carrito.calcularPrecio()
        
    if opcion==5:
        break







###Otra forma
class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"El producto {self.nombre} con id {self.id}  de {self.precio} soles, cuenta con {self.stock} und en stock"
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra: 
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProduct(self,product,id):
        self.listaProductos.remove(product)
   
    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
        print(f"Precio total: {self.precioTotal}")
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print("Hay ",len(self.listaProductos)," productos en el carrito")
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar producto
    4)Motrar el precio total
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del prodcuto:")
            stock=int(input("ingrese el stock del prodcuto:"))
            release=int(input("ingrese el release del prodcuto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print(Error)
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        if len(carrito.listaProductos)>0:
            try:
                id_=int(input("Ingrese el id del producto que quiere quitar: "))
                for index in carrito.listaProductos:
                    if index.id==id_:
                        carrito.quitarProduct(index,index.id)
                    else:
                        print("No exite producto con ese id")
            except Exception as Error:
                    print(Error)
        else:
            print("No hay productos en el carrito para quitar")
    if opcion==4:
        carrito.calcularPrecio()
        
    if opcion==5:
        break
