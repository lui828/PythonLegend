print('BANCO DE CODÉDEX')

pin = int(input('Ingrese su PIN:'))

while pin != 1234:
  pin = int(input('PIN incorrecto. Ingrese su PIN nuevamente: '))

if pin == 1234:
  print('PIN aceptado!')

