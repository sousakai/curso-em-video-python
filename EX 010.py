valor = float(input("Digite o seu valor em reais:"))
dol = valor / 5.57
eur = valor / 6.07
print(f"Com o seu valor de R${valor}, você pode comprar:\n {dol:.2f} dólares;\n {eur:.2f} euros.")