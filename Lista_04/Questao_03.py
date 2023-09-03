def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Digite a quantidade de números que deseja verificar: "))
numeros = []

for _ in range(n):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

primos = 0
nao_primos = 0

for numero in numeros:
    if eh_primo(numero):
        primos += 1
    else:
        nao_primos += 1

print(f"Quantidade de números primos: {primos}")
print(f"Quantidade de números não primos: {nao_primos}")
