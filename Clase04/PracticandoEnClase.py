class  Persona:
    def __init__(self,fullname,tipoDocumento,nroDocumento):
        self.fullname=fullname
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocumento
    def __str__(self):
        return f"Lapersona {self.fullname} con {self.tipoDocumento} y nro {self.nroDocumento}"
    
class Cliente(Persona):
    def __init__(self,fullname,tipoDocumento,nroDocumento):
        super().__init(fullname,tipoDocumento,nroDocumento)
class Asesor(Persona):
    def __init__(self,fullname,tipoDocumento,nroDocumento):
        super().__init(fullname,tipoDocumento,nroDocumento)

p1=Persona("karen","dni","456168")

a2=Cliente(p1)

print(a2)