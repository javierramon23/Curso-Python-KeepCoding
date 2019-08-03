'''
    ESTRUCTURAS DE CONTROL:
    
    1.- SECUENCIA.
    2.- SELECCION.
    3.- ITERACION.
    4.- BLOQUE CODIGO.
    5.- FUNCIONES.
    
'''

'''
    SELECCION(CONDICION):
    
    Es una BIFURCACION en la SECUENCIA a causa de una CONDICION LOGICA (True/False).
    
    Aparece la INSTRUCCION "IF" que PERMITE IMPLEMENTAR esta SELECCION (CONDICION), en PYTHON existen TRES FORMAS de utilizar el "IF" (SELECCION):
    
        1.- SELECCION/CONDICION BASICA: if
            
            if condicion_logica_se_cumple:
                Bloque_Codigo
            
        2.- SELECCION/CONDICION SIMPLE: if - else
        
            if condicion_logica_se_cumple:
                Bloque_Codigo
            else:
                Bloque_Codigo
                
        3.- SELECCION/CONDICION MULTIPLE: if - elif - else
        
            if condicion_logica_1_se_cumple:
                Bloque_Codigo
            elif condicion_logica_2_se_cumple:
                Bloque_Codigo
            elif condicion_logica_3_se_cumple:
                Bloque_Codigo
            else:
                Bloque_Codigo
    
    La SELECCION/CONDICION permite ROMPER el FLUJO "NORMAL" de EJECUCION de las INSTRUCCIONES, es decir la SECUENCIA de un PROGRAMA.
    
'''
print('SELECCION BASICA:\n')

print('Gracias x participar\n')

print('SELECCION SIMPLE:\n')

num_str = input('Introduce un numero: ')

num = int(num_str)

if num % 2 == 0:
    print('{} es un numero PAR'.format(num))
else:
    print('{} es un numero IMPAR'.format(num))
    
print('Gracias x participar\n')

print('SELECCION MULTIPLE:\n')

vocal = input('Selecciona una VOCAL: ')

if vocal == 'a':
    print('Has pulsado la letra "a"')
elif vocal == 'e':
    print('Has pulsado la letra "e"')
elif vocal == 'i':
    print('Has pulsado la letra "i"')
elif vocal == 'o':
    print('Has pulsado la letra "o"')
elif vocal == 'u':
    print('Has pulsado la letra "u"')
else:
    print('NO HAS PULSADO UNA VOCAL')
    
print('Gracias x participar')
