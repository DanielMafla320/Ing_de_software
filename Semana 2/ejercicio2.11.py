tamaño_piscina = float(input('Introduce el valor en metros cubicos de agua consuimido: '))
valor_metro_cubico = float(input('Introduce el valor de la tarifa por cada metros cubicos de agua consuimido: '))
pago = tamaño_piscina * valor_metro_cubico
print('El valor del pago por', float(tamaño_piscina),'metros cubicos es de $', int(pago), 'pesos.')