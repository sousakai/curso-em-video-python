frase = input("Digite a frase desejada:").strip().upper()
print(f"A letra A apareceu {frase.count("A")} vezes.")
print(f"A primeira letra A apareceu na posição {frase.find("A")+1}")
print(f"A última letra A apareceu na posição {frase.rfind("A")+1}")