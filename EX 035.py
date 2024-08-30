seg_1a = input("Digite o primeiro lado:")
seg_2b = input("Digite o segundo lado:")
seg_3c = input("Digite o terceiro lado:")
if (
    seg_1a < seg_2b + seg_3c
    and seg_2b < seg_1a + seg_3c
    and seg_3c < seg_1a + seg_2b
):
    print("Pode formar triângulo.")
else:
    print("Não forma triângulo.")
