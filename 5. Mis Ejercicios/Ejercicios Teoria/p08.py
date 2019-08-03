'''
    CODIGOS ASCII y CODIGO UNICODE:
    
    Representan los CODIGOS NUMERICOS de TODOS los CARACTERES que un computador puede representar.
    
    Se organizan de la siguiente manera:
    Códigos de CONTROL: del 00 al 31 y el 127: \n, \t, \b, etc.
    Códigos IMPRIMIBLES: del 32 al 126: por ejemplo, letras mayusculas y minusculas, numeros, simbolos, etc.
    Códigos EXTENDIDOS: del 128 al 255: caracteres específicos de cada idioma como por ejemplo, la 'Ñ'.
'''

'''
    Dos METODOS que se pueden utilizar para la CONVERSION de CARACTERES en COD. ASCII y VICEVERSA son:
    
    1. ord(caracter): Devuelve el NUMERO ENTERO asociado a UN CARACTER.
    2. chr(entero): Devuelve el CARACTER asociado al NUMERO ENTERO.
'''
caracter = 'a'
print('El codigo ASCII del caracter "{}" es {}'.format(caracter, ord(caracter)))

cod_caracter = 97
print('El codigo ASCII {} representa al caracter "{}"'.format(cod_caracter, chr(cod_caracter)))