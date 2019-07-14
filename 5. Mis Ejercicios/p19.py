'''
    FUNCIONES de ALTO NIVEL o de NIVEL SUPERIOR:
        Son aquellas FUNCIONES que adminten otras FUNCIONES como PARAMETROS de ENTRADA o que RETORNAN una FUNCION.
    
    FUNCIONES de PRIMER NIVEL:
        Son aquellas FUNCIONES que se tratan como un VALOR(Funcion "NORMAL").
    
    FUNCIONES ANONIMAS:
        Son aquellas que NO ESTAN ASOCIADAS a un NOMBRE o IDENTIFICADOR.
'''

'''
    FUNCION vs FUNCION():
    
        Es importante conocer la DIFERENCIA entre estas dos formas de HACER REFERENCIA a una FUNCION.
        
            1.- nombre_funcion   --> SIN PARENTESIS, NO LA ESTAMOS INVOCANDO/LLAMANDO, como una VARIABLE LOCAL que CONTIENE una FUNCION.
            2.- nombre_funcion() --> La estamos INVOCANDO, es decir, EJECUTANDO.
'''

'''
    FUNCIONES "NORMALES" o de PRIMER NIVEL:
'''
def media(*lista):
    if len(lista) == 0:
        return 0
    
    suma = 0
    for item in lista:
        suma += item
        
    return suma/len(lista)

def maximo(*lista_valores):
    if len(lista_valores) == 0:
        return 0
    
    maximo = lista_valores[0]
    
    '''
    for indice in range(1, len(lista_valores)):
        if lista_valores[indice] >= maximo:
            maximo = lista_valores[indice]
    '''
    
    for valor in lista_valores:
        if valor >= maximo:
            maximo = valor
    
    return maximo

def minimo(*lista_valores):
    if len(lista_valores) == 0:
        return 0
    
    minimo = lista_valores[0]
    
    for valor in lista_valores:
        if valor <= minimo:
            minimo = valor
            
    return minimo

'''
    FUNCION de ALTO NIVEL o NIVEL SUPERIOR:
'''
def estadisticas(tipo_funcion, *lista_valores):
    return tipo_funcion(*lista_valores)


#print(estadisticas(maximo,6,1,13,8,9))
#print(estadisticas(media,6,1,13,8,9))

'''
    FUNCIONES QUE DEVUELVEN FUNCIONES:
'''

'''
    EJEMPLO:
'''
# Definimos un DICCIONARIO vacio.
funciones = dict()

# 'LLenamos' el DICCIONARIO con las FUNCIONES disponibles, con SUS IDENTIFICADORES.
funciones['MAX'] = maximo
funciones['MIN'] = minimo
funciones ['MED'] = media

# FUNCION que determina si una funcion existe dentro del DICCIONARIO y la DEVUELVE(la funcion) SI EXISTE.
def existeFuncion(nombreFuncion):
    if nombreFuncion in funciones.keys():
        # Si la FUNCION existe, DEVUELVE la FUNCION
        return funciones[nombreFuncion]
    return None

# FUNCION que "PROCESA" la ENTRADA del usuario para EVITAR PROBLEMAS.
def procesarEntrada(entrada):
    return entrada.upper()

# LISTA de valores para utilzar.
lista_valores = [2, 4, 6, 0, 8, 10, -1]

# Se solicita al USUARIO que elija una de las FUNCIONES.
funcionSeleccionada = procesarEntrada(input('Selecciona la operación que quieres realizar (MAX, MIN, MED):'))

# Mientras la FUNCION elegida por el USUARIO no EXISTA en el DICCIONARIO, la volvemos a pedir.
while funcionSeleccionada not in funciones.keys():
    print('Esa FUNCION no está disponible, elije una opción de las disponibles.')
    funcionSeleccionada = procesarEntrada(input('Selecciona la Operación que quieres realizar (MAX, MIN, MED):'))


# NOTESE AQUI LA DIFERENCIA ENTRE las DOS FORMAS de HACER REFERENCIA a las FUNCIONES, CON y SIN PARENTESIS.
# En este caso, la variable "funcion" almacenará la FUNCION que le le DEVUELVEN, por lo tanto SIN PARENTESIS.
funcion = existeFuncion(funcionSeleccionada)
# Ahora utilizamos los PARENTESIS para EJECUTAR la FUNCION almacenada en "funcion".
print(funcion(*lista_valores))
    
    