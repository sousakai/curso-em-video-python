from math import sqrt
cat_oposto = float(input("Digite o valor do cateto oposto:"))
cat_adj = float(input("Digite o valor do cateto adjacente:"))
hipotenusa = cat_oposto ** 2 + cat_adj ** 2
print(f"A hipotenusa é de {sqrt(hipotenusa):.2f}.")
# Também existe a função math.hypot(), onde você apenas indica os catetos e o cálculo é automático.
