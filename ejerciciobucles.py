tamano = int (input ("ingrese el tamaño de la lista"))
lista = []
while tamano != 0:
    tamano -=1
    print (f'el valor al ingresar es: {tamano}')  
    valor=input()
    lista.append(valor)
print (lista)


