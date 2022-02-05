# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar a 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada Km acima do limite!
velocidade = float(input('O carro está andando em quantos KM/H ? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('\nATENÇÃO!! ')
    print('Você está andando a {:.1f}KM/H'.format(velocidade))
    print('Acima de 80 KM/H, você está sujeito a multa!')
    print('Você ganhou uma multa de R${:.2f}\n'.format(multa))
else:
    print('\nFIQUE TRANQUILO!\n')
    print('Você está andando na velocidade permitida!')
print('Tenha um bom dia e dirija com segurança!')