'''
    PROGRAMACION ORIENTADA A OBJETOS (POO)
    
    Un OBJETO es una porcion de codigo que tiene ESTADO y COMPORTAMIENTO.
    Es la FORMA de ENCAPSULAR CODIGO MAS COMPLETA.
    
    Un OBJETO tiene DOS características principales:
        - La CLASE de OBJETO:
            Porción de CODIGO capaz de CREAR INSTANCIAS de si misma que MANTIENEN CADA UNA su ESTADO
            y realizan FUNCIONES INDEPENDIENTES unas de otras.
            
        - El OBJETO(INSTANCIA) propiamente dicho:
            Será CADA una de las INSTANCIAS existentes de una CLASE.
'''
'''
    VENTAJAS y NECESIDAD de los OBJETOS
    
    VENTAJAS:
        - Los OBJETOS permiten REUTILIZAR CODIGO.
        
        - Los OBJETOS permiten ENCAPSULAR FUNCIONALIDADES.
            
            FUNCIONALIDADES ESPECIFICAS en OBJETOS ESPECIFICOS:
                - Presentación y Entrada de Datos x Pantalla.
                - Acceso a Ficheros y Bases de Datos.
                - Logica de los Datos.
                
            Lo que se CONOCE COMO el MODELO MVC o MODELO, VISTA, CONTROLADOR.
            
        - Los OBJETOS facilitan la MODIFICACIÓN y el MANTENIMIENTO.
    
    NECESIDAD:
        - Los OBJETOS permiten la CONSTRUCCION y MANTENIMIENTO de APLICACIONES MUY COMPLEJAS, con MUCHOS COMPONENTES.
'''
'''
    OBJETOS(INSTANCIAS) y CLASES:
    
        - CLASE: MOLDE o PROTOTIPO, BLOQUE de CODIGO que define TODAS sus FUNCIONALIDADES y las VARIABLES que DETERMINAN su ESTADO.
        
            - METODOS: FUNCIONES que un OBJETO puede realizar.
            - ATRIBUTOS: VARIABLES que determinan el ESTADO de la INSTANCIA del OBJETO.
    
'''
# DEFINICION de la CLASE Gato
class Gato():
    
    # CONSTRUCTOR de la CLASE Gato
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    # METODO de la CLASE Gato
    def maullar(self):
        print('El Gato {} está Maullando'.format(self.nombre))

# Se CREAN INSTANCIAS del OBJETO Gato.
mi_gato = Gato('Riku', 3, 5)
tu_gato = Gato('Silluka', 5, 4)

# Se utiliza el METODO maullar de CADA uno de los GATOS
mi_gato.maullar()
tu_gato.maullar()

'''
    EL CONSTRUCTOR(METODO) DE UN OBJETO
    
    El METODO __init__() es OBLIGATORIO en la CREACION de una CLASE y se deomina CONSTRUCTOR.
    
    Es la FUNCION que permite a una CLASE la CREACION de NUEVAS INSTANCIAS e INICIALIZARLAS con un ESTADO DETERMINADO.
    
'''
'''
    IMPRIMIENDO UNA CLASE
    
    Para "IMPRIMIR" UNA CLASE se utiliza el METODO __str__() en el que se puede definir COMO SE QUIERE QUE SE MUESTRE la CLASE 
'''
class Perro():
    def __init__(self, nombre):
        self.nombre = nombre
    
    # El METODO __str__() permite definir COMO se MUESTRA la CLASE cuando se IMPRIME
    def __str__(self):
        # Se DEVUELVE COMO QUEREMOS QUE SE REPRESENTE la CLASE
        return('Esta es una INSTANCIA de la Clase Perro y define un ATRIBUTO "nombre" con el valor: {}'.format(self.nombre))
    
un_perro = Perro('Rex')

# Cuando se utiliza el METODO print() sobre una CLASE, se INVOCA el METODO __str__().
print(un_perro)

'''
    METODOS y ATRIBUTOS
    
        - METODOS: Los METODOS de una CLASE son las FUNCIONES PROPIAS de esa CLASE.
            - DEBEN INCLUIR NECESARIAMENTE un PRIMER PARAMETRO 'self'.
            - Cuando se INVOCAN DEBE hacerse ASOCIADO a la INSTANCIA de su CLASE.
        
        - ATRIBUTOS: Son las VARIABLES PROPIAS de la CLASE y DEFINEN en ESTADO de una INSTANCIA. Se puede ACCEDER a ellos y MODIFICARLOS:
            - ACCESO: nombre_instancia.nombre_atributo
            - MODIFICACION: nombre_instancia.nombre_atributo = valor
        
        ES MUY RECOMENDABLE NO PERMITIR EL ACCESO y MODIFICACION DIRECTA de los ATRIBUTOS. Se DEBEN IMPLEMENTAR METODOS ESPECIFICOS:
            - Metodo GET para el ACCESO
            - Metodo SET para la MODIFICACION
'''
class Coche():
    def __init__(self, marca):
        self.marca = marca
        
un_coche = Coche('Ferrari')

# Se puede ACCERDER al VALOR de un ATRIBUTO de una CLASE.
print('La marca del coche creado es: {}'.format(un_coche.marca))

# Se puede MODIFICAR el VALOR de un ATRIBUTO de una CLASE.
un_coche.marca = 'Porche'


print('La marca del coche creado es: {}'.format(un_coche.marca))

'''
    HERENCIA
    
    Es posible CREAR CLASES que HEREDEN de otras CLASES de forma que estas nuevas CLASES MANTENDRAN los ATRIBUTOS y METODOS de la CLASE PADRE
    y pueden incluir NUEVOS METODOS y ATRIBUTOS (CLASE HIJA)
    
    SOBREESCRITURA de METODOS
    
    Las CLASES HIJAS pueden SOBREESCRIBIR los METODOS que HEREDA de la CLASE PADRE para AJUSTARLOS a SUS NECESIDADES
    
'''
class CocheAlquiler(Coche):
    # CONSTRUCTOR de una CLASE HIJA
    def __init__(self, marca, precioHora):
        # Se INVOCA al CONSTRUCTOR de la CLASE PADRE
        Coche.__init__(self, marca)
        # Se COMPLETA con los ATRIBUTOS PROPIOS de la CLASE HIJA
        self.precioHora = precioHora
    
    def __str__(self):
        return 'La Marca del coche es {} y cuesta {}€ al dia'.format(self.marca, self.precioHora)

un_coche_alquilado = CocheAlquiler('Seat', 50)

print(un_coche_alquilado)

'''
    POLIMORFISMO
    
    OBJETOS DISTINTOS COMPARTEN METODOS con la MISMA SINTAXIS(CON LOS MISMOS PARAMETROS) pero realizan FUNCIONES DISTINTAS.
'''
class Figura():
    def __init__(self, base, altura = None):
        self.base = base
        self.altura = altura
    
    # Se CREA LA DEFINICION de los METODOS en la CLASE PADRE pero NO SE IMPLEMENTAN    
    def area(self):
        pass

# HEREDAMOS de la CLASE Figura
class Triangulo(Figura):
    
    def __init__(self, base, altura = None):
        Figura.__init__(self, base, altura)
        
    def area(self):
        return (self.base * self.altura) / 2

# HEREDAMOS de la CLASE Figura
class Cuadrado(Figura):
    
    def __init__(self, base, altura = None):
        Figura.__init__(self, base, altura)
        
    def area(self):
        return (self.base ** 2)

un_triangulo = Triangulo(2, 3)
un_cuadrado = Cuadrado(3)

print('El Area del Triangulo es: {}'.format(un_triangulo.area()))
print('El Area del Cuadrado es: {}'.format(un_cuadrado.area()))