from math import sin, cos, tan, radians
angulo = (float(input("Digite o ângulo que você deseja calcular:")))
print(f"O seu ângulo de {angulo}, possui:\n"
      f"O seno de {sin(radians(angulo)):.2f};\n"
      f"O cosseno de {cos(radians(angulo)):.2f};\n"
      f"A tangente de {tan(radians(angulo)):.2f};\n")
