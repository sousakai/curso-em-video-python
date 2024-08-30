salario = float(input("Digite o salário:\n"
                      "R$"))
if salario < 1250:
    aumento_salB = salario * 0.15
    print(f"O salário é de R${aumento_salB + salario:.2f}, com acréscimo de R${aumento_salB:.2f}")
else:
    aumento_salA = salario * 0.10
    print(f"O salário é de R${aumento_salA + salario:.2f}, com acréscimo de R${aumento_salA:.2f}.")
    