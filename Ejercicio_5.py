
def sumayresta(a,b):
    suma=a+b
    resta=b-a
    return suma,resta



#~CARGA DE VALORES
val1=2
val2=8

valor_suma,valor_resta=sumayresta(val1,val2)


print("La suna de "+str(val1)+" y "+str(val2)+" es:"+str(valor_suma))
print("La resta de "+str(val2)+" y "+str(val1)+" es:"+str(valor_resta))