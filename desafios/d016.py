''' crie um programa que leia umm número real qualquer
    pelo teclado e mostre na tela sua porção inteira
    exemplo: numero 6.127 tem e porção inteira 6     '''

from math import trunc

numero = float(input("digite um número: "))

# trunc apaga o que tem depois da vírgula
print(f"porção inteira = {trunc(numero)}")
