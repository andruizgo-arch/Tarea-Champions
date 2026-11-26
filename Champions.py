import numpy as np
import matplotlib.pyplot as plt
archivo = "equiposChampions.csv"

equipos = np.loadtxt(archivo, delimiter=",", skiprows=1,
                     usecols=0, dtype=str, encoding="utf-8")


datos = np.loadtxt(archivo, delimiter=",", skiprows=1,
                   usecols=(2, 3, 4, 5, 6), dtype=int, encoding="utf-8")

print("Cantidad de equipos:", len(equipos))
print("Tamaño del arreglo:", datos.shape)
print(equipos[:3])
print(datos[:3])

ganados = datos[:, 0]
empatados = datos[:, 1]
puntos = ganados * 3 + empatados * 1

print("Puntos por equipo:")
for i in range(len(equipos)):
    print(equipos[i], puntos[i])

goles_favor = datos[:, 3]
goles_contra = datos[:, 4]
diferencia = goles_favor - goles_contra

print("\nDiferencia de goles:")
for i in range(len(equipos)):
    print(equipos[i], diferencia[i])

tabla = np.column_stack((equipos, datos, puntos, diferencia))
orden = np.lexsort((-diferencia, -puntos))
tabla = tabla[orden]

encabezado = "equipo,ganados,empatados,perdidos,goles_favor,goles_contra,puntos,diferencia_goles"
np.savetxt("tabla posiciones.csv", tabla, delimiter=",", fmt="%s",
           header=encabezado, comments="", encoding="utf-8")

print("\nArchivo tabla posiciones.csv creado")

plt.figure(figsize=(12, 6))
barras = plt.bar(equipos[orden], puntos[orden], color="royalblue")
plt.bar_label(barras)

plt.title("Puntos por equipo en la Champions League")
plt.xlabel("Equipos")
plt.ylabel("Puntos")

plt.xticks(rotation=45, ha="right")
plt.yticks(range(0, puntos.max() + 2, 2))
plt.tight_layout()

plt.savefig("grafica puntos.png", dpi=150)
plt.show()