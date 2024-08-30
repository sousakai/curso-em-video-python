n1 = input("Digite o primeiro valor:")
n2 = input("Digite o segundo valor:")
n3 = input("Digite o terceiro valor:")
numeros = [n2, n3, n1]
numeros_ord = sorted(numeros)
print(f"O menor valor é de {numeros_ord[0]}.")
print(f"O maior valor é de {numeros_ord[2]}.")