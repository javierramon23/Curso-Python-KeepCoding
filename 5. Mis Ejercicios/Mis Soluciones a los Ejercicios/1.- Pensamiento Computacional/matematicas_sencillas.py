'''
EJERCICIO 5:
'''
primer_operando_str = input('Primer Operando?: ')
segundo_operando_str = input('Segundo Operando?: ')

'''
CUALQUIER COSA "leida"  a través de "input()" es una CADENA de CARACTERES
por lo tanto es necesario TRANSFORMAR esa CADENA en un NUMERO si se quiere
trabajar con OPERACIONES.
PAra ello utilizamos los METODOS "int(), float()".
'''
primer_operando = float(primer_operando_str)
segundo_operando = float(segundo_operando_str)

print('La SUMA es: {}\nLa RESTA es: {}\nEl PRODUCTO es: {}\nLa DIVISION es: {}'
    .format(primer_operando + segundo_operando,
        primer_operando - segundo_operando, 
        primer_operando * segundo_operando,
        # Con la FUNCION "round()" se REDONDEA un FLOAT con los DECIMALES que se especifiquen.
        round(primer_operando / segundo_operando,1)))

'''
RETO:
'''
ope1_str = input('Primer Operando: ')
ope2_str = input('Segundo Operando: ')

'''
El METODO "isdigit()" DEVUELVE "True" si la CADENA que lo EJECUTA REPRESENTA un NUMERO ENTERO POSITIVO
y False en caso contrario.
'''
if ope1_str.isdigit() and ope2_str.isdigit():
    ope1 = float(ope1_str)
    ope2 = float(ope2_str)

    print('La SUMA es: {}\nLa RESTA es: {}\nEl PRODUCTO es: {}\nLa DIVISION es: {}'
        .format(ope1 + ope2, ope1 - ope2, ope1 * ope2, round(ope1 / ope2,1)))
        # Con la FUNCION "round()" se REDONDEA un FLOAT con los DECIMALES que se especifiquen.
            
else:
    print('Los operandos introducidos no son validos.')


