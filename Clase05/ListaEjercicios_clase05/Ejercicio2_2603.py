import pandas as pd
import sqlite3
##### EJERCICIO 2
print("\n EJERCICIO 2")

biblioteca=[
            ("Silvio en El Rosedal ","Julio Ramón Ribeyro","cuento"),
            ("Poema 20 ","Pablo Neruda","poema"),
            ("El túnel ","Ernesto Sábato","novela"),
           ]
df = pd.DataFrame(biblioteca)
print(df)
Conn1=sqlite3.connect("Clase05/ListaEjercicios_clase05/Ej2.db")
cursor1=Conn1.cursor()

cursor1.execute("CREATE TABLE IF NOT EXISTS Biblioteca (NameBook VARCHAR, Autor VARCHAR, Categoría VARCHAR)")

cursor1.executemany("INSERT INTO Biblioteca VALUES(?,?,?)",biblioteca)
Conn1.commit()
Conn1.close()