from math import sqrt
cateto = float(input("Digite o valor do cateto (largura):\n"))
cateto_adj = float(input("Digite o valor do cateto adjacente (altura):\n"))
hipotenusa_1 = (cateto ** 2) + (cateto_adj ** 2)
resultado = sqrt(hipotenusa_1)
print(f"O triângulo retângulo de cateto {cateto} e de cateto adjacente {cateto_adj} possui a hipotenusa de valor {resultado:.2f}.")
