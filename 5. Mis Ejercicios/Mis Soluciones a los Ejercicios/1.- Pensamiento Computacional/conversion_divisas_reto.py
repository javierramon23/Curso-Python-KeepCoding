
'''
FUNCION que se realiza una CONVERSION de MONEDA
'''
def conversion(pais, cantidad_moneda):
    # DICCIONARIO con RELACION de PAISES y CAMBIOS.
    tipos_de_cambio = {
        'ESPAÑA': 0.91,
        'SUIZA': 0.98,
        'BITCOIN': 0.000092,
        'CHINA': 6.94,
    }
    # Se BUSCA el PAIS en el DICCIONARIO, SI EXISTE, se hace la CONVERSION
    if pais in tipos_de_cambio:
        # Se REDONDEA el CAMBIO a DOS DECIMALES.
        conversion = round(cantidad_moneda * tipos_de_cambio[pais], 2)
        # Se MUESTRAN los RESULTADOS
        print('{} $ a una tasa de cambio de {}\nTotal {}€'.format(cantidad_moneda, tipos_de_cambio[pais], conversion))
    # SI NO EXISTE, se AVISA
    else:
        print('No disponemos del cambio solicitado.')
    

# ENTRADA de DATOS.
pais = input('Cual es el PAIS que vas a VISITAR?: ')
str_cantidad_moneda = input('Cuantos Dolares quieres cambiar?: ')

# CONVERSION DE CADENA a FLOAT
cantidad_moneda = float(str_cantidad_moneda)

# Se INVOCA a la FUNCION de CONVERSION de MONEDA.
conversion(pais, cantidad_moneda)