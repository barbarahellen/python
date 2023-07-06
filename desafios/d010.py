# crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar
# considere US$ 1,00 = R$ 3,27

valor = float(input("quanto você tem na carteira? "))

dolar = valor/3.27

print(f"você pode comprar {dolar:.2f} dólares")
