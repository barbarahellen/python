# Trabalhando com Módulos

# Utiliza-se o comando import algumabiblioteca para importar todas
# as funcionalidades de uma biblioteca que são necessárias para o programa.
# Para importar parte da biblioteca, utiliza-se:
# from algo import algumacoisa

# import math

from math import sqrt, floor

# exemplos de funções:
# ceil - arredonda um número para cima
# floor - arrendonda um número para baixo
# trunc - trunca um número, elimina da vírgula pra frente
# pow - potência
# sqrt - calcula a raíz quadrada
# factorial - calcula o fatorial de um número

num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raíz de {num} é igual a {floor(raiz)}")
