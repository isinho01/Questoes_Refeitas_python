preco_quilo = 20.00
quantidade_clientes = int(input("Digite a quantidade de clientes na mesa: "))
valor_total_conta = 0

for cliente in range(1, quantidade_clientes + 1):
    peso_prato_gramas = float(input(f"Cliente {cliente}: Digite o peso do prato (em gramas): "))
    valor_bebida = float(input(f"Cliente {cliente}: Digite o valor gasto com bebida: "))
    peso_prato_quilos = peso_prato_gramas / 1000.0
    valor_prato = preco_quilo * peso_prato_quilos
    valor_total_cliente = valor_prato + valor_bebida
    valor_total_conta += valor_total_cliente

print(f"O valor total da conta da mesa é: R$ {valor_total_conta:.2f}")
