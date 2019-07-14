'''
    CARACTERES Y CADENAS

    Una CADENA o STRING no es mas que un tipo de DATO formado una LISTA de otro tipo de datos: CARACTERES.
    
    Tanto las CADENAS como los CARCATERES se representan entre COMILLAS, SIMPLES o DOBLES ' '/" ".
    
    IMPORTANTE: 4 ES DISTINTO QUE '4'.
    
    Cada CARACTER de una CADENA se almacena en una posición CONTIGUA de la MEMORIA y su FINAL se marca con un CARACTER ESPECIFICO.
'''

# Podemos acceder a un TROZO concreto de una CADENA utilizando la secuencia [indice_desde:indice_hasta+1]
cadena = 'Hola, Mundo'
print('Solo queremos imprimir la SUBCADENA: Mundo')
print(cadena[0:4])

# Tambien es posible trabajar con las CADENAS desde el FINAL de estas:
# Basta con saber que el ULTIMO CARACTER viene representado por el INDICE -1
# El ANTERIOR por -2 y asi SUCESIVAMENTE.

print('Solo queremos imprimir el ULTIMO CARACTER: o')
print(cadena[-1])

# Del mismo modo podemos seleccionar SUBCADENAS de la PARTE FINAL utilizando la secuencia [indice_inicio_negativo:indice_final_negativo]
print('Solo queremos imprimir la SUBCADENA: Hola')
print(cadena[-12:-7])


# Tambien es posible utilizar las sentencias anteriores para SUBCADENAS sin especificar UNO DE LOS INDICES, [:indice_final] o [indice_inicial:]
# La posición vacía significa desde el inicio si va delante de los dos puntos y hasta el final si va detrás de los dos puntos
print('Imprimimos las SUBCADENA: Hola y Mundo sin especificar los INDICES INICIAL y FINAL')
print(cadena[:4])
print(cadena[-5:])

'''
    Las CADENAS tambien se pueden SUMAR y MULTIPLICAR:
    
    La SUMA consiste en UNIR/CONCATENAR las CADENAS: cadena_uno + cadena_2 = cadena_unocadena_dos
    
    La MULTIPLICACION consiste en REPETIR 'N' VECES la CADENA: cadena * 2 = cadenacadena
'''
print('Mi nombre es: ' + 'Javier')
print('Hola' * 3)

'''
    FUNCIONES SOBRE CADENAS: LEN, FIND, UPPER, LOWER, REPLACE.
'''
    
# len(cadena): Devuelve la LONGITUD de la CADENA.
print(len('Mi nombre es Javier'))

# cadena_donde_buscar.find(cadena_a_buscar): Permite BUSCAR una CADENA DENTRO de OTRA.
# Devuelve el INDICE de la CADENA BUSCADA (si la encuentra, si no, DEVUELVE -1

print(('Hola, Mundo').find('Javier'))
print(('Hola, Mundo').find('Hola'))

#cadena.upper(): Devuelve la CADENA con TODOS los CARCATERES en MAYUSCULAS.
print('Hola, Mundo'.upper())

#cadena.lower(): Devuelve la CADENA con TODOS los CARCATERES en MINUSCULAS.
print('Hola, Mundo'.lower())

# cadena.replace(subcadena_buscada, subcadena_a_remplazar): Retorna la CADENA con la NUEVA SUBCADENA REMPLAZADA.
print('Mi nombre es Javier')
print('Mi nombre es Javier'.replace('Javier', 'Alejandro'))

'''
    SECUENCIAS de ESCAPE y CARCATERES ESPECIALES
    
    Una SECUENCIA d ESCAPE está formada por DOS CARACTERES el CARCATER d ESCAPE(\) y el caracter a imprimir o carácter escapado.
    
    EJEMPLOS:
         \n: Salto de Linea.
         \t: Tabulacion.
         \b: Retroceso, elimina el CARCATER ANTERIOR.
    \" o \': Permite imprimir las COMILLAS DOBLES o SIMPLES como un CARACTER NORMAL no como DELIMITADOR de CADENAS.
'''