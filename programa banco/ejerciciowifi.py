redes =[] #define lista vacia


while True: #genera un ciclo infinito
    print("opcion 1 agregar red") #imprime en pantalla
    print("opcion 2 ver redes") #imprime en pantalla
    print("opcion 0 para salir") #imprime en pantalla
    opcion = int(input ("ingrese una opcion")) #imprime en pantalla

    if opcion == 1: #compara la opcion con el  valor entero 1 y ejecuta blooque de codigo
        red = {} #define dicccionario vacio
        print("ingrese la red") #imprime en pantalla
        nombre = input() #ingresa datos del teclado a la variable
        red ["nombre"] = nombre #guarda el dato del input en el diccionario clave nombre
        print("ingrese la contraseña") #imprime en pantalla
        clave=input() #ingrese datos del teclado a la variable
        red["clave"] = clave #guarda el dato del input en el diccionario clave
        redes.append(red) #agrega diccionario a la lista 

    elif opcion == 2: #compara la opcion con el valor entero 1 y ejecuta bloque de codito
        for i in rango (len(redes)): #repite el bloque segun el tamaño de la lista redes (metodo)
            print(redes[i]) #imprime en pantalla 
