# Ensinamentos da Aula 10! Condições Simples e Compostas
nome = str(input('Digite seu nome: ')).strip().capitalize()
n1 = float(input('Informe sua 1° Nota: '))
n2 = float(input('Informe sua 2° Nota: '))
m = (n1 + n2) / 2
tags = ['ALUNO REGULAR', 'ALUNO BOM', 'ALUNO ÓTIMO', 'ALUNO 10!!', 'PRODIGIO']
print('Analisando Média Escolar do Aluno...\n...\n ...')
if m >= 6:
    print('Sua média escolar está boa! {}! Parabéns'.format(m))
    print('Você ganhou a TAG {}'.format(tags[1]))
else:
    print('Sua média está baixa!! ESTUDE MAIS!! Nota: {}'.format(m))
    print('Você ganhou a TAG {}'.format(tags[0]))
