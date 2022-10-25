# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393
import math
from matplotlib import pyplot

#funciones cuadráticas
def f1(x):
    return math.sqrt(x)
def f2(x):
    return -math.sqrt(x)

x = range(0, 100)


# Graficar funciones.

pyplot.plot(x, [f1(i) for i in x], c="green",label='RAIZ DE X')
#pyplot.plot(x, [f2(i) for i in x], c="green")

# Limitar los valores de los ejes.
pyplot.xlim(-1, 100)
pyplot.ylim(-10, 10)

# color ejes
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# mostrar
pyplot.legend() # imprime referencias
pyplot.title('Raiz de X')
pyplot.grid()
pyplot.show()
















