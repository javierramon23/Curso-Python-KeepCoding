# CONSTANTE con el % de IMPUESTOS.
TASA_IMPUESTO = 0.055

'''
Como CREAR LISTAS VACIAS de UNIDADES y PRECIOS.
TAMBIEN SE PUEDEN DEFINIR LISTAS VACIAS con la SINTAXIS: nombre_lista[]
'''
lista_precios = list()  
lista_unidades = list()

# Se RELLENAN las LISTAS.
indice = 0 # Para RECORRER las LISTAS.
while indice < 3:
    lista_unidades.append(float(input('Unidades del producto: ')))
    lista_precios.append(float(input('Precio del producto: ')))
    indice += 1 # Se pasa a la SIGUENTE POSICION de la LISTA.

# Se INICIALIZAN los "ACUMULADORES".
subtotal = 0 
tasas = 0 

# Se RECORREN de nuevo las LISTAS para realizar los CALCULOS.
indice = 0 
while indice < 3:
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