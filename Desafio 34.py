# Escreva um programa que perunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%
salario = float(input('Qual o seu salário? R$ '))

# Condiçonais para aumentar salário
if salario > 1250:
    aumento = salario + (salario * 10) / 100
    print('Seu Salário é de R$ {} e teve um aumento de 10%!'.format(salario))
    print('Agora você recebe: R$ {}'.format(aumento))
else:
    aumento = salario + (salario * 15) / 100
    print('Seu salário é de R$ {} e teve um aumento de 15%!'.format(salario))
    print('Agora você recebe: R$ {:.2f}'.format(aumento))
