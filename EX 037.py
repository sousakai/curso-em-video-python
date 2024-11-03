numero = int(input('Digite o número que você quer converter:\n'))
conversao = int(input('''Digite qual a conversão que você deseja fazer: \n
1 - Binário
2- Octal
3 - Hexadecimal \n'''))
if (conversao == 1):
    print(f'O seu número {numero} em base binária é: \n{bin(numero)[2:]}')    
elif(conversao == 2):
    print(f'O seu número {numero} em base binária é: \n{oct(numero)[2:]}')  
elif(conversao == 3):
    print(f'O seu número {numero} em base binária é: \n{hex(numero)[2:]}')
else:
    print('Opção inválida. Selecione um número de 1 a 3.')  