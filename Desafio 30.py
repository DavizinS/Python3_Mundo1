# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR OU IMPAR
num = int(input('Digite número: '))

if num % 2 == 0:
    print('O número {}, é um número PAR'.format(num))
else:
    print('O número {}, é um número ÍMPAR!'.format(num))
