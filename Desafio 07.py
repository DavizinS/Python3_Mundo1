# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média!
aluno = input('Digite o nome do Aluno: ')
nota1 = float(input('Informe a 1° Nota do Aluno: '))
nota2 = float(input('Informe a 2° Nota do Aluno: '))
media = (nota1 + nota2) / 2
print('\033[1;31m=\033[m'*20)
print('Desafio 07 - Curso em Video')
print('\033[1;31m='*20)
print('\033[1;34mA média escolar do aluno: {}, é de: {:.1f}'.format(aluno, media))