biblioteca={
"categorías":["novela","cuento","poema"],
"libros":{
    "00774":{
                "nombre":"Silvio en El Rosedal ",
                "autor":"Julio Ramón Ribeyro",
                "categoría":"cuento",
                "estado":"prestado",
            },
    "00668":  {   
                "nombre":"Poema 20 ",
                "autor":"Pablo Neruda",
                "categoría":"poema",
                "estado":"disponible"
            },
    "00992":{   
                "nombre":"El túnel ",
                "autor":"Ernesto Sábato",
                "categoría":"novela",
                "estado":"disponible"
            }
        },
"usuarios":[
            {
               "name":"Ariel",
               "libro prestado":"Silvio en El Rosedal"  
            },
            {
               "name":"Bruno",
               "libro prestado":""  
            }
           ]
        }


def ObtenerCategorias():
    print("Las categorías son: ",biblioteca["categorías"])
def ObtenerNombre_Autor():
    cod=input("Ingrese el código del libro: ")
    if cod in biblioteca["libros"].keys():
        nombreL=biblioteca["libros"][cod]["nombre"]
        autorL=biblioteca["libros"][cod]["autor"]
        print(f"""Datos del libro
        Nombre: {nombreL}, Autor: { autorL}""")
    else:
        print("_El código ingresado no existe_")
        ObtenerNombre_Autor()
def CambiarEstado():
    cod=input("Ingrese el código del libro que quiere cambiar su estado: ")
    if cod in biblioteca["libros"].keys():
        if biblioteca["libros"][cod]["estado"]=="disponible":
           biblioteca["libros"][cod]["estado"]= "prestado"
           print(biblioteca["libros"][cod])
        else:
            print("El libro seleccionado ya está prestado")
    else:
        print("_El código ingresado no existe_")
        CambiarEstado()

def ObtenerLista_Usuarios():
    lista=[]
    usuario1=biblioteca["usuarios"][0]["name"]
    usuario2=biblioteca["usuarios"][1]["name"]
    lista.append(usuario1)
    lista.append(usuario2)
    print("Los usuarios son: ", lista)


def intro():
    op=int(input("""Operaciones
1) Obtener la lista de categorías de libros.
2) Obtener nombres de los libros y autores.
3) Poder cambiar el estado de un libro a prestado
4) Lista de usuarios de la biblioteca.

Ingrese la operación que desea realizar: """))
    if   op==1:
        ObtenerCategorias()
    elif op==2:
        ObtenerNombre_Autor()
    elif op==3:
        CambiarEstado()
    elif op==4:
        ObtenerLista_Usuarios()
    else:
        print("__Número incorrecto__")
        intro()
print("---BIENVENIDO A LA BIBLIOTECA---")
intro()

