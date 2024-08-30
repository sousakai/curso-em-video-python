num = int(input("Digite o número:"))
print(f"O número possui {num // 1 % 10} unidades.")
print(f"O número possui {num // 10 % 10} dezenas.")
print(f"O número possui {num // 100 % 10} centenas.")
print(f"O número possui {num // 1000 % 10} milhares.")

#Essa solução funciona usando uma solução matemática.


#num = input("Digite o número:")
#print(f"O número possui {num[3]} unidades.")
#print(f"O número possui {num[2]} dezenas.")
#print(f"O número possui {num[1]} centenas.")
#print(f"O número possui {num[0]} milhares.")

#Essa solução funciona apenas se o número inserido for de 4 dígitos. Menos que isso, o código quebra.
