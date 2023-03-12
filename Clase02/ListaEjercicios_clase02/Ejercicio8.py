##### EJERCICIO 8
print("EJERCICIO 8")

primos_List=[]
for num in range(2,100000,123):#range(inicio,stop,step) 
    cont=0
    i=2
    while i<num and cont==0:
        x=num%i
        if x==0:
            cont+=1
        i+=1
    if cont==0:
       primos_List.append(num)
print(primos_List)
