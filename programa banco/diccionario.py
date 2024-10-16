
cliente = {
    "nombre": "jorge",
    "apellido": "Rodriguez",
    "telefono": "3236315530",
    "saldo": "50000",
    "edad": "40"
    }

print(cliente)
valor = cliente["nombre"]
print(valor)
cliente["profesion"] = "ingeniero"
print(cliente)
print(cliente["telefono"])
del cliente["telefono"]

print(cliente) #para ver las claves de los elementos anteriores>nombre, apellido, saldo, edad, profesion,con del se quito el telefono#
claves = cliente.keys()
print(claves)

print(cliente) 
print(cliente.keys())#otra forma para ver las claves o sea nombre, apellido
print(cliente.values()) #ver jorge, rodriguez

cajero = { #es otra carpeta donde nombre Jorge lo cambio por Juan y apellido rodriguez por ramirez
    "nombre":"juan",
    "apellido":"ramirez"
}
print(cajero)  #se ve los datos de la nueva carpeta 
print(cliente) #se ve los datos anteriores jorge, rodriguez,,,,
cliente.update(cajero) #cambiar jorge a juan y rodriguez por ramirez
print(cliente) # se ve con los nevos datos

      
      








