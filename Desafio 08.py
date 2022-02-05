# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros
# KM / HM / DAM / M / DM / CM / MM
metro = float(input('Quantos metros: '))
dcm = metro * 10
cent = metro * 100
mili = metro * 1000
km = metro / 1000
hm = metro / 100
dam = metro / 10
print('='*20)
print('Desafio 08 - Curso em Vídeo')
print('='*20)
print('\033[35m{}m metros são {:.0f}cm e {:.0f} em milímetros'.format(metro, cent, mili))
print('\033[31m{}m metros são {}km, {} Hectometro e {} Decametro'.format(metro, km, hm, dam))
