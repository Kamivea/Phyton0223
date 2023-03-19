def Ej6(): 
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