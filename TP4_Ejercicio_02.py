# Licenciatura en Ciencias de datos
# Programacion II
# Docente: Ing. Mario Martínez
# Alumno: Claudio Nicolas Kees - DNI: 32.328.393

stock = {}
stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0} #stock en 0
flag = True
while flag == True:
    print('\nMediante los numeros, ingrese el producto que quiera agregar \n')
    value = input('1.Tornillos; 2.Tuercas; 3.Arandelas; para finalizar ingrese FIN \n')
    if str(value.upper()) != "FIN":
        cantidad= int(input('Ingrese la cantidad de stock que quere agrega '))
        if value == '1':
            stock['tornillos'] = stock['tornillos'] + cantidad
        elif value == '2':
            stock['tuercas'] = stock['tuercas'] + cantidad
        elif value == '3':
            stock['arandelas'] = stock['arandelas'] + cantidad
        else:
            print('\n******Ingrese un valor correcto*******')
    else:
        flag = False
stock_2 = stock.items()
for i, x in stock_2:
    print(i, '-->',x)





