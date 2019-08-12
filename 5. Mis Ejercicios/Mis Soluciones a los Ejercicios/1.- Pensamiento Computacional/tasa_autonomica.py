TASA_APLICABLE = 0.055

def tasa_autonomica(precio, provincia):
    # Si se trata de VALENCIA se INCREMENTA el PRECIO
    if provincia == 'VA':
        precio = precio + (precio * TASA_APLICABLE)

    # Se DEVUELVE el PRECIO.
    # Si no es VALENCIA, el PRECIO NO SE HABRA INCREMENTADO.
    return precio

str_precio =    input('Precio..........:')
str_provincia = input('Provincia.......:')

precio = float(str_precio)
print('El subtotal es {:.2f}\nLa tasa SI SE APLICA es {:.2f}\nEl Total es {:.2f}'
        .format(precio, TASA_APLICABLE * precio, tasa_autonomica(precio, str_provincia)))