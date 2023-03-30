from E3_CapaModelo import *

def consulta(opcion:int):
    match opcion:
        case 1:
            crear_table()
            print("---Se creó la tabla---")
        case 2:
            try: 
                insertar_data()
                print("---Se insertó la data---")
            except Exception as E:
                print(E)
        case 3:
            mostrar_data()
        case _:
            print("---action por default---")
            