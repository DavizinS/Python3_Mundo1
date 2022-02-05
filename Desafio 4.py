n1 = int(input('Digite o 1° Valor: '))
n2 = int(input('Digite o 2° Valor: '))
n3 = int(input('Digite o 3° Valor: '))
Soma = n1 + n2 + n3
Media = Soma / 3
print('\033[1;31mA soma do valor\033[m {}, {} e {} é igual a: \033[1;36m{}\033[m'.format(n1, n2, n3, Soma))
print('\033[1;31mA média aritmética Dos Valores\033[m {}, {}, {}, é de {:.2f}'.format(n1, n2, n3, Media))

