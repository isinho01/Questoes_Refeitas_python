n = int(input("Digite um número para ver a sua tabuada de multiplicação: "))
print(f"Tabuada de multiplicação de {n}:")
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")