km_viagem = float(input("Digite a quilometragem:"))
if km_viagem < 200:
    print(f"Você pagará R${km_viagem * 0.50:.2f}.")
else:
    print(f"Você pagará R${km_viagem * 0.45:.2f}.")
