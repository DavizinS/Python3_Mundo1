cores = {'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[37m',
         'limpa': '\033[m'}
msg = 'Olá, {}Mundo!{}'
print(msg.format(cores['roxo'], cores['limpa']))
print('No {}futuro\033[m serei {}um\033[m ótimo {}programador!'.format(cores['ciano'], cores['amarelo'], cores['roxo']))
