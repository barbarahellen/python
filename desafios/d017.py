# faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa

# from math import sqrt, pow
from math import hypot

catOpo = float(input("Comprimento do cateto oposto: "))
catAdj = float(input("Comprimento do cateto adjacente: "))

# hip = sqrt(pow(catOpo, 2) + (pow(catAdj, 2)))
hip = hypot(catOpo, catAdj)

print(f"A hipotenusa vai medir {hip:.2f}")
