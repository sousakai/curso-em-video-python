salario= float(input("Qual o salário do funcionário?\n"))
aumento = float(input("Digite o valor do aumento(em porcentagem):\n"))
valor_aumento = aumento /100
aumento_salarial = valor_aumento * salario
salario_final = salario + aumento_salarial
print(f"O salário do funcionário será: {salario_final}, com acréscimo de {aumento_salarial}.")


