def interes_compuesto(capital, interes_anual, tiempo, recalculo_interes):
    total_inversion = capital * ((1 + (interes_anual / recalculo_interes))**(recalculo_interes * tiempo))
    return total_inversion

# DATOS DE ENTRADA
str_capital =           input('Capital Inicial..................: ')
str_interes_anual =     input('Interes Anual....................: ')
str_recalculo_interes = input('Recalculos Anuales...............: ')
str_tiempo =            input('Años.............................: ')

# CAMBIOS DE TIPO (STRING --> NUMERICO)
capital =           float(str_capital)
interes =           float(str_interes_anual) / 100
recalculo_interes = int(str_recalculo_interes)
tiempo =            int(str_tiempo)

# INVOCACION de la FUNCION y FORMATEO de la SALIDA
print('El TOTAL de la Inversión al cabo de {} años será de {:.2f}€'.format(tiempo, interes_compuesto(capital, interes, tiempo, recalculo_interes)))


