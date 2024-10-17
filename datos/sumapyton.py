lista1 = [4,8,10,12,14,16,18]
lista2 = [3,5,6,7,9,11,13,15]
resultado = []
act=0
for i in range(len(lista1)):
    for j in range(len(lista2)):
        suma= lista1[i]+lista2[i]
    resultado.append(suma)
        
print(resultado)

