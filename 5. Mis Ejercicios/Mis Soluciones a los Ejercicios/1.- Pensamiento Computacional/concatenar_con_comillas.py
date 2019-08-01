'''
EJERCICIO 3:
'''
cita = input('Introduce una cita famosa: ')
autor = input('Quien enuncio esa cita?: ')

print('"{}", {}'.format(cita.title(), autor.capitalize()))

'''
RESTRICCION:
'''
# Es posible COMBINAR las COMILLAS SIMPLES (') y las DOBLES (") para evitar tener que ESCAPARLAS
print('"' + cita.title() + '", ' + autor.title())

# Utilizando SOLO COMILLAS SIMPLES (') y el CARACTER ESCAPE (\)
print('\'' + cita.capitalize() + '\', ' + autor.capitalize())