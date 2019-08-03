'''
    FUNCIONES ANONIMAS o LAMBDA:
    
    Son las UNICAS FUNCIONES que no tienen asignado un NOMBRE u IDENTIFICADOR.
    
    En PYTHON se definen:
        
        lambda lista_argumentos: expresión
'''

# Un ejemplo de una FUNCION ANONIMA/LAMBDA:
# Asignamos la FUNCION ANONIMA a una VARIABLE.
cuadrado = lambda valor: valor**2
# EJECUTAMOS la FUNCION a través del NOMBRE de la VARIABLE.
print(cuadrado(2))

'''
    PARA QUE SIRVEN LAS FUNCIONES LAMBDA:
    
        1.- Pueden utilizarse como ARGUMENTOS de FUNCIONES de NIVEL SUPERIOR.
'''
# FUNCION que DEVUELVE la SUMA de los elementos de una LISTA después de aplicarles una FUNCION.
def sumaTodos(funcion, *lista):
    suma = 0
    
    for numero in lista:
        suma += funcion(numero)
    
    return suma

# Utilizando una FUNCION LAMBDA NO ES NECESARIO definir de forma INDEPENDIENTE la FUNCION que generara los CUADRADOS y los CUBOS.
print(sumaTodos(lambda numero:numero ** 2, 2,5,8,9,7))
print(sumaTodos(lambda numero:numero ** 3, 2,5,8,9,7))
    
