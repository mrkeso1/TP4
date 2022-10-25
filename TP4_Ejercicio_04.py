# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

import csv
with open('CSV/propiedades.csv', mode ='r') as csvfile:
    dos_ambientes = 0
    tres_ambientes = 0
    datos = list(csv.DictReader(csvfile))
    columna = 'tipo_propiedad'
    ambiente = 'ambientes'
    for fila in range(len(datos)):
        if str(datos[fila][columna]) == 'Departamento':
            if str(datos[fila][ambiente]) == '2':
                dos_ambientes +=1
            elif str(datos[fila][ambiente]) == '3':
                tres_ambientes += 1
            else:
                continue

print('Los departamentos con dos ambientes son: ', dos_ambientes)
print('Los departamentos con dos ambientes son: ',tres_ambientes)










