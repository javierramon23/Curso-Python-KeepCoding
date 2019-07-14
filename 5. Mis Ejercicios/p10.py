'''
    LOS BOOLEANOS, OPERADORES LOGICOS Y DE COMPARARCION:
    
    OPERADORES DE COMPARACION:
    
    1.- == : ¿ES IGUAL A?
    2.- != : ¿ES DISTINTO A?
    3.- <  : ¿ES MENOR QUE?
    4.- >  : ¿ES MAYOR QUE?
    5.- <= : ¿ES MENOR O IGUAL QUE?
    6.- >= : ¿ES MAYOR O IGUAL QUE?
    
    La comparacion DEBE DARSE ENTRE DATOS/VARIABLES/CONSTANTES DEL MISMO TIPO.
    
    SU RESULTADO SIEMPRE SERA UN BOOLEANO: True o False.
    
    NOTAR QUE LA PRIMERA LETRA del BOOLEANO TIENE QUE IR EN MAYUSCULAS.
    
    COMPARADORES LOGICOS:
    
    1.-  Y: and --> A and B
    2.-  O: or  --> A or B
    3.- NO: not --> not A
'''
'''
    DICCIONARIOS:
    
    Pueden interprestarse como una LISTA pero donde CADA ELEMENTO esta formado por UN PAR de ELEMENTOS
    una CLAVE y un VALOR asociado a esa CLAVE.
    
    Un DICCIONARIO es un CONJUNTO de PARES CLAVE/VALOR.
    
    A diferencia que en las LISTAS/TUPLAS, para ACCEDER a un ELEMENTO del DICCIONARIO se debe utilizar su CLAVE
    en lugar del INDICE, pudiendo se esta un STRING, un BOOLEANO o un NUMERO. Respesto a los VALORES ASOCIADOS,
    estos pueden ser CUALQUIER TIPO VALIDO en PYTHON, incluso OTRO DICCIONARIO.
    
    CREACION de un DICCIONARIO:
    
    La NOTACIÓN para CREAR un DICCIONARIO ES:
    
    nombreDiccionario = {clave_1:valor_1, clave_2:valor_2, ...., clave_n:valor_n}
    
    ACCESO a los ELEMENTOS:
    
    La NOTACIÓN para ACCEDER a un ELEMENTO de un DICCIONARIO es IGUAL que la utilizada con las LISTAS/TUPLAS, pero
    en lugar de utilizar el INDICE, se utiliza la CLAVE --> nombreDiccionario[clave]
    
    !!!IMPORTANTE¡¡¡: El problema con este TIPO de ACCESO es que SI NO EXISTE LA CLAVE BUSCADA, el PROGRAMA "PETA"
    
    ES MUY RECOMENDABLE UTILIZAR la NOTACIÓN --> nombre_diccionario.get(clave), que NO hace "CASCAR" el PROGRAMA.
'''
miDiccionario = {1:'Lunes', 2:'Martes', 3:'Miercoles', 4:'Jueves', 5:'Viernes', 6:'Sabado', 7:'Domingo'}
print('Mi Diccionario: {}\n'.format(miDiccionario))

print('El PRIMER día de la SEMANA es el {} y el ULTIMO es el {}\n'.format(miDiccionario.get(1), miDiccionario.get(7)))

'''
    RECORRER un DICCIONARIO:
    
    La forma basica de ITERAR un DICCIONARIO es con un BUCLE FOR, la ITERACIÓN de un DICCIONARIO RETORNA LAS CLAVES
    de este.
'''

for clave in miDiccionario:
    print('Clave {} --> Valor: {}'.format(clave, miDiccionario[clave]))
    
'''
    OTRAS FORMAS DE RECORRER el DICCIONARIO:
    
    1.- nombre_diccionario.items() --> Devuelve una TUPLA con la CLAVE y el VALOR.
    2.- nombre_diccionario.keys()  --> Devuelve una TUPLA con las CLAVES.
    3.- nombre_diccionario.items() --> Devuelve una TUPLA con los VALORES.
    
    A partir de estas TUPLAS podemos ITERAR como con cualquier otra TUPLA.
'''

print('\nMi Diccionario es:\n{}\n'.format(miDiccionario.items()))

for item in miDiccionario.items():
    print(item)
    
print('\nMi Diccionario tiene las siguientes CLAVES:\n{}\n'.format(miDiccionario.keys()))
for key in miDiccionario.keys():
    print(key)
    
print('\nMi Diccionario tiene los siguientes VALORES:\n{}\n'.format(miDiccionario.values()))
for valor in miDiccionario.values():
    print(valor)
    
'''
    COMPROBAR EXISTENCIA CLAVE:
    
    1.- NO RECOMENDADA --> De forma SIMILAR a una LISTA/TUPLA --> nombre_diccionario[clave] --> SI NO EXISTE "ROMPE".
    
    2.- Metodo "get()" --> nombre_diccionario.get(clave) --> SI NO EXISTE DEVUELVE el VALOR de Python "None".
    
    3.- OPERADOR "in"  --> clave in nombre_diccionario.
'''

print('\nExiste la CLAVE "1" en Mi Diccionario: {}'.format(miDiccionario.get(1)))
print('\nExiste la CLAVE "8" en Mi Diccionario: {}'.format(miDiccionario.get(8)))
print('\nExiste la CLAVE "2" en Mi Diccionario: {}'.format(2 in miDiccionario))
print('\nExiste la CLAVE "9" en Mi Diccionario: {}'.format(9 in miDiccionario))