fluxo_carteira = []

print("----------------")
print("@ Fluxo da carteira")
print("1 - Adicionar algum valor")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")

def adicionar_transacao(tipo):
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    
    # Se for despesa, o valor será negativo
    if tipo == 2:
        valor = -valor

    fluxo_carteira.append({
        "nome": nome,
        "valor": valor
    })

while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        adicionar_transacao(1)  # Tipo 1 para adicionar valor
    elif opcao == 2:
        adicionar_transacao(2)  # Tipo 2 para adicionar despesa
    else:
        break

# Cálculo do saldo
total = 0
for fc in fluxo_carteira:
    print("Nome:", fc['nome'], "Valor: R$", fc['valor'])
    total += fc['valor']

print("Saldo atual: R$", total)