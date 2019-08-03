'''
    GESTION de ERRORES:
    
    Los ERRORES en PROGRAMACION se llaman EXCEPCIONES.
    
    Lo habitual es que el PROGRAMA se DETENGA y de un MENSAJE DE ERROR lo mas EXHAUSTIVO POSIBLE a cerca de el ERROR.
    
    Las EXCEPCIONES son ESTRUCTURAS de DATOS que MANTIENEN TODA LA INFORMACION RELACIONADA CON EL ERROR y que permiten que un LENGUAJE DE PROGRAMACION
    nos de el MENSAJE que se ha comentado en el parrafo anterior.
    
    Gracias a las EXCEPCIONES conseguimos dos cosas:
    
        1.- OBTENER INFORMACION de DONDE, COMO y PORQUE se ha PRODUCIDO el ERROR.
        2.- CONTROLARLA para EVITAR UN COMPORTAMIENTO CATASTROFICO del PROGRAMA.
    
    Es MUY IMPORTANTE CONTROLAR LAS EXCEPCIONES y EVITAR que se produzcan EXCEPCIONES NO CONTROLADAS.
    
'''

'''
    MANEJO O CONTROL de LAS EXCEPCIONES:
    
    Cada LENGUAJE tiene su forma de CONTROLAR/MANEJAR las EXCEPCIONES.
    
    En PYTHON se utiliza el BLOQUE -> try-except-finally.
'''
# Dados los siguientes datos, la división va a GENERAR una EXCEPCION de DIVISION x CERO
dividendo = 5
divisor = 0

# Si no se INCLUYE el BLOQUE 'try-except' el programa se ROMPERA de manera BRUSCA.
try:
    print('El resultado de dividir {} / {} es {}'.format(dividendo/divisor))
    
# Si se incluye el BLOQUE, cuando se produzca la EXCEPCION PYTHON la CONTROLA y podemos CONTROLAR SU COMPORTAMIENTO.
except:
    print('División por 0, la operacion {}/{} no se puede realizar'.format(dividendo, divisor))

'''
    UN BLOQUE TRY-EXCEPT-FINALLY con DETALLE:
    
    try:
        # Aqui el CODIGO 'NORMAL'...el que puede FALLAR.
    
    except IOError:
        # Aqui el CODIGO que se EJECUTARA si se produce un ERROR de E/S
        # INCLUYENDO el TIPO DE EXCEPCIÓN junto con la PALABRA 'except' podemos AFINAR EL TRATAMIENTO de ERRORES
        
    except ZeroDivisionError:
        # Aqui el CODIGO que se EJECUTARA si se produce un ERROR de DIVISION X CERO.
        
    except:
        # Aqui el CODIGO que se EJECUTARA si se produce un CUALQUIER TIPO DE ERROR que no se haya ESPECIFICADO ANTERIORMENTE
    
    finally:
        # Aqui el CODIGO que se EJECUTARA TANTO SI SE PRODUCE UNA EXCEPCION COMO SI NO.
        # MUY UTIL para temas de CIERRE de FICHEROS, DESCONEXIONES DE BASES de DATOS, DEVOLVER UN RESULTADO, etc..
        # ESTE BLOQUE es OPCIONAL y puede NO APARECER.
        
    Además de CAPTURAR la EXCEPCIÓN POR SU TIPO para tratarla como más nos guste, es posible CAPTURAR TODOS SUS DATOS ASOCIADOS para TRATARLOS.
    
    except Exception as e:
        # Aqui podemos PROCESAR la VARIABLE 'e' para obtener MAS DETALLE de la EXCEPCION.
'''

def division(a,b):
    try:
        resultado = a / b
        
    except TypeError:
        print('Los operandos de la divison deben de ser numeros')
        resultado = None
        
    except ZeroDivisionError:
        print('No es posible realizar la division x cero')
        resultado = None
    
    except Exception as e:
        print('Error {}'.format(e))
        resultado = None
        
    finally:
        return resultado

print()
print('Un ejemplo del TRATAMIENTO de EXCEPCIONES:')
print('\n1.- Si alguno de los operandos no es un NUMERO:')
print(division('3',2))
print('\n2.- Si el DIVISOR introducido es un CERO:')
print(division(5,0))
print('\n3.- Si los OPERANDOS introducidos son CORRECTOS:')
print(division(2,1))