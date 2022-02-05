dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pdia = (dias * 60) + (km * 0.15)
total = pdia
totaltaxa = total + (total * 9 / 100)
print('O total a pagar é: R$ {}'.format(total))
print('Você pode parcelar o valor em 5x com 9% de taxa')
print('Ficando por {}'.format(totaltaxa))