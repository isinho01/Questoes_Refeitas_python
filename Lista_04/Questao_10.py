quantidade_produtos = int(input("Digite a quantidade de produtos que você está comprando: "))
valor_total_compra = 0

for i in range(1, quantidade_produtos + 1):
    preco_produto = float(input(f"Digite o preço do produto {i}: "))
    valor_total_compra += preco_produto

valor_avista = valor_total_compra * 0.95
valor_parcelado = valor_total_compra * 1.002
valor_parcelado /= 3

print(f"Valor total da compra: R$ {valor_total_compra:.2f}")
print(f"Opções de pagamento:")
print(f"1. À vista (5% de desconto): R$ {valor_avista:.2f}")
print(f"2. Parcelado em 3 vezes: 3x de R$ {valor_parcelado:.2f}")
