# Aunque en Python NO EXISTEN las CONSTANTES como tal.
# Por CONVENIO, una VARIABLE en MAYUSCULAS, se considera una CONSTANTE.
METRO_A_YARDA = 1.19599
YARDA_A_METRO = 0.83612

tipo_medida = input('Selecciona la unidad de medida(m2/yd2): ')

if tipo_medida == 'm2' or tipo_medida == 'yd2':
    
    ancho = input('Ancho de la habitacion?(m): ')
    profundo = input('Profundidad de la habitacion?(m): ')

    if not ancho.isdigit() or not profundo.isdigit():
        print('Alguna de las medidas introducidas no es valida, vualve a intentarlo')
    else:
        superficie = float(ancho) * float(profundo)
        if tipo_medida == 'm2':
            superficie_m2 = superficie
            superficie_yd2 = superficie * METRO_A_YARDA

            print('Superficie en m2: {} | Superficie en yd2: {}'.format(superficie_m2, superficie_yd2))
        elif tipo_medida == 'yd2':
            superficie_yd2 = superficie
            superficie_m2 = superficie * YARDA_A_METRO

            print('Superficie en m2: {} | Superficie en yd2: {}'.format(superficie_m2, superficie_yd2))
else:
    print('La UNIDAD de MEDIDA seleccionada NO ES VALIDA.')
    




