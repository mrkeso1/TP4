# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import matplotlib.pyplot as plt
import pandas as pd #libreria pandas

datos = pd.read_csv('CSV/poblacion.csv')
datos = datos.sort_values('year',ascending=True) #acomoda datos por año


año = datos['year']
poblacion = datos['poblacion']


plt.plot(año, poblacion, c='green', label='Población anual')
plt.scatter(año, poblacion,c='red')

plt.legend() # imprime referencias
plt.show()# imprime grafico











