'''
    PERSISTENCIA:
    
    De forma simple, la PERSISTENCIA se trata de GUARDAR el ESTADO de una APLICACION para poder RECUPERARLO en otro momento:
    
        - ALMACENAR la INFORMACION en elgún tipo de SOPORTE para poder RECUPERARLO mas adelante.
        - ESTRUCTURAR esta INFORMACION de forma que sea FACILMENTE ALMACENABLE y RECUPERABLE.
    
    ALMACENAMIENTO:
    
    Principalmente dos formas:
        1.- En un ARCHIVO.
        2.- En una BASE de DATOS.
    
    ESTRUCTURA DE DATOS:
    
    Habitualmente dos casos de ALMACENAMIENTO de la INFORMACION:
    
        - Una serie de DATOS cuyos VALORES se almacenan simplemente SEPARADOS por COMAS(,) o PUNTOS y COMAS(;) en un FICHERO.
        - Una serie de DATOS cuyos VALORES se almacenan como un REGISTRO formado por UNIDADES MENORES de INFORMACION denominados CAMPOS.
'''
'''
    MANEJO DE FICHEROS/ARCHIVOS:
    
    Un ARCHIVO es un conjunto de BITS y BYTES con un NOMBRE y una EXTENSION localizado en una UNIDAD de ALMACENAMIENTO EXTERNO.
    Funciona IGUAL que la MEMORIA de un COMPUTADOR.
    
    PYTHON maneja DOS TIPOS de ARCHIVOS:
    
        1.- FICHEROS de TEXTO
        2.- FICHEROS BINARIOS
        
    En ambos casos pueden utilizarse para: GRABAR información, LEER información o AMBAS cosas.
    
    OPERACIONES sobre FICHEROS:
    
        1.- ABRIR un FICHERO:
        
            1.1.- INDICANDO TIPO DE ACCESO:
                1.1.1.- Para LECTURA.
                1.1.2.- Para ESCRITURA.
                1.1.3.- Para LECTURA/ESCRITURA.
                
            1.2.- INDICANDO TIPO FICHERO:
                1.2.1.- TEXTO.
                1.2.2.- BINARIO.
                
        2.- LECTURA/ESCRITURA de un FICHERO: Acceso SIEMPRE SECUENCIAL y HACIA ADELANTE.
            
        3.- CERRAR un FICHERO.
'''

'''
    FICHEROS DE TEXTO:
    
    Buena forma de ALMCENAR INFORMACION TIPO TEXTO --> Formato CSV(Comma-Separated Values) donde los DISTINTOS CAMPOS de un REGISTRO estan SEPARADOS por COMAS(,):
        
        --> nombre, apellido1, apellido2, edad
    
    Otra forma de ALMACENAR INFORMACION TIPO TEXTO --> Formato POSICIONAL donde se define cada CAMPO X SU POSICION en el REGISTRO:
    
        --> Usuario:
                Nombre:    Posición 00 a 29
                Apellido1: Posición 30 a 59
                Apellido2: Posición 60 a 79
                Edad:      Posición 80 a 109
'''

'''
    OPERACIONES CON FICHEROS en DETALLE:
    
        1.- APERTURA de FICHEROS:
        
            --> open('nombre_fichero_con_ruta', 'modo_acceso')
        
            Donde los MODOS pueden ser:
            
                - r : Abrir fichero para LECTURA. El puntero se posiciona al PRINCIPIO del fichero
                - r+: Abrir fichero para LECTURA y ESCRITURA. El puntero se posiciona al PRINCIPIO del fichero
                - w : Trunca a cero la longitud o crea un fichero de texto para escritura. El puntero se posiciona al PRINCIPIO del fichero
                - w+: Abrir fichero para LECTURA y ESCRITURA. Se CREA el fichero si no existe de lo contrario se trunca. El puntero se posiciona al PRINCIPIO del fichero
                - a : Abrir fichero para LECTURA. Se CREA el fichero si no existe. El puntero se posiciona al FINAL del fichero.
                - a+: Abrir fichero para LECTURA y ESCRITURA. Se CREA el fichero si no existe. El puntero se posiciona al FINAL del fichero.
        
            Además el MODO puede determinar el TIPO FICHERO:
                1.- t: TEXTO --> PPOR DEFECTO SI NO SE ESPECIFICA.
                2.- b: BINARO
        
            Cuando se ABRE un FICHERO, se CREA un OBJETO TIPO FICHERO sobre el que se realizan el resto de OPERACIONES:
        
                ficheroPrueba = open('fichero.txt', 'rb')
        
        2.- LECTURA de FICHEROS:
        
            --> fichero.read(n)
        
                Donde 'n' es OPCIONAL, la OPERACION LEERA 'n' CARACTERES, sino, TODO EL FICHERO.
        
                Devuelve 'n' CARACTERES o el TOTAL del FICHERO sobre el que se podrá OPERAR posteriormente.
            
            --> fichero.readLines(n)
            
                Donde 'n' es OPCIONAL, indica el MAXIMO NUMERO DE CARACTERES, como se LEE x LINEAS, SIEMPRE LEE las LINEAS NECESARIAS para CUBRIR ESE NUMERO.
                
                Si no se indica, LEE TODAS las LINEAS del FICHERO.
            
            --> fichero.readLine(n)
            
                Donde 'n' es OPCIONAL, indica el MAXIMO NUMERO DE CARACTERES, si es MAS que el MAXIMO de la LINEA, devuelve la LINEA.
        
        3.- ESCRITURA de FICHEROS:
        
            --> fichero.write(n)
            
                Donde 'n' es la CADENA a ESCRIBIR.
        
        4.- CIERRE de FICHEROS:
        
            --> fichero.close()
'''
'''
    ALGUNOS EJEMPLOS DE TODO LO ANTERIOR:
'''
print('Ejemplo de ALMACENAMIENTO de INFORMACION en FICHERO de TEXTO en FORMATO CSV')

# Se crea un DICCIONARIO con la INFO a GUARDAR
usuario = {
    'nombre': 'Javier',
    'apellido1': 'Ramón',
    'apellido2': 'Sola',
    'edad': 41,
    }

# FUNCION para GUARDAR la INFO en un FICHERO.
def guardar(registro):
    # Se ABRE/CREA el FICHERO DESTINO indicando su NOMBRE y el TIPO de ACCESO.
    # En este caso: w+ --> LECTURA y ESCRITURA
    fSalida = open('salida.txt', 'w+')
    # Se ESCRIBE la INFO en el FICHERO.
    fSalida.write(registro)
    # Se CIERRA el FICHERO una vez se ha finalizado la operacion...MUY IMPORTANTE.
    fSalida.close()
    
# FUNCION para LEER la INFO de un FICHERO.    
def leer():
    fEntrada = open('salida.txt', 'r')
    # NO SE ESPECIFICA LA CANTIDAD DE CARACTERES A LEER, POR LO TANTO SE LEE TODO EL FICHERO.
    fichero = fEntrada.read()
    fEntrada.close()
    return fichero

# EL FICHERO ALMACENA INFO TIPO TEXTO POR LO QUE ES NECESARIO CONVERTIR EL DICCIONARIO EN UNA CADENA ANTES DE GUARDARLO.
csv_usuario = '{},{},{},{}'.format(usuario['nombre'], usuario['apellido1'], usuario['apellido2'], usuario['edad'])

# INVOCAMOS A LA FUNCION PASANDOLE LA CADENA GENERADA CON LOS DATOS DEL DICCIONARIO.
print('\n1.- Se almacena la información del DICCIONARIO en el fichero "salida.txt".')
guardar(csv_usuario)
print('2.- La información ha sido almacenada.')
print('3.- Se lee la información del fichero "salida.txt".')
# INVOCAMOS ALA FUNCION DE LECTURA Y ALMACENAMOS SU RETORNO EN UNA VARIABLE
registro = leer()
print('4.- Se muestra la información leida desde el fichero.\n')
# IMPRIMIMOS EL REGISTRO LEIDO DEL FICHERO
print(registro)