# Leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
# separadamente.
nome = str(input('Digite seu nome: ')).strip().split()
print('Seu primeiro nome é {}'.format(nome[0]).title())
print('Seu ultimmo nome é {}'.format(nome[len(nome)-1]))
