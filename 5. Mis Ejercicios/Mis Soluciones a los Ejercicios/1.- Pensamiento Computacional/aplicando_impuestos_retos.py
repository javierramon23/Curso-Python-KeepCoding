# CONSTANTE con el % de IMPUESTOS.
TASA_IMPUESTO = 0.055

'''
Como CREAR LISTAS VACIAS de UNIDADES y PRECIOS.
TAMBIEN SE PUEDEN DEFINIR LISTAS VACIAS con la SINTAXIS: nombre_lista[]
'''
lista_precios = list()  
lista_unidades = list()

# Se RELLENAN las LISTAS.
# BUCLE INFINITO que permite PERMITE INSERTAR TODOS los PROUCTOS DESEADOS.
while True:
    unidades_producto = input('Unidades del producto: ')
    precio_unidad = input('Precio del producto: ')

    # BUCLE INFINITO que CONTROLA que SOLO PUEDAN METERSE NUMEROS FLOAT.
    while True:
        '''
        Para CONTROLAR que las CADENAS introducidas x teclado sean FLOAT
        Se CREA una EXCEPCION que CONTROLA la CONVERSION de esas CADENAS el FLOAT
        Si al intentar la CONVERSION se PRODUCE UN ERROR es que la CADENA no es un FLOAT
        y por lo tanto se VUELVE a pedir su INTRODUCCION.
        '''
        try:
            unidades_producto = float(unidades_producto)
            precio_unidad = float(precio_unidad)
        except:
            print('Alguno de los datos introducidos no es valido, vuelve a intentarlo.')
            unidades_producto = input('Unidades del producto: ')
            precio_unidad = input('Precio del producto: ')
        else:
            # Los DATOS INTRODUCIDOS SON NUMEROS FLOAT x lo tanto SALIMOS del BUCLE.
            break
    
    # Se INTRODUCEN los DATOS en las LISTAS.
    lista_unidades.append(unidades_producto)
    lista_precios.append(precio_unidad)

    # Para controlar el NUMERO de PRODUCTOS.
    continuar = input('Mas productos?(S/N): ')
    if continuar.lower() == 'n':
        # No se METEN MAS PRODUCTOS x lo tanto SALIMOS del BUCLE.
        break

# Se INICIALIZAN los "ACUMULADORES".
subtotal = 0 
tasas = 0 

# Se RECORREN de nuevo las LISTAS para realizar los CALCULOS.
indice = 0
while indice < len(lista_precios):
    subtotal = subtotal + (lista_unidades[indice] * lista_precios[indice])
    tasas = subtotal * TASA_IMPUESTO
    indice += 1 # Se pasa a la SIGUENTE POSICION de la LISTA.

# CALCULO FINAL.
total = subtotal + tasas

# Se MUESTRAN los RESULTADOS.
'''
El METODO "round()" permite REDONDEAR un FLOAT
SINTAXIS: round(float, numero_decimales)
'''
print('Subtotal: {}€\nTasas: {}€\nTOTAL: {}€'.
    format(round(subtotal, 2), 
           round(tasas, 2), 
           round(total, 2)
        )
    )