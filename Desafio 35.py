# Desenvolva um programa que leia os comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triangulo
n1 = float(input('Qual a primeira reta? '))
n2 = float(input('Qual a segunda reta? '))
n3 = float(input('qual a terceira reta? '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos podem formar um triangulo!')
else:
    print('Os segimentos NÃO podem formar um triangulo!')
