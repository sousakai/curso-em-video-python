produto = float(input("Digite o valor do produto:"))
desconto = float(input("Digite o valor do desconto (em porcentagem):"))
valor_desconto = desconto /100
desconto_produto = valor_desconto * produto
produto_final = produto - desconto_produto
print(f"O desconto foi de R${desconto_produto} e o valor final do produto é de R${produto_final}") 
## O exercício original solicita um código onde o desconto sempre será de 5%. Aqui, o valor é inserido pelo usuário. 

