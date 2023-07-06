# Faça um programa que leia algo pelo teclado e mostre
# na tela o teu tipo primitivo e todas as informações
# possíveis sobre ele.

algo = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(algo))

print(f"só tem espacos? {algo.isspace()}")
print(f"é um numero? {algo.isnumeric()}")
print(f"é alfabético? {algo.isalpha()}")
print(f"é alfanumérico? {algo.isalnum()}")
print(f"está em maiúsculas? {algo.isupper()}")
print(f"está em minusculas? {algo.islower()}")
print(f"está capitalizado? {algo.istitle()}")
