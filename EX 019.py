from random import choice as escolha
aluno1 = input("Digite o nome do primeiro aluno:")
aluno2 = input("Digite o nome do segundo aluno:")
aluno3 = input("Digite o nome do terceiro aluno:")
aluno4 = input("Digite o nome do quarto aluno:")
classe = (aluno1, aluno2, aluno3, aluno4)
print(f"O aluno selecionado foi {escolha(classe)}!")

#O comando "as" dá um nome para a função. Em resumo, foi importado a função "choice" da biblioteca random, com outro nome.