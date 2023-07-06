# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = float(input("quantos dias alugados? "))
km = float(input("Quantos km percorridos? "))

valor = (km * 0.15) + (60 * dias)

print(f"o valor a pagar será de R$ {valor:.2f}")
