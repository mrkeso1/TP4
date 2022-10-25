# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393
import math
from matplotlib import pyplot
y=0
#funciones cuadráticas
def f1(x):
    return pow(x,2)
def f2(x):
    return pow(x, 3)
x = [y/10 for y in range(-40, 41)]

print(x)

# Graficar funciones.

pyplot.plot(x, [f1(i) for i in x], c="blue",label='**2')
pyplot.plot(x, [f2(i) for i in x], c="orange",label='**3')


# Limitar los valores de los ejes.
pyplot.xlim(-6, 6)
pyplot.ylim(-70, 70)

# color ejes
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# mostrar
pyplot.legend() # imprime referencias
pyplot.title('Ejercicio_10')
pyplot.grid()
pyplot.show()
















