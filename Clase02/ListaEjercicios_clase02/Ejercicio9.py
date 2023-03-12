##### EJERCICIO 9
print("EJERCICIO 9")

### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':"m",
            'password':"",
            'rol':"inventario" ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"",
        "ubicacion":""
    }],
    "productos":[
    {
        "nombre":"n",
        "precio":"",
        "stock":0
    }]
}
##### funciones
#####
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede")
        ubicacion=input("ingrese ubicacion")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")
def agregarProductos():
    rol=obtenerRol(usuario)
    if rol=='inventario':
        NameProduct=input("Ingrese el nombre de producto: ")
        Precio=float(input("Ingrese el precio: "))
        Stock=int(input("Ingrese el stock: "))
        dictProd={
                    "nombre":NameProduct,
                    "precio":Precio,
                    "stock":Stock
                 }
        sistema["productos"].append(dictProd)
#####
def cambiarStock():
    rol=obtenerRol(usuario)
    if rol=='inventario':
        producto=input("Ingrese el nombre del producto: ")
        stock=int(input("Ingrese el nuevo stock: "))
        for i,valor in enumerate(sistema["productos"]):
            if valor["nombre"]==producto :
                valor['stock']=stock
        



usuario=input("Ingrese su usuario: ") #Solicito el usuario de manera general para no incluirlo dentro de cada función
agregarProductos()
cambiarStock()
print(sistema)


