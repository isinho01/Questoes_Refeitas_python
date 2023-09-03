soma = 0
quantidade_numeros = 0
maior_numero = float('-inf')
menor_numero = float('inf')

while True:
    numero = float(input("Digite um número (ou -1 para parar): "))
    
    if numero == -1:
        break
    
    quantidade_numeros += 1
    soma += numero
    
    if numero > maior_numero:
        maior_numero = numero
    
    if numero < menor_numero:
        menor_numero = numero
        
if quantidade_numeros > 0:
    media = soma / quantidade_numeros
    print(f"Quantidade de números digitados: {quantidade_numeros}")
    print(f"Média aritmética: {media}")
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")
else:
    print("Nenhum número foi digitado.")