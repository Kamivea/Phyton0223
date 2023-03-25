import requests

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
response = requests.get(url)

data=response.json()

message="""
    1) Ver tipo de cambio
    2) Comprar dolares
    3) Vender dolares
    4) Cambiar soles a dolores
    5) Salir
"""
class CasaCambio:
    def __init__(self,venta,compra) -> None:
        self.venta=venta
        self.compra=compra
    def vender(self,monto):
        Totalventa=self.compra*monto #considero self.compra al vender pues el cambista debe ganar
        print("El ciente debe recibir: ",Totalventa,"soles")
    def comprar(self,monto):
        TotalCompra=self.venta*monto #considero self.venta al comprar pues el cambista debe ganar
        print("El ciente debe entregar",TotalCompra,"soles")
    def cambiar(self,monto):
        Totalcambio=monto/self.venta #se divide entre el valor más alto
        print("El ciente debe recibir",Totalcambio,"dolares")
    def __str__(self) -> str:
        return f"El precio de venta es {self.venta} y el precio de compra es {self.compra}"

while(True):
    print(message)
    opcion=int(input("Ingrese una opción: "))
    cc=CasaCambio(data['venta'],data['compra'])
    if opcion==1:
        print(f"Tasa de cambio en compra es {data['compra']} y en venta es {data['venta']}")
    if opcion==2:
        monto=float(input("Ingrese cuántos dolares quiere comprar: "))
        cc.comprar(monto)
    if opcion==3:
        monto=float(input("Ingrese cuántos dolares quiere vender: "))
        cc.vender(monto)
    if opcion==4:
        monto=float(input("Cuántos soles desea cambiar: "))
        cc.cambiar(monto)
    if opcion==5:
        print("Gracias, hasta luego")
        break