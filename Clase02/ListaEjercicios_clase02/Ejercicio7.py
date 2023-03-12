##### EJERCICIO 7
print("EJERCICIO 7")

my_string1="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y 
archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el 
año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó 
una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. 
No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos 
electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la 
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más 
recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye 
versiones de Lorem Ipsum."""
#Encontrar palabra y contar las veces que aparecen
palabra=input("Ingrese la palabra que desea buscar:")
a=my_string1.find(palabra)
if a !=-1:
    print("Se encuentra en la posición: ",my_string1.find(palabra))
    print("Aparece",my_string1.count(palabra),"veces esa palabra")

else:
    print("Palabra no encontrada")
#Encontar palabra y detectar error directamente
print(my_string1.index("archivos"))
#Immprimir el texto sin los primeros 700 caracteres 
print(my_string1[700:])
#Separar con comas en forma de lista las 6 primeras palabras
print(my_string1.split(sep=" ", maxsplit=6))
#Convertir todo a mayúscula
print(my_string1.upper())
