'''
    ESTRUCTURAS DE CONTROL:
    
    1.- SECUENCIA.
    2.- SELECCION.
    3.- ITERACION.
    4.- BLOQUE CODIGO.
    5.- FUNCIONES.
    
'''

'''
    SECUENCIA:
    
    La ESTRUCTURA de CONTROL mas SENCILLA, se ejecutan las INSTRUCCIONES/SENTENCIAS de manera LINEAL CONSECUTIVAMENTE de la PRIMERA A LA ULTIMA y el PROGRAMA PARA.
    
'''
# Instrucción 1 --> INICIAL
edad_perro_str = input('¿Cuantos años tiene tu perro?:')
# Instrucción 2
edad_perro = int(edad_perro_str)
# Instrucción 3
edad_humana = edad_perro * 7
# Instrucción 4 --> FINAL
print('Tu perro tiene {} años humanos'.format(edad_humana))