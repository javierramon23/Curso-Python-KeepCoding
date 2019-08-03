'''
    FUNCIONES RECURSIVAS/ITERATIVAS:
    
    Una FUNCION es RECURSIVA si en su EJECUCIÓN SOLO SE INVOCA A SI MISMA de forma REPETIDA.
'''

'''
    NOTA: FORMA ALTERNATIVA de la FUNCION "print()" --> print('cadena_para_imprimir', end = 'un_caracter')
    
    En esta forma, se sustituye el SALTO de LINEA por defecto de print() por el CARACTER ASIGNADO A "end".
'''

'''
    Con la FUNCION "range()" tambien es posible establecer SERIES DE NUMEROS INVERSOS, utilizando INDICES NEGATIVOS para REDUCIR la SERIE.
'''
for contador in range(10, -1, -1):
    print(contador, end = ':')
print('Final')

'''
    COMO CREAR una FUNCION RECURSIVA/ITERATIVA:
    
        1.- Establecer cuna el la OPERACION BASICA a REALIZAR(Ej. Disminuir Contador).
        2.- Establecer el PUNTO DE SALIDA o FINALIZACION (Ej. Contador < 0)
        
        Este ultimo punto es FUNDAMENTAL para evitar la creación de un BUCLE INFINITO.
'''

def cuenta_atras(contador):
    if contador >= 0:
        print(contador, end = ',')
        return cuenta_atras(contador - 1)
    
    print('Fin de la Recursividad')
    return

print()   
print('Cuenta Atras RECURSIVA:')
cuenta_atras(10)