numero_personas = input('Cuantas personas somos?:')
numero_pizzas = input('Cuantas pizzas han traido?:')

num_personas = int(numero_personas)
num_pizzas = int(numero_pizzas)

if num_personas % 2 == 0:
    porciones_pizza = num_personas
else:
    porciones_pizza = num_personas + 1


porciones_sobran = (num_pizzas * porciones_pizza) % num_personas
porciones_persona = (num_pizzas * porciones_pizza) // num_personas

print('Cada persona tomara {} porciones de pizza y sobraran {} porciones'.format(porciones_persona, porciones_sobran))

