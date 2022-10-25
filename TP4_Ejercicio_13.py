# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import numpy as np
lista = list(range(10))
valores = np.asarray(lista)
a = np.where(valores>3,valores,0)
b = np.where(valores%2==0,valores,0)

print(a)
print(b)




















