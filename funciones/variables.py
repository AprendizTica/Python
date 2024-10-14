#cantidad = int (input ("ingrese la cantidad de los productos"))
#valor = int(input ("ingrese el precio"))
 #  print cantidad
  #  print ()
   
#def calcular (x,y)
#    returm x*y

#resultado=calcular (cantidad, valor)
#print (resultado)

def calcular(x,y):
   return x * y
def multiplicar(x,y):
   return x * y

total = 0
cantidad =1

while cantidad !=0:
    print("ingrese cantidad producto")
    cantidad =float(input())
    if cantidad==0:
        break
    print("ingrese valor de producto")
    valor = float(input())
    subtotal = calcular(cantidad, valor)
    Subtotal=multiplicar(subtotal,1.19)
    total+=Subtotal 

print(f"el total de los productos es {total}")
