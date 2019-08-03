'''
    ESTRUCTURAS DE CONTROL:
    
    1.- SECUENCIA.
    2.- SELECCION.
    3.- ITERACION.
    4.- BLOQUE CODIGO.
    5.- FUNCIONES.
    
'''

'''
    ITERACION(BUCLE):
    
    Es la REPETICION de un BLOQUE DE CODIGO un numero DETERMINADO DE VECES. Existes TRES formas de implementar un BUCLE:
    
        1.- UNTIL: REPETIR un BLOQUE de CODIGO "HASTA" que se CUMPLA UNA CONDICION --> EN PYTHON NO EXISTE EL BUCLE "UNTIL".
        2.- WHILE: REPETIR un BLOQUE de CODIGO "MIENTRAS" que se CUMPLA UNA CONDICION.
        3.- FOR: REPETIR un BLOQUE de CODIGO UN "NUMERO DETERMINADO" de veces.
    
    NOTA: EXISTE una CUARTA forma de ITERACION denominada RECURSIVIDAD.
'''

'''
    1.- BUCLE UNTIL:
    
        EN PYTHON NO SE INCLUYE LA IMPLEMENTACION DEL BUCLE "UNTIL".
'''

'''
    2.- BUCLE MIENTRAS(WHILE):
    
        condicion = True
        
        while condicion == True:
            Bloque_Codigo
            condicion = comprobar_condicion
        
        Bloque_Codigo
    
'''

print('Los primeros 10 numeros enteros son:')

# Controla el numero de veces que se ejecutara el WHILE.
contador = 0

while contador < 10:
    print(contador)
    # Se MODIFICA la instruccion que controla el WHILE para evitar el BUCLE INFINITO.
    contador +=1

print('Gracias x participar\n')

'''
    3.- BUCLE FOR:
    
        for veces in range(inicio, fin):
            Bloque_Codigo
        
        Bloque_Codigo
    
    FUNCION "range()":
    
    Cuando en Python se utiliza range(ini, fin), lo que devuelve es el siguiente CONJUNTO de VALORES --> [ini, fin), es decir,
    el VALOR SUPERIOR NO FORMA PARTE DEL RANGO
    
'''
print('Los primeros 10 numeros enteros son:')

# NOTAR que el 10 no esta incluido, range() es un INTERVALO ABIERTO por lo que el SEGUNDO VALOR queda EXCLUIDO.
for item in range(0,10):
    print(item)

print('Gracias x participar\n')
