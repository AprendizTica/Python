lista1 = [4,8,10,12,14,16,18,5]
lista2 = [3,5,6,7,9,11,13,15,4]
resultado = []
for i in range (8): #cantidad de numeros
    vir1=lista1[i]
    vir2=lista2[i]
    res=vir1+vir2
    resultado.append(res)
print(resultado)