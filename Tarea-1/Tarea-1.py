"""Tarea 1"""

import csv
import numpy as np

ruta = "C:/Users/luisa/OneDrive/Escritorio/EDD_2025/Tarea-1/Presencia-Redes-Sociales.csv"

with open(ruta, mode="r", encoding="utf-8") as archivo:
    readerCsv = csv.reader(archivo)
    datosCsv = list(readerCsv)

datosTw = []
datosFb = []
datosYt = []

for row in datosCsv:
    if row[0] == "TWITTER" and "FOLLOWERS" in row[1]:
        datosTw.append(row[3:9])
    elif row[0] == "FACEBOOK" and "SEGUIDORES" in row[1]:
        datosFb.append(row[3:9])
    elif row[0] == "YOUTUBE" and "VISUALIZACIONES" in row[1]:
        datosYt.append(row[3:9])

datosTw = np.array(datosTw, dtype=int)
datosFb = np.array(datosFb, dtype=int)
datosYt = np.array(datosYt, dtype=int)

# Diferencia de seguidores en Twitter
difFollowTw = datosTw[0, -1] - datosTw[0, 0]
print("La diferencia de seguidores en Twitter entre enero y junio es:", difFollowTw)

# Diferencia de visualizaciones en Youtube
meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO"]

print("Elija un mes entre enero y junio")
mesI = input("Ingrese el mes de inicio: ").strip().upper()
mesF = input("Ingrese el mes de fin: ").strip().upper()

if mesI not in meses or mesF not in meses:
    print("Por favor elija un mes de los que se indicaron")
else:
    i1 = meses.index(mesI)
    i2 = meses.index(mesF)
    difVisuaYt = datosYt[0, i2] - datosYt[0, i1]
    print(f"La diferencia de visualizaciones en YouTube entre {
          mesI} y {mesF} es: {difVisuaYt}")

# Promedio de crecimiento Twitter y Facebook
promCreTw = np.mean(datosTw)
promCreFb = np.mean(datosFb)

print("El promedio de crecimiento de Twitter entre enero y junio:", promCreTw)
print("El promedio de crecimiento de Facebook entre enero y junio:", promCreFb)

# Promedio de me gusta en cada red social
datosLikeTw = np.array([row[3:9] for row in datosCsv if row[0]
                       == "TWITTER" and "ME GUSTA" in row[1]], dtype=int)
datosLikeFb = np.array([row[3:9] for row in datosCsv if row[0]
                       == "FACEBOOK" and "ME GUSTA" in row[1]], dtype=int)
datosLikeYt = np.array([row[3:9] for row in datosCsv if row[0]
                       == "YOUTUBE" and "ME GUSTA" in row[1]], dtype=int)

promLikeTw = np.mean(datosLikeTw)
promLikeFb = np.mean(datosLikeFb)
promLikeYt = np.mean(datosLikeYt)

print("El promedio de 'Me gusta' en Twitter entre enero y junio es: ", promLikeTw)
print("El promedio de 'Me gusta' en Facebook entre enero y junio es: ", promLikeFb)
print("El promedio de 'Me gusta' en YouTube entre enero y junio es: ", promLikeYt)
