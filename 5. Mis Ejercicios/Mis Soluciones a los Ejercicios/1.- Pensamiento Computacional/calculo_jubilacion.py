# Se IMPORTA el MODULO "time" para trabajar con FECHAS(Objetos Tipo FECHA)
import datetime

edad = input('Cuantos años tienes?: ')
edad_jubilacion = input('A que edad vas a jubilarte?: ')

anyos_restantes = int(edad_jubilacion) - int(edad)

print('Te quedan {} años para jubilarte.'.format(int(edad_jubilacion) - int(edad)))

'''
FECHAS en Python:
Para conseguir la FECHA del SISTEMA y TRABAJAR con FECHAS se utilizan los distintos METODOS del MODULO "datetime"
El METODO "datetime.now()" DEVUELVE la FECHA ACTUAL COMPLETA(YYYY-MM-DD hh:mm:ss).
'''
# El TIPO de DATO que DEVUELVE "now()" es un OBJETO de CLASE "datetime"
fecha_actual = datetime.datetime.now()
# Para OBTENER el AÑO podemos ACCEDER AL ATRIBUTO "year" del OBJETO DEVUELTO
anyo_actual = fecha_actual.year

print('Estamos en {}, te jubilaras en {}'.format(anyo_actual, anyo_actual + anyos_restantes))