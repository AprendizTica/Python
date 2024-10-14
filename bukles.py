tamano = input ("ingrese el tamaño de la lista")
lista = []
for i in range(int(tamano)):
    print (f'el valor al ingresar es: {i}')  
    valor=input()
    lista.append(valor)
print (lista)