import turtle

theTurtle = turtle.Turtle()

'''
    Polygon
'''

def drawPolygon(origin, size, sides):
    # Se establece el origen del poligono (x,y).
    theTurtle.goto(origin[0], origin[1])
    # Se establece el grado de inclinación inicial.
    theTurtle.seth(0)
    # Se calcula los grados que se deben girar en cada trazo para dibujar cada lado.
    angle = 360/sides
    
    '''
        El bucle FOR ejecuta las instrucciones que contiene tantas veces como se determine
        en su DEFINICION, se suele utilizar para ITERACIONES en las que se conoce el NUMERO de VECES
        que se quiere REPETIR.
        
        El Método "range()" se utiliza para establecer un RANGO de valores, en este caso determina
        determina el nímero de repeticiones del FOR.
    '''
    for i in range(0, sides):
        # Se dibuja el lado "i" que corresponda
        # Con una longitud de "size".
        # Despues se gira el numero de grados adecuado "angle".
        # Tantas veces como numero de lados tenga al poligono "sides".
        theTurtle.fd(size)
        theTurtle.left(angle)    


def drawTriangle(origin, size):
    # Se invoca la función "drawPolygon()" incluyendo el numero de lados del poligono
    drawPolygon(origin, size, 3)

def drawSquare(origin, size):
    drawPolygon(origin, size, 4)

def drawPentagon(origin, size):
    drawPolygon(origin, size, 5)


drawTriangle((0,0), 50)

drawSquare((0,0), 50)

drawPentagon((0,0), 50)

'''
    Abstraccion que permite dibujar un poligono con n lados
    Aquí n = 6
'''
drawPolygon((0,0), 50, 6)