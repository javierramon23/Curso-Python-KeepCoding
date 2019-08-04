'''
FUNCION que se realiza una CONVERSION de MONEDA
'''
def conversion(tipo_cambio, cantidad_moneda):
    # Se REDONDEA el CAMBIO a DOS DECIMALES.
    conversion = round(cantidad_moneda * tipo_cambio, 2)
    
    # Se MUESTRAN los RESULTADOS
    print('{} $ a una tasa de cambio de {}\nTotal {}€'.format(cantidad_moneda, tipo_cambio, conversion))


# ENTRADA de DATOS.
str_tipo_cambio = input('Cual es el cambio actual de Dolar a Euros?: ')
str_cantidad_moneda = input('Cuantos Dolares quieres cambiar?: ')

# CONVERSION DE CADENA a FLOAT
tipo_cambio = float(str_tipo_cambio)
cantidad_moneda = float(str_cantidad_moneda)

# Se INVOCA a la FUNCION de CONVERSION de MONEDA.
conversion(tipo_cambio, cantidad_moneda)