import math

# INTRODUCCION de DATOS
str_ancho_techo = input('Metros de ancho del techo?: ')
ancho_techo = float(str_ancho_techo)
str_largo_techo = input('Metros de largo del techo?: ')
largo_techo = float(str_largo_techo)

# SUPERFICIE a PINTAR
superficie_total = ancho_techo * largo_techo

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
botes_pintura += 1 if botes_pintura % 5 > 0 else 0

# CON MODULO "math"
# botes_pintura = math.ceil(litros_pintura / 5)

# MUESTRA RESULTADOS
print('Necesitaras {} botes de pintura para pintar {} m2 de techo.'.format(litros_pintura, superficie_total))
print('Por lo tanto necesitaras comprar {} botes de pintura para hacerlo.'.format(botes_pintura))
