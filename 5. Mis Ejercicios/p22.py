'''
    DATOS Y SUS TIPOS:
    
    Un DATO no es mas que un "TROZO DE INFORMACION" que tendrá sentido en su CONTEXTO.
    
    En los CONTEXTOS HABITUALES tenemos DOS TIPOS de DATOS:
        1.- TEXTO.
        2.- NUMEROS.
    
    Además existe OTRO TIPO de DATOS menos obvio:
    
        3.- BOOLEANOS --> SI/NO o Verdadero/Falso(True/False)
    
    De FORMA MAS FORMAL otra CLASIFICACION de TIPOS de DATOS es:
        1.- PRIMITIVOS:
            1.1.- CARACTERES.
            1.2.- NUMERICOS.
            1.3.- BOOLEANOS.
            
        2.- COMPUESTOS/ESTRUCTARDOS: Formados por la COMBINACION de DATOS PRIMITIVOS:
            2.1.- ARRAYS: LISTA de DATOS PRIMITIVOS
            2.2.- CADENAS de CARACTERES/STRINGS: LISTA DE CARACTERES
            2.3.- REGISTROS/DICCIONARIOS.
'''

'''
    LAS VARIABLES:
    
    Una VARIABLE no es más que un CONTENEDOR de DATOS que contendrá un VALOR y se identifica con un NOMBRE.
    
    El CONTENIDO de una VARIABLE puede CAMBIAR a lo largo de un PROGRAMA.
    
    ASIGNACION de VARIABLES:
    
    Cuando se trabaja con VARIABLES, el SIGNO '=' representa ASIGNACION y no IGUALDAD:
    
        A = B --> El ALGEBRA, el SIGNO '=' implica que la PARTE IZQUIERDA de la expresión es IDENTICA a la PARTE DERECHA.
        
        A = B --> En PROGRAMACIÓN, es SIGNO '=' implica que la PARTE IZQUIERDA de la expresión SE VA A CONVERTIR en la PARTE DERECHA.
'''

'''
    TIPOS DE VARIABLES:
    
        1.- TIPADO DEBIL/FUERTE:
            
            Un LENGUAJE es FUERTEMENTE TIPADO si una VARIABLE de un DETERMINADO TIPO SOLO PUEDE USARSE CON DATOS DE ESE MISMO TIPO.
            
            SI --> a = 1 y b = '2':
            
            La expresion a + b DARIA UN ERROR en un LENGUAJE FUERTEMENTE TIPADO.....COMO PYTHON.
            
            En un LENGUAJE DEBILMENTE TIPADO, se produciría una CONVERSION DE TIPOS y se realizaría la operación....COMO EN JAVASCRIPT.
            
        2.- TIPADO ESTATICO/DINAMICO:
        
            En un LENGUAJE de TIPADO ESTATICO se requiere que la VARIABLE SE DECLARE de un TIPO y se MANTIENE ASI TODA LA VIDA DEL PROGRAMA.
            En un LENGUAJE de TIPADO DINAMICO ASUME el TIPO de VARIABLE en función del DATO QUE CONTIENE y PUEDE CMABIAR EL TIPO a lo largo de la VIDA DEL PROGRAMA.
'''

'''
    SON LAS VARIABLES ETIQUETAS O CONTENEDORES????
    
    Ambas afirmaciones SON CIERTAS, segun el TIPO y la ESTRUCTURA de los DATOS, los LENGUAJES de PROGRAMACIÓN deciden utilizar las VARIABLES como ETIQUETAS o CONTENEDORES.
    
    Un ejemplo de estos comportamientos en PYTHON sería el siguiente:
    
        Las VARIABLES de tipo ENTERO actuan como CONTENEDORES.
        Las VARIABLES de tipo LISTA actuan como ETIQUETAS.
        
    ¿POR QUE ESTO ES IMPORTANTE?:
    
    A la hora de COPIAR VARIABLES hay que tener en cuenta este COMPORTAMIENTO para evitar RESULTADOS NO ESPERADOS.
'''

print('Variables CONTENEDORES vs Variables ETIQUETAS:')
print('Variables CONTENEDORES:')

a = 10
b = a

print('El valor INICIAL de a = {} y el de b = {}'.format(a,b))

a += 1

print('El valor FINAL de a = {} y el de b = {}'.format(a,b))

print('Variables ETIQUETAS:')

a = [1,2,3,4,5,6]
b = a

print('El valor INICIAL de a = {} y el de b = {}'.format(a,b))

a.append(7)

print('El valor FINAL de a = {} y el de b = {}'.format(a,b))

b = a[:]

print('Para COPIAR una LISTA debemos utilizar la EXPRESION "[:]"')

a.append(8)

print('El valor DEFINITIVO de a = {} y el de b = {}'.format(a,b))

