'''
    MODULOS Y LIBRERIAS:
    
    LOS MODULOS:
    
    Son FUNCIONALIDADES que NO FORMAN PARTE del NUCLEO de PYTHON pero que pueden ser IMPORTADAS a este para poder utilizarlas.
    
    Un ejemplo de MODULO que se utiliza mucho en PYHTON es el MODULO RANDOM que incluye FUNCIONES para generar distintos tipos de DATOS ALEATORIOS.
    
    Para poder utilizar un MODULO, PRIMERO es necesario IMPORTARLO:
    
        import nombre_modulo
    
    Una vez IMPORTADO al nuestro programa, podemos INVOCAR las distintas FUNCIONES que incluye:
    
        nombre_modulo.nombre_funcion()
    
    CUALQUIER FICHERO de PYTHON (.py) puede ser IMPORTADO para utilizarlo como un MODULO por OTRO FICHERO PYTHON.
    
    Es decir, CUALQUIER PROGRAMA PYTHON PUEDE SER MODULO DE OTRO PROGRAMA PYTHON.
    
    Lo que plantea la siguiente DUDA.......¿Como se sabe si un programa esta ejecutandose como PROGRAMA INDEPENDIENTE o como MODULO de OTRO?:
    
    Cuando se ejecuta un programa PYTHON, se CREA AUTOMATICAMENTE una VARIABLE GLOBAL --> __name__, cuyo VALOR permite conocer en cual de las dos situaciones estamos:
    
        1.- __name__ == __main__       --> Si el FICHERO .PY se esta ejecutando como PROGRAMA INDEPENDIENTE.
        2.- __name__ == nombre_fichero --> Si el FICHERO .PY está actuando como un MODULO IMPORTADO.
'''

import random

print("Lista de Números generados de manera aleatorio con el MODULO RANDOM:\n")

for num in range(10):
    '''
        La función "randint(limite_inferior, limite_superior)" genera un numero ENTERO PSEUDOALEATORIO ENTRE el limite_inferior y el limite_superior.
    '''
    print('Numero {}: {}'.format(num,random.randint(0,10)))
    
'''
    VARIABLE GLOBAL __name__ :
'''

if __name__ == '__main__':
    print('\nEl Programa se esta ejecutando de forma INDEPENDIENTE: El Valor de la Variable Global __name__ es', __name__)
else:
    print('El Programa se esta ejecutando como un MODULO: El Valor de la Variable Global __name__ es', __name__)

'''
   IMPORTAR PARTES o FUNCIONALIDADES CONCRETAS:
   
   Además de IMPORTAR un PROGRAMA COMPLETO es posible IMPORTAR aquellas FUNCIONES/FUNCIONALIDADES ESPECIFICAS de un PROGRAMA.
   
       from nombre_archivo.py import nombre_funcion1, nombre_funcion2,..., nombre_funcionN
'''

'''
    LIBRERIAS:
    
    En muchas ocasiones se utiliza la palabra LIBRERIA como un SINONIMO de MODULO pero en realidad, una LIBRERIA es un CONJUNTO DE MODULOS que se publican para su USO PUBLICO.
'''
        