'''
INTERES SIMPLE: A = P x (1 + rt)
    - A = Cantidad Ganada
    - P = Cantidad Invertida
    - r = Interes
    - t = Años transcurridos desde el inicio de la inversion
'''

def interes_simple(inversion, interes, tiempo):
    '''
    Función que calcula el Interes Simple de una Inversion
    '''
    # Al TOTAL le restamos la cantidad invertida INICIAL para obtener el BENEFICIO
    # Para NORMALIZAR la inversion, la REDONDEAMOS con la FUNCION "round()"
    contador = 1
    while contador <= tiempo:
        ganancias = (round(inversion, 2) * (1 + (interes / 100) * contador)) - inversion
        '''
        FORMATEO de DECIMALES con "format()":
        Utilizando la SINTAXIS: {:."numero_decimales"f}
        Se puede determinar el NUMERO de DECIMALES que se MOSTRARAN al IMPRIMIR.
        '''
        print('Tras {} años de una inversion de {:.2f}€ al {:.2f}% de interes, su beneficio acumulado debe ser de {:.2f}€'
        .format(contador,
                inversion, 
                interes, 
                ganancias)
        )
        contador += 1
    '''
    IMPORTANTE: NO ES LO MISMO REDONDEAR CON LA FUNCION "round()" QUE CON EL FORMATO "{:.f}"
    DEL METODO "format()" de "print()".
    EL METODO "round()" MODIFICA EL VALOR, MIENTRAS QUE "format()" SOLO MODIFICA LA FORMA DE
    IMPRIMIRLO.
    '''

# DATOS ENRADA
str_inversion = input('Cantidad Inicial Invertida: ')
str_interes = input('Interes de la Inversion(%): ')
str_tiempo = input('Tiempo Transcurrido(años):')

interes_simple(float(str_inversion),float(str_interes), float(str_tiempo))