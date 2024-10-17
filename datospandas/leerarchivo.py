import pandas as pd

df = pd.read_csv("poblacion.csv")
#print(df[["Date","COL", "ARG"]])

#print(df.head()) Imprime las n primeras filas de la poblacion csv
#print(df.describle()) Descipcion de los datos de la poblacion csv
#print(df.tail()) Inprime las ultimas n filas de la poblacion csv
#print(df.sample()) Muestra una fila aleatoria de la poblacion

print(df.iloc[0])

filtro=df[df['COL']>30000000]#filtro de la poblacion de colombia mayor a 30000000
print(filtro["COL"]) #que nos muestra en consola solo la columna Col del filtro anterior
