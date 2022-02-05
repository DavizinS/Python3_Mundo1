# Escreva um programa que faça o computador "Pensar" um número inteiro entre 0 a 5 e peça para o usuário descobrir!
# O programa irá escrever na tela se o usuário acertou ou perdeu!
from random import randint
from time import sleep
sorteado = randint(0, 5)
print('\n...Desafio 30...\nO computador pensou em um número de 0 a 5! Tente acertar!')
resp = int(input('Qual número você acha que é o certo? '))
print('PROCESSANDO...')
sleep(3)
if resp == sorteado:
    print('O seu número foi {} e o computador pensou no número: {}'.format(resp, sorteado))
    print('Você acertou!!')
else:
    print('Você errou! Tente novamente!')
    print('Eu pensei no número {} e você no número {}'.format(sorteado, resp))
