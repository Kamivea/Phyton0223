import sqlite3
from datetime import datetime
try:
    conexion = sqlite3.connect("Clase04/ListaEjercicios_clase04/TextoEj4.txt")
    cursor = conexion.cursor()
    fichero=open("Clase04/ListaEjercicios_clase04/TextoEj4.txt","a")
    msg=input("Ingrese un mensaje: ")
    fecha0=datetime.now()
    fecha1=datetime.strftime(fecha0, ' %B %d %Y ')
    fichero.write(f"{fecha1} - TextoEj4.txt - {msg}")

except Exception as E:
    print(E)