# Desafio 16 - Curso em Video
# Crie um programa que leia um número real qualquer pelo teclado e ostre na tela a sua porção inteira
# Ex: Digite um número: 6.127 tem a parte inteira 6
# from math import trunc
num = float(input('Digite um número: '))
print('O valor inteiro de {} é {:.0f}'.format(num, int(num)))
