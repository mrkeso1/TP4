# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import matplotlib.pyplot as plt
mes = [3, 4, 5, 6]
gasto_carne = [1650, 2600, 3100, 4000]
gasto_verdura = [2500, 2200, 1800, 600]
# carne
plt.plot(mes, gasto_carne, 'c', label='Carnes')

# verdura
plt.plot(mes, gasto_verdura, 'y', label='Verduras')

plt.legend() # imprime referencias
plt.show()# imprime grafico











