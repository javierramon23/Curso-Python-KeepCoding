YARDA_CUADRADA = 1.19599

ancho = input('Ancho de la habitacion?(m): ')
profundo = input('Profundidad de la habitacion?(m): ')

superficie_metros = round(float(ancho) * float(profundo), 2)
superficie_yardas = round(superficie_metros * YARDA_CUADRADA, 2)

print('La superficie de la habitación es de {} m2'.format(superficie_metros))
print('La superficie de la habitación es de {} yd2'.format(superficie_yardas))