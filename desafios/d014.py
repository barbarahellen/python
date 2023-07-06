# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input("digite a temperatura em graus ºC: "))

fah = ((temp * 9) / 5) + 32

print(f"a temperatura de {temp} ºC é igual a {fah} ºF")
