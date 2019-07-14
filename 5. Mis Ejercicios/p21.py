'''
    DECORADORES:
    
    Un DECORADOR es una FUNCION que se APLICA a OTRA FUNCION para INCREMENTAR o MODIFICAR su FUNCIONALIDAD.
    
    Un DECORADOR TOMA una FUNCION como ENTRADA y la DEVUELVE MODIFICADA como RESUTADO.
'''

# FUNCIONES INICIALES:
# Se limitan a realizar la operación y mostrar el resultado.
def suma(op1, op2):
    return op1 + op2

def cuadrado(op):
    return op * op

def areaTriangulo(base, altura):
    return (base * altura)/2

print(suma(1,2))

# FUNCIONES y PARAMETROS:
# Ademas de mostrar el resultado, informan de los PARAMETROS:

def suma(op1, op2):
    print('El primer operando de la operacion es {}'.format(op1))
    print('El primer segundo de la operacion es {}'.format(op2))
    return op1 + op2

print(suma(1,2))

# FUNCION "debug".
# Tomando una FUNCION como PARAMETRO de ENTRADA DEVUELVE otra FUNCION que:
# 1.-
# 2.-
def debug(funcion):
    
    def outFunction(*args):
        
        return funcion(*args)
    
    return outFunction
    


