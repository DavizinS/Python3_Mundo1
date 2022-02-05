# Exercicio 21 - Tocando um MP3 (Curso em Vídeo)

import pygame

print('Tocando agora: Lady Writter - Dire Straits')

pygame.init()
pygame.mixer.music.load('lady.mp3')
pygame.mixer.music.play()
x = input('Pressione enter para encerrar a música.')
