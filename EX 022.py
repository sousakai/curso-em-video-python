nome = input("Digite seu nome:").strip()
primeiro_nome = nome.split()
print(f"Seu nome em letras maiúsculas é de {nome.upper()};")
print(f"Seu nome em letras minúsculas é de {nome.lower()};")
print(f"Seu nome ao todo possui {len(nome) - nome.count(" ")} letras;")
print(f"Seu primeiro nome é {primeiro_nome[0]}, e possui {len(primeiro_nome[0])} letras.")

#Importante lembrar da função - nome.count(" "), que retira da contagem os espaços em branco.