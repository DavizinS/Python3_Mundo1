# O calculo da raiz quadrada do Cateto oposto e do Cateto adjacente dará o resultado da Hipotenusa
# Formula: (Cateto Oposto ** 2 + Cateto Adjacente ** 2) ** (1/2)
from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
