# Um Professor quer sortear um dos seus quatros alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
# Choice - Escolhe alguém da lista

from random import choice
nome1 = input('1° Aluno: ')
nome2 = input('2° Aluno: ')
nome3 = input('3° Aluno: ')
nome4 = input('4° Aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O escolhido para limpar o quadro foi: {}'.format(escolhido))
