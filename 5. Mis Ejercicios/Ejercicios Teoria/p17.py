'''
    ESTRUCTURAS DE CONTROL:
    
    1.- SECUENCIA.
    2.- SELECCION.
    3.- ITERACION.
    4.- BLOQUE CODIGO.
    5.- FUNCIONES.
'''
'''    
    BLOQUE DE CODIGO:
    
    Permiten DIFERENCIAR unas partes de la SECUENCIA de INSTRUCCIONES de otras.
    Son GRUPOS de INSTRUCCIONES que se AGRUPAN por algún motivo.
    
    Se utilizan NO TANTO para ORGANIZAR la SECUENCIA de INSTRUCCIONES sino como forma de PERMITIR la VARIACION de esta SECUENCIA con SELECCION(CONDICION) y BUCLES.
'''
'''
    FUNCIONES:
    
    Una FUNCION no es mas que un BLOQUE de CODIGO con un NOMBRE/ETIQUETA que puede ser INVOCADO/LLAMADO para su EJECUCION por este NOMBRE/ETIQUETA.
    
    En Python, la CREACION de una FUNCION EMPIEZA con la PALABRA RESERVADA def.
    
    Las FUNCIONES admiten una serie de DATOS de ENTRADA, PARAMETROS, NINGUNO(), UNO(parametro) o VARIOS(parametro1, parametro2,..) SEPARADOS POR COMAS.
    
    Una FUNCION tambien puede DEVOLVER UN RESULTADO, lo hace a través de la SENTENCIA return que será la ULTIMA que ejecute la FUNCION.
    
    RESUMIENDO --> Una FUNCION es un BLOQUE de CODIGO con una ETIQUETA\NOMBRE que la IDENTIFICA y permite INVOCARLO cada vez que se necesite y que permite el ENVIO de PARAMETROS de ENTRADA y puede DEVOLVER un RESULTADO.
'''

def suma(operando1, operando2):
    return operando1 + operando2

valor1 = input('Introduce el primer valor:')
valor1 = int(valor1)

valor2 = input('Introduce el segundo valor:')
valor2 = int(valor2)

total = suma(valor1, valor2)

print('El resultado de sumar {} y {} es {}'.format(valor1, valor2, total))

'''
    MAS SOBRE FUNCIONES:
    
    Las FUNCIONES ENCAPSULAN cierta FUNCIONALIDAD, responden al MODELO E --> P --> S IGUAL q los PROGRAMAS, por lo tanto pueden considerarse SUBPROGRAMAS.
    
    AMBITO DE UNA FUNCION: Variables GLOBALES y LOCALES.
    
        1.- Variable GLOBAL: Se definen en el CUERPO PRINCIPAL del PROGRAMA y PUEDE ser UTILIZADA en CUALQUIER PARTE del PROGRAMA.
        2.- Variable LOCAL : Se definen en el CUERPO de una FUNCION y SOLO PUEDE ser UTILIZADA DENTRO de la FUNCION que la CREA.
        
    Lo ANTERIOR tiene varias CONSECUENCIAS:
    
        1.- El NOMBRE de una VARIABLE se refiere a SU VALOR en SU AMBITO.
        2.- DENTRO de una FUNCION SE PUEDE ACCEDER a una VARIABLE GLOBAL.
        3.- DENTRO de una FUNCION NO SE PUEDE MODIFICAR una VARIABLE GLOBAL.
            3.1.- A NO SER QUE SE INDIQUE EXPLICITAMENTE que es una VARIABLE GLOBAL con la sentencia --> global nombre_variable_global
    
    ¡¡EXCEPCIONES!!:
    
    TODO lo dicho sirve para VARIABLES que son consideradas CONTENEDORES, aquellas que son consideradas ETIQUETAS (Ej. las LISTAS) no actúan así.
    Esto se llama PASAR PARAMETROS de una función POR VALOR(CONTENEDOR) o por REFERENCIA(ETIQUETA).
'''

'''
    ARGUMENTOS/PARAMETROS DE ENTRADA:
    
    1.- ARGUMENTOS FIJOS       --> Si NO se INFORMAN TODOS, se produce un ERROR   --> def nombre_funcion(param1, param2)
    
    2.- ARGUMENTOS POR DEFECTO --> Si NO se INFORMAN, TIENEN un VALOR POR DEFECTO --> def nombre_funcion(param1 = valor, param2 = valor)
    
    3.- ARGUMENTOS VARIABLES   --> Pueden recibir un NUMERO VARIABLE de ARGUMENTOS, una LISTA([]) INDETERMINADA DE ARGUMENTOS --> def nombre_funcion(*lista_argumentos)
    
    4.- ARGUMENTOS VARIABLES DICCIONARIO --> Pueden recibir un NUMERO VARIABLE de ARGUMENTOS, una DICCIONARIO({}) INDETERMINADO DE PARES CLAVE-VALOR --> def nombre_funcion(**diccionario)
    
    NOTA:
    En el caso de que sean necesarios DISTINTOS TIPOS DE ARGUMENTOS el ORDEN de estos en la "FIRMA" de la FUNCION serán:
        1.- POSICIONALES (FIJOS, POR DEFECTO)
        2.- VARIABLES (LISTA)
        3.- VARIABLES CLAVE-VALOR (DICCIONARIO)
        
'''

'''
    ARGUMENTOS FIJOS:
'''
def suma_fijos(s1, s2):
    return s1 + s2

# SI NO SE "PASAN" TODOS los ARGUMENTOS DECLARADOS en la FIRMA de la FUNCION DARA ERROR.
# ERROR
print(suma_fijos(1))
# CORRECTO
print(suma_fijos(1,2))



'''
    ARGUMENTOS POR DEFECTO:
'''
def suma_por_defecto(s1=1, s2=2):
    return s1 + s2

# SI NO SE "PASA" alguno de ellos, se utiliza su VALOR POR DEFECTO y TODO FUNCIONA.
# CORRECTO
print(suma_por_defecto())
# CORRECTO
print(suma_por_defecto(1))
# CORRECTO
# NOTA: PYTHON permite "INFORMAR" un ARGUMENTO POR SU NOMBRE, NO SOLO POR SU ORDEN DENTRO DE LA "FIRMA".
print(suma_por_defecto(s2=3))
# CORRECTO
print(suma_por_defecto(1,2))



'''
    ARGUMENTOS VARIABLES:
'''
def suma_variables(*elementos):
    suma = 0
    for elemento in elementos:
        suma = suma + elemento
        #suma += elemento
        
    return suma/len(elementos)

print(suma_variables(1,2,3,4,5))

'''
    ARGUMENTOS VARIABLES DICCIONARIO
'''
def asignaturasymedia(**notas):
    suma = 0
    
    # ATENCION a como 
    for asignatura, nota in notas.items():
        print(asignatura, ':', nota)
        suma = suma + nota
    
    print('******')
    print('Nota Media Curso: ', suma/len(notas))

#
asignaturasymedia(Matematicas = 5.5, Naturales = 7, Fisica = 9, Española = 7, Idioma = 8.5)