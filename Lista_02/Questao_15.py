n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
print("Números informados:")
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n3: {n3}")
if n1 > n2:
    n1, n2 = n2, n1
if n1 > n3:
    n1, n3 = n3, n1
if n2 > n3:
    n2, n3 = n3, n2
print("\nNúmeros ordenados em ordem decrescente:")
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n3: {n3}")