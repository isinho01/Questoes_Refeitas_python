m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))
if m > n:
    m, n = n, m
print(f"Números no intervalo entre {m} e {n}:")
for numero in range(m, n + 1):
    print(numero)