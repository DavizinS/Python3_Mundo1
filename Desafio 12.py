altura = float(input('Qual a altura da Parede? '))
largura = float(input('Qual a largura da Parede? '))
dimensao = altura * largura
pintar = dimensao / 2
print('Sua parede tem a dimensão de {} x {} e sua aréa é de {:.3f}m²'.format(altura, largura, dimensao))
print('Para pintar uma parede de {:.3f}m² precisará de {:.2f}L de tinta'.format(dimensao, pintar))