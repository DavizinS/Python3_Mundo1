# Desafio 24 - Crie um programa que leia o nome de alguma cidade e diga se ela começa ou não com o nome "Santo
cidade = str(input('Em que cidade você Nasceu? ')).strip()
print(bool(cidade[0:5].upper() == 'SANTO'))
