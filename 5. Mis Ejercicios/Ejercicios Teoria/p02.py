'''
    Introducir Edad del perro
'''
strEdad = ""

while strEdad == "":
    '''
    Con el metodo "input()" hacemos que Python solicite al usuario un dato de entrada
    desde el teclado.
    '''
    strEdad = input("Edad del perro: ")
    
    '''
    El método "isdigit()" comprueba si el string esta compuesto SOLO DE NUMEROS,
    devuelve un BOOLEANO.
    '''
    if not strEdad.isdigit():
        print("La edad del perro ha de ser un número entero")
        strEdad = ""

# Se debe convertir la entrada x teclado (SIEMPRE UN STRING) en el tipo de dato deseado.
# En este caso, un entero con el metodo "int()".
edad = int(strEdad)

'''
    Calcular edad humana del perro
'''
edadHumana = edad * 7

'''
    Mostrar edad del perro
'''
#print("Su perro tiene %d años humanos" % edadHumana)

'''
El metodo "format()" permite darle formato a una cadena de forma rápida.
'''
print('Su perro tiene {} años humanos'.format(edadHumana))