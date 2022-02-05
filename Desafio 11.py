# Faça um algoritmo que leia um preço e mostre seu novo preço com desconto de 5%
produto = float(input(('Qual foi o seu salário desse mês? € ')))
porc = produto * 20 / 100
novo = porc
npreco = produto - (porc)
print('Imposto descontado do salário será €{:.2f}, Você receberá no salário bruto €{:.2f}'.format(novo, npreco))
