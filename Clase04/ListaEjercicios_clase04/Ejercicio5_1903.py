import re
numCelular=input("Ingrese su número de celular:")
validar=re.search(r"^9\d{8}$", numCelular) #Al agregar {8} implica que debe haber 8 caracteres númericos después del 9
if validar:
    print("Número válido")
else:
    print("¡Número inválido!")

