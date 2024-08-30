cidade = input("Digite a sua cidade:").strip()
#Retira os espaços extras no início e fim das palavras.
print(cidade[:5].upper() == "SANTO")

# Verifica, dentro da própria função print, sem usar if e else, se equivale a "SANTO" o início da cidade.

# A função :5 define um limite de caracteres. Nesse caso, apenas o suficiente da palavra SANTO.

# Definimos como upper, para que o programa consiga comparar o input com a palavra que lhe foi dada
# independentemente de como o usuário digitar.