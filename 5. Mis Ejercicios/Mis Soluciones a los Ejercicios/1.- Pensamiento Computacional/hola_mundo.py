'''
Segun ENUNCIADO
'''
print('EJERCICIO 1:')
nombre = input('Cual es tu nombre?: ')
saludo = 'Hola ' + nombre + ', como estas?'
print(saludo)

'''
RETO 1: Se INVOCA DIRECTAMENTE a la FUNCION "input()".
'''
print('EJERCICIO 1: RETO 1')
# Utilizando el METODO "format()" para FORMATEAR CADENAS de TEXTO.
print('Hola {}, como estas?'.format(input('Cual es tu nombre?:')))

# Utilizando el OPERADOR "+" para CONCATENAR CADENAS
print('Hola ' + input('Cual es tu nombre?:') + ', como estas?')

'''
RETO 2: Utilizando CONDICIONALES if-elif ENCADENADOS o tambien UTILIZANDO NUMEROS ALEATORIOS.
'''
print('EJERCICIO 1: RETO 2')
# SENTENCIAS IF-ELIF:
nombre = input('Cual es tu nombre?: ')

if nombre == 'Javier':
    print('Hola ' + nombre + ', como estas?')
elif nombre == 'Alex':
    print('Hey ' + nombre + ', como lo llevas?')
elif nombre == 'Luis':
    print('How are you, ' + nombre + '?')
else:
    print('Hola ' + nombre)

# MODULO "ramdom" y LISTA de NOMBRES:
# Se IMPORTA el MODULO "ramdom" para poder GENERAR NUMEROS ALEATORIOS.
import random

# LISTA con posibles saludos.
lista_saludos = ['Hola', '¿Que tal?', '¿Como estas?', '¿Que pasa?']

nombre = input('¿Cual es tu nombre ?:')

# Se GENERA un NUMERO ALEATORIO para seleccionar un saludo de la LISTA.
'''
La FUNCION "randint()" del MODULO "random" GENERA un NUMERO ALEATORIO ENTERO.
Si se DEFINEN LIMITES, el numero generado quedará entre estos LIMITES.
'''
# Se GENERA un NUMERO ALEATORIO ENTERO ENTRE 0 y 3
numero_saludo = random.randint(0, 3)

print(lista_saludos[numero_saludo] + ', ' + nombre)