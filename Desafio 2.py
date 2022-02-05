cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
nome = input('Qual é o seu nome? ').strip().capitalize()
idade = input('Qual é a sua idade? ')
print('É um prazer te conhecer, {}{} !\033[m {}APTO\033[m a servir!'.format(cores['vermelho'], nome, cores['verde']))
