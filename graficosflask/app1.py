import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("enfermedades.csv")
x = df["Año"]
y = df["Enfermedades Respiratorias "]
z = df["Hipertensión "]
t = df["Obesidad "]
a = df["Diabetes "]
b = df["Enfermedades Cardiovasculares "]
c = df["Enfermedades Osteomusculares "]
d = df["Enfermedades Autoinmunes "]

plt.plot(x, y, color='blue', linestyle='--',marker='o')
plt.plot(x, z, color='yellow', linestyle='--',marker='o')
plt.plot(x, t, color='purple', linestyle='--',marker='o')
plt.plot(x, a, color='brown', linestyle='--',marker='o')
plt.plot(x, b, color='red', linestyle='--',marker='o')
plt.plot(x, c, color='green', linestyle='--',marker='o')
plt.plot(x, d, color='orange', linestyle='--',marker='o')
plt.legend(["Enfermedades Respiratorias","Hipertensión","Obesidad","Diabetes","Enfermedades Cardiovasculares","Enfermedades Osteomusculares","Enfermedades Autoinmunes"], loc="upper left")
plt.xlabel('AÑO')
plt.ylabel('CASOS')
plt.title('ENFERMEDADES FRECUENTES EN COLOMBIA') 
plt.show()