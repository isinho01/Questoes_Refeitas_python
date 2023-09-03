def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros_primos = []
numero = 2

while len(numeros_primos) < 50:
    if eh_primo(numero):
        numeros_primos.append(numero)
    numero += 1

print("Os 50 primeiros números primos são:")
for primo in numeros_primos:
    print(primo, end=" ")
