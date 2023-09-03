angulo = float(input("Digite um ângulo em graus: "))
if 0 <= angulo < 90:
    quadrante = "primeiro quadrante"
elif 90 <= angulo < 180:
    quadrante = "segundo quadrante"
elif 180 <= angulo < 270:
    quadrante = "terceiro quadrante"
elif 270 <= angulo < 360:
    quadrante = "quarto quadrante"
else:
    quadrante = "fora do intervalo de 0 a 360 graus"
print(f"O ângulo de {angulo} graus está no {quadrante}.")