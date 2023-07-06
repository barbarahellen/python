# Sempre que algo é lido só com o input, ele é considerado string
# Para alterar esse tipo, precisa-se colocar ele antes do input

n = input("digite algo: ")
print(n.isnumeric())
print(n.isupper())
print(n.isalpha())
