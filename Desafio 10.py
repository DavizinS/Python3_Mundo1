# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos DOL ela pode comprar
# Dollar está 5,54
dollar = 5.54
money = float(input('Quanto de dinheiro você tem na carteira? R$ '))
conv = money / dollar
print('\033[33m='*20)
print('\033[1;32mDesafio 10 - Curso em Vídeo')
print('\033[33m='*20)
print('')
print('\033[32mSe você converter seu dinheiro em dollar você terá {:.2f} US$!'.format(conv))
