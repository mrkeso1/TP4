# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import matplotlib.pyplot as plt
import pandas as pd #libreria pandas

datos = pd.read_csv('CSV/poblacion.csv')
datos = datos.sort_values('year',ascending=True) #acomoda datos por año

options = [2000, 2005, 2010, 2015, 2020]

datos_filtrados = datos[(datos['year']).isin(options)]

print(datos_filtrados)

año = datos_filtrados['year']
poblacion = datos_filtrados['poblacion']

plt.xlabel('Año')
plt.ylabel('Población')
plt.bar(año, poblacion)
plt. title('Población Histórica Mundial')
plt.legend() # imprime referencias
plt.show()# imprime grafico











