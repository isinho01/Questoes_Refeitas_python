n = int(input("Digite o valor de n: "))

soma = 0

for i in range(1, n + 1):
    termo = 1 / i
    soma += termo

print(f"A soma da série é igual a {soma}")
