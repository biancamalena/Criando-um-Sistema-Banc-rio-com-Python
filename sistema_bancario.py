saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""
    ===== MENU =====
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
    
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor do depósito deve ser positivo.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))

        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500.00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor do saque deve ser positivo.")

    elif opcao == 'e':
        print("\n======= EXTRATO =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("========================")

    elif opcao == 'q':
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, escolha uma opção válida.")