import turtle

theTurtle = turtle.Turtle()

'''
    Funciones en Pyhton:
    Se utiliza la palabra reservada "def" para definir la Función.
    Una función puede definirse SIN PARAMETROS de entrada, solo poniendo los PARENTESIS.
    O estableciendo una serie de PARAMETROS de ENTRADA.
    Los parametros de entrada pueden definirse de varias formas:
    1- Posicionales --> (param1, param2,...).
    2- Por Defecto --> (param1=valor1, param2=valor2,...).
    3- A traves de una LISTA --> (*listaParametros).
    4- A traves de un DICCIONARIO --> (**nombreDiccionario).
'''
def drawTriangle(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(120)
    theTurtle.fd(size)
    theTurtle.left(120)
    theTurtle.fd(size)
    theTurtle.left(120)

def drawSquare(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)

def drawPentagon(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)

'''
Abstracción de los procesos de dibujar Triangulo, cuadrado y pentagono
'''
'''
    Los ARRAYS en Python se pueden definir de varias maneras en función de sus
    propiedades, en este caso se utilizan LISTAS, que son ARRAYS ORDENADOS que
    pueden MODIFICARSE, se definen utilizando PARENTESIS y separando sus elementos con COMAS.
    
    También pueden definirse utilizando la palabra reservada "list()".
    
    Para acceder a un elemento de una LISTA se utilizan los CORCHETES:
    
    nombreLista[posiciónElemento]
    
    IMPORTANTE, las LISTAS en Python comienzan en la POSICION CERO.
    
    MAS ADELANTE SE COMENT EL TEMA DE LAS LISTAS CON MAS PROFUNDIDAD.
'''
drawTriangle((0,0), 50)
drawSquare((0,0), 50)
drawPentagon((0,0), 50)