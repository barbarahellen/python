# faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário com 15% de aumento

salario = float(input("salário = "))
novo = salario + (salario * 15 / 100)

print(f"o salário com aumento fica: {novo:.2f}")
