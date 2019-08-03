import math

# Bucle INFINITO.
while True:
    # INTRODUCCION de DATOS
    str_ancho_techo = input('Metros de ancho del techo?: ')
    ancho_techo = float(str_ancho_techo)
    str_largo_techo = input('Metros de largo del techo?: ')
    largo_techo = float(str_largo_techo)

    if ancho_techo <= 0 or largo_techo <= 0:
        print('Las medidas del techo no pueden ser negativas.')
    else:
        # SUPERFICIE a PINTAR: TECHO ES RECTANGULAR --> Lado x Lado
        # superficie_total = ancho_techo * largo_techo

        # SUPERFICIE a PINTAR: TECHO ES CIRCULAR --> pi x radio^2
        superficie_total = math.pi * ancho_techo ** 2

        '''
        REDONDEO de un FLOAT a un ENTERO:
        2 FUNCIONES del MODULO "math": "ceil()" y "floor()"
            - ceil() : REDONDEA el FLOAT al ENTERO SUPERIOR MAS CERCANO.
            - floor(): REDONDEO el FLOAT al ENTERO INFERIOR MAS CERCANO.
        '''
        # Si con 5 litros de pintura se pintan 100 m2
        # Basta una sencilla REGLA de TRES.

        '''
        ¿CUANTOS LITROS DE PINTURA NECESITAMOS?
        '''
        litros_pintura = math.ceil((superficie_total * 5) / 100)

        '''
        ¿CUANTOS BOTES DE PINTURA DE 5 LITROS NECESITAMOS?
        '''
        # SIN MODULO "math"
        '''
        CON la DIVISION ENTERA(//) CALCULAMOS LOS BOTES COMPLETOS QUE NECESITAMOS
        '''
        botes_pintura = litros_pintura // 5

        '''
        CON el MODULO de la DIVISION(%) COMPROBAMOS SI NECESITAMOS ALGUN BOTE EXTRA.
        SI el RESTO NO ES 0, NECESITAMOS UN BOTE MAS.
        '''
        # OPERADOR TERNARIO: resultado = "valor_si" IF CONDICION ELSE "valor_no"
        botes_pintura += 1 if litros_pintura % 5 > 0 else 0

        # CON MODULO "math"
        # botes_pintura = math.ceil(litros_pintura / 5)

        # MUESTRA RESULTADOS
        print('Necesitaras {} litros de pintura para pintar {} m2 de techo.'.format(litros_pintura, superficie_total))
        print('Por lo tanto necesitaras comprar {} botes de pintura para hacerlo.'.format(botes_pintura))
        
        # FINALIZAMOS el WHILE
        break
