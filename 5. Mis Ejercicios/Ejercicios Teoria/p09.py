'''
    LISTA y TUPLAS en PYTHON.
    
    Las LISTAS y TUPLAS es como se conocen a los ARRAYS en PYTHON aunque también pueden verse como TABLAS de VALORES.
    
    Son secuencias ITERABLES de elementos DEL MISMO o DISTINTO TIPO.
    
    La UNICA DIFERENCIA REAL entre LISTAS y TUPLAS es que las LISTAS SE PUEDEN MODIFICAR y las TUPLAS NO (Ni Longitud, Ni Contenido).
    
    A la hora de CREARLAS tambien existen diferencia, las TUPLAS se crean utilizando CORCHETES '[]' y las TUPLAS, utilizando PARENTESIS '()'
    
    Para ACCEDER a cada uno de los ELEMENTOS de una LISTA/TUPLA se UTILIZAN INDICES, que representan CADA UNA DE LAS POSICIONES de los ELEMENTOS.
'''

'''
    ¡¡¡ES IMPORTANTE RECORDAR QUE EL INDICE INICIAL DE UNA LISTA/TUPLA es el '0' NO el '1'!!!
'''

'''
    Algunos EJEMPLOS de ACCESO a ELEMENTOS:
'''
listaPrueba = ['Enero', 'Febrero', 'Marzo', 4, 5, 6, True, False]

tuplaPrueba = ('Enero', 'Febrero', 'Marzo', 4, 5, 6, True, False)

# Por medio de INDICES: nombre_LISTA[indice] | nombre_TUPLA[indice]

print('La LISTA de ejemplo es: {}\n'.format(listaPrueba))
print('La TUPLA de ejemplo es: {}\n'.format(tuplaPrueba))

print('El elemento 3 de la LISTA es: {}'.format(listaPrueba[2]))
print('El elemento 4 de la TUPLA es: {}\n'.format(tuplaPrueba[3]))

# Acceso por la PARTE FINAL: nombre_LISTA[indice_NEGATIVO] | nombre_TUPLA[indice_NEGATIVO]
# DONDE EL ULTIMO INDICE sera el '-1', el anterior, '-2', '-3' y asi hasta el primero.

print('El ULTIMO elemento de la LISTA es: {}'.format(listaPrueba[-1]))
print('El PENULTIMO elemento de la TUPLA es: {}\n'.format(listaPrueba[-2]))

# Acceso a SUBLISTAS/SUBTUPLAS concretas desde el INICIO: nombreLISTA[indice_inicial:indice_final + 1] | nombreTUPLA[indice_inicial:indice_final + 1]
# NOTAR que SIEMPRE hay que SUMAR UNO al LIMITE FINAL por que ese elemento NO ESTARA INCLUIDO en la SUBLISTA/SUBTUPLA
# Del mismo modo podemos utilizar INDICES NEGATIVOS para seleccionar SUBLISTAS/SUBTUPLAS desde el FINAL.

print('Los DOS PRIMEROS elementos de la LISTA son: {}'.format(listaPrueba[0:2]))
print('Los DOS ULTIMOS de la TUPLA son: {}\n'.format(listaPrueba[-5:-1]))

# Existen unas VARIANTES de lo ANTERIOR y consiste en NO especificar el PRIMER ELEMENTO del CONJUNTO o el ULTIMO
# lo que INDICA que la SUBLISTA/SUBTUPLA se inicia desde el PRIMER ELEMENTO o hasta el ULTIMO.
# Del mismo modo podemos utilizar INDICES NEGATIVOS para seleccionar SUBLISTAS/SUBTUPLAS desde el FINAL.

print('Los TRES PRIMEROS elementos de la LISTA son: {}'.format(listaPrueba[:3]))
print('Los TRES ULTIMOS de la LISTA son: {}\n'.format(listaPrueba[5:]))

print('Los TRES PRIMEROS elementos de la LISTA son: {}'.format(listaPrueba[:-5]))
print('Los TRES ULTIMOS de la LISTA son: {}\n'.format(listaPrueba[-3:]))

'''
    MANIPULACION de LISTAS --> LAS TUPLAS SON INMUTABLES, NO SE PUEDEN MODIFICAR
'''

'''
    INSERTAR ELEMENTOS, DOS FORMAS:
    1.- CONCATENANDO el ELEMENTO a la LISTA '+' --> nombreLista + [elemento]
    2.- Con el METODO append() --> nombreLista.append(elemento)
    
    !!!EL NUEVO ELEMENTO SIEMPRE SE INSERTA AL FINAL de la LISTA.
'''
print('La Lista INICIAL es: {}'.format(listaPrueba))

# Se inserta el elemento 'NOVIEMBRE' en la LISTA utilizando el METODO append()
listaPrueba.append('NOVIEMBRE')
# Se inserta el elemento 'DICIEMBRE' en la LISTA utilizando CONCATENACION
listaPrueba += ['DICIEMBRE']

print('Si INSERTAMOS el elmento {} y el elemento {} a la Lista INICIAL, el resultado es: {}\n'.format('NOVIEMBRE','DICIEMBRE',listaPrueba))

'''
    ELIMINAR ELEMENTOS, DOS FORMAS:
    1.- Por INDICE con el METODO 'del':
        1.1.- Elementos INDIVIDUALES --> del nombreLista[indice_elemento]
        1.2.- SUBLISTAS de Elementos --> del nombreLista[indice_inicial:indice_final]
        
    2.- Por CONTENIDO con el METODO remove() --> nombreLista.remove(elemento_a_borrar)
'''

listaInicial = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis']

# Borrado con METODO 'del' de UN ELEMENTO CONCRETO.
print('La LISTA inicial es {}\n'.format(listaInicial))
del listaInicial[0]
print('La LISTA si BORRAMOS el ELEMENTO 0 es {}\n'.format(listaInicial))

# Borrado con METODO 'del' de RANGO de ELEMENTOS.
del listaInicial[0:2]
print('La LISTA si BORRAMOS los DOS PRIMEROS ELEMENTOS es {}\n'.format(listaInicial))

# Borrado con METODO 'remove()' de un ELEMENTO.
'''
    !!!IMPORTANTE: EL ELEMENTO QUE QUEREMOS BORRAR DEBE EXISTIR SINO EL PROGRAMA DARA UN ERROR DE EJECUCION.
'''
listaInicial.remove('Seis')
print('La LISTA si BORRAMOS el ELEMENTO con CONTENIDO "Seis" es {}\n'.format(listaInicial))

'''
    RECORRER LISTAS/TUPLAS:
    
    Solo es necesario crear un BLUCE que vaya desde la POSICION (INDICE) '0' hasta el INDICE 'len(lista) - 1'
'''
listaBucle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print('Recorrer LISTA con un Bucle FOR IN:')

for item in listaBucle:
    print(item)

print('')
print('Recorrer LISTA con un Bucle FOR IN RANGE:')
# El valor '0' de RANGE NO ES NECESARIO PONERLO, BASTA CON PONER el VALOR FINAL.
for i in range(0, len(listaBucle)):
    print(listaBucle[i])
    
print('')
print('Recorrer LISTA con un Bucle WHILE:')
indice = 0
while indice < len(listaBucle):
    print(listaBucle[indice])
    indice += 1
    
'''
    COPIAR LISTAS
    
    La forma mas sencilla de COPIAR una LISTA es --> cadena_nueva = cadena_vieja[:]
'''
print('')
listaUno = ['Voy', 'a', 'copiar', 'esta', 'lista']
listaDos = listaUno[:]

print('La LISTA ORIGEN es: {}\n'.format(listaUno))
print('La LISTA DESTINO despues de COPIARLA es: {}'.format(listaDos))









