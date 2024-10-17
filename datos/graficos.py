import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

#plt.plot(x,y) lee los datos de x y y grafico de linea
plt.bar(x, y)
plt.xlabel('Eje X') #letrrero de eje x
plt.ylabel('Eje Y') #letrere del eje y
plt.title('Grafico simple de Matplot1') #titulo del grafico
plt.show() #imprime en consoa el grafico