# um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = input("1º aluno: ")
a2 = input("2º aluno: ")
a3 = input("3º aluno: ")
a4 = input("4º aluno: ")

lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print(f"O aluno escolhido foi {escolhido}")
