# Operadores Aritméticos

# Adição: +
# ex: 5 + 2 == 7
# Subtração:
# ex: 5 - 2 == 3
# Multiplicação: *
# ex: 5 * 2 == 10
# Divisão: /
# ex: 5 / 2 = 2.5
# Potência: **
# ex: 5 ** 2 == 25
# Divisão inteira: //
# ex: 5 // 2 == 2
# Resto da divisão ou módulo: %
# ex: 5 % 2 == 1


# Ordem de precedência:

# 1º: ()
# 2º: ** (potência)
# 3º: * / // % (multiplicação, divisão, divisão inteira e resto da divisão)
# 4º: + - (adição e subtração)

print(49**(1/2))  # raiz quadrada
print(125**(1/3))  # raiz cúbica

n1 = int(input("um valor: "))
n2 = int(input("outro valor: "))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
exp = n1 ** n2

print(f"a soma é {soma}, o produto é {mult} e a divisão é {div:.2f}")
print(f"divisão inteira {divint} e potência {exp}")
