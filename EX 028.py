import random, time
chute = int(input("Escolha um número de 0 a 5."))
numero = random.choice(range(0, 6))

#Escolhe um número de 0 a 5. Poderia ser usado o comando randint, que é um número inteiro aleatório.
print("Vamos ver...")

#Mantém o programa em pausa por 3 segundos.
time.sleep(3)

if chute == numero: #Condição que compara o número do usuário e do computador.
    print("Acertou!")
else:
    print(f"Errou feio. Era o número {numero}.")