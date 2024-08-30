import random
aluno1 = (input("Insira o nome do primeiro aluno:"))
aluno2 = (input("Insira o nome do segundo aluno:"))
aluno3 = (input("Insira o nome do terceiro aluno:"))
aluno4 = (input("Insira o nome do quarto aluno:"))
aluno5 = (input("Insira o nome do quinto aluno:"))
classe = [aluno5, aluno4, aluno3, aluno1, aluno2]
classe_ord = random.sample(classe, len(classe))
print(classe_ord)

#O uso da função len garante que ele irá embaralhar todos os elementos da lista.
