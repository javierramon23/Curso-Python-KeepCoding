'''
EJERCICIO 4:
'''
'''
Los NUMEROS en la CADENA indican DONDE DEBEN INSERTARSE
las palabras INTRODUCIDAS.
'''
plantilla = "Un 0 1 debe 2 3"
plantilla_sustitucion = 'Un {} {} debe {} {}'

nombre = input('Sustantivo de la frase?: ')
verbo = input('Verbo de la frase?: ')
adverbio = input('Adverbio de la frase?: ')
adjetivo = input('Adjetivo de la frase?: ')

# CUENTA los CARACTERES de la PLANTILLA.
contador_caracteres = 0
# CONTIENE la FRASE FINAL QUE SE FORMARA, la PLANTILLA + las PALABRAS.
frase = ''

'''
UNA CADENA(STRING) NO ES MAS QUE UNA LISTA DE CARACTERES y por lo tanto
ES POSIBLE RECORRERLA CARACTER A CARACTER con un BUCLE de REPETICION.

La FUNCION len() DEVUELVE el NUMERO de CARACTERES de UNA CADENA.
'''
while contador_caracteres < len(plantilla):
    # Para saber donde INSERTAR cada una de las PALABRAS INTRODUCIDAS en la PLANTILLA.
    if plantilla[contador_caracteres] == '0':
        frase = frase + nombre
    elif plantilla[contador_caracteres] == '1':
        frase= frase + adjetivo
    elif plantilla[contador_caracteres] == '2':
        frase= frase + verbo
    elif plantilla[contador_caracteres] == '3':
        frase= frase + adverbio
    else:
        # Si no es un HUECO para RELLENAR(0, 1, 2, 3) se PONER el CARACTER "leido" DIRECTAMENTE
        frase = frase + plantilla[contador_caracteres]    
    # Se pasa la SIGUIENTE CARACTER de la CADENA.
    contador_caracteres += 1

print(frase)

'''
VERSION CON SUSTITUCION.
'''
# UTILIZANDO SUSTITUCION, es decir, las LLAVES ({}) y el METODO "format()".
# El CODIGO se SIMPLIFICA MUCHO.
print(plantilla_sustitucion.format(nombre, adjetivo, verbo, adverbio))



