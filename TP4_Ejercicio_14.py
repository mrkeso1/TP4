# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import numpy as np

valores = np.array([1, 2, 4, 7])

mask_a = valores > 1
mask_b = (valores % 2) == 0
a=valores[mask_a]
b=valores[mask_b]

print(a)
print(b)
























