# Faça um programa que leia um ano qualquer
# e mostre se ele é BISSEXTO
from datetime import date
ano = int(input('Que ano você deseja analisar? Coloque 0 Para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano Bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto!'.format(ano))
print('By Davizera')
