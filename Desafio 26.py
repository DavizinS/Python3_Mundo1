# Crie um programa que leia uma frase e mostre
# Quantas vezes aparece a letra A (OK)
# Em que posição ela aparece a primeira vez (OK)
# Em que posição ela aparece a ultima vez (OK)
frase = str(input('Diga qualquer coisa: ')).strip().upper()
print('Vezes que a letra "A" apareceu: {}'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição: {}'.format(frase.rfind('A')+1))
