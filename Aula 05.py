n = input('Digite alguma coisa: ')
print('\033[1;31mO Tipo primitivo desse valor é: ', type(n))  # Vermelho
print('\033[1;32É númerico? {}'.format(n.isnumeric()))  # Verde
print('\033[1;33mÉ AlfaNúmerico? {}'.format(n.isalnum()))  # Amarelo
print('\033[1;34mÉ Alfabético? {}'.format(n.isalpha()))  # Azul
print('\033[1;35mEstá em Maiúsculo? {}'.format(n.isupper()))  # Roxo
print('\033[1;36mEstá em minúsculo? {}'.format(n.islower()))    # Azul Ciano
print('\033[1;37mSó tem espaços? {}'.format(n.isspace()))   # Cinza
print('\033[mEstá capitalizada? {}'.format(n.istitle()))
