# Desenvolva o programa que pergunte a distância de uma viagem em KM
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
# e R$ 0,45 para viagens mais longas.
distancia = float(input('Quantos KM você deseja viajar? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O preço da passagem para uma viagem de {:.2f}km é de R$ {:.2f}'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('O preço da passagem para uma viagem de {:.2f}km é de R$ {:.2f}.'.format(distancia, passagem))
