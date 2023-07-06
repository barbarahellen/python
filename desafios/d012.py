# faça um algoritmo que leia o preço de um produto e
# mostre o seu novo preço com 5% de desconto

preco = float(input("qual é o preço do produto? R$ "))
desconto = preco - (preco * 5 / 100)

print(f"o preço com 5% de desconto fica: {desconto:.2f}")
