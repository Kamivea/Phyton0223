import sqlite3

con=sqlite3.connect("Clase05/ListaEjercicios_clase05/Ejercicio3_2603/Ej3.db")

cursor=con.cursor()

def crear_table():                    # PRIMARY KEY means unique value, INTEGER means int, VARCHAR means str and 100 quantify
    cursor.execute("CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(100),edad INTEGER)")
    con.commit()

def insertar_data():
    n=int(input("Ingrese la cantidad de usuarios que desea ingresar: "))
    for i in range(n):
        name=input("\nIngrese el nombre del usuario: ")
        edad=int(input("Ingre la edad del usuario: "))
        cursor.execute("INSERT INTO usuario VALUES(NULL,?,?)",(name,edad))
        con.commit()

def mostrar_data():
    data=cursor.execute("SELECT * FROM usuario").fetchall()
    print(data)


