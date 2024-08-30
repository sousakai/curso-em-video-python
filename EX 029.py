km = float(input("Qual a sua velocidade?"))
if km <= 80:
    print("Parabéns. Dirija com segurança.")
else:
    print(f"Você ultrapassou o limite de segurança na via.\n"
          f"Receberá uma multa de R${(km - 80) * 7:.2f}")
