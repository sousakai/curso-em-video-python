import math
num = int(input("Digite o número:"))
raiz = math.sqrt(num)
print(f"A raíz de {num} é de {math.ceil(raiz)}")

# É necessário usar math.sqrt, pois nesse caso foi importado toda a biblioteca math. Se fosse utilizado o comando from math import sqrt, apenas digitar sqrt resolveria o problema.