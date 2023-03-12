dni_mayores=[4567,8448,5422,5484,8974,3152,6589]
organizadores={"lia":[8448,4586],
               "marta":[2145,5422], 
               "angel":[6872]
              }

def verificar_edad(dni):
    if dni in dni_mayores:
        print("Mayor de edad -> Usario permitido")
        return 1
    else:
        print("Menor de edad -> Usario no permitido")
        return 0
def validar_invitación(dni):
    if dni in organizadores["angel"] or dni in organizadores["lia"] or dni in organizadores["marta"]:
        print("Persona invitada")
        return 1
    else:
        return 0
def asignar_zona(dni):
    if dni in organizadores["angel"]:
        zona="B"
    elif dni in organizadores["lia"]:
        zona="C"
    else:
        zona="A"
    print("Zona asignada: ", zona)

def main():
    dni=int(input("Ingrese su número de DNI: "))
    
    if validar_invitación(dni)==1:
        if verificar_edad(dni)==1:
            asignar_zona(dni)
 
main()