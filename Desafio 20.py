# Shuffle (Mistura as ordens)

from random import shuffle, choice

n1 = str(input('1° Aluno: '))
n2 = str(input('2° Aluno: '))
n3 = str(input('3° Aluno: '))
n4 = str(input('4° Aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será!')
print(lista)
escolhido = choice(lista)
print('Quem não precisará se apresentar será: {}'.format(escolhido))
