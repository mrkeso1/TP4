# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import csv
suma = 0
archivo_csv =open('CSV/stock.csv', mode ='r')
datos = list(csv.DictReader(archivo_csv))
columna = "tornillos"
for fila in range(len(datos)):
    suma += int(datos[fila][columna])
print("\nLos tornillos son -->", suma)





