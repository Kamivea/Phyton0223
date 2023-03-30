###### EJERCICIO 1
print("EJERCICIO 1")
import pandas as pd

print(pd.__version__)
###Cargando datos csv
wine=pd.read_csv("./Clase05/input/winequality-white.csv",sep=";")#el archivo está separado por punto y coma (;)
print(wine.head()) #imprime las 5 primeras filas

###Cargando datos excel
cancer=pd.read_excel("./Clase05/input/Cancer.xlsx")
print(cancer.head())  #imprime las 5 primeras filas

###Cargando datos json
productos=pd.read_json("./Clase05/input/productos.json")
print(productos) #imprime todo

##### EJERCICIO 1.1
print("\n EJERCICIO 1.1")
print(productos.precio>=15) #imprimimos con false o true al filtrar el precio
print("\n--Dataframe_Productos filtrado por el precio--")
filtrado=productos[productos.precio>=15]# mostramos ya filtrado
print(filtrado)

