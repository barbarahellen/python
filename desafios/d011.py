# faça um programa que leia a largura e a altura de uma parede em metros
# e calcule sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2


largura = float(input("digite a largura da parede (em metros): "))
altura = float(input("digite a altura da parede (em metros): "))

area = largura * altura
tinta = area/2
print(f"sua parede tem a área de {area} m^2")
print(f"serão necessários {tinta:.2f} litros de tinta para pintá-la")
