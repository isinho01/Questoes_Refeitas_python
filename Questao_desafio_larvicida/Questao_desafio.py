comprimento = float(input("por favor informe a comprimento: "))
largura = float(input("por favor informe a largura: "))
altura = float(input("por favor informe a altura: "))
print("lembrando que todas as medidas devem ser em cm")

volume = (largura * altura * comprimento)
print(f"o volume calculado é {volume}")
capacidade = volume/1000
print(f"sua capacidade em litros é {capacidade}")
larvicida = capacidade/1000
print(f"a quantidade de larvicida a ser usada é: {larvicida:.2f} gramas ")