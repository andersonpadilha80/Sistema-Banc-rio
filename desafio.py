menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

valor_deposito = 0
valor_saque = 0


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Déposito efetuado com sucesso!")
        else:
            print("Valor de depósito incorreto, tente novamente.")



    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        if valor_saque < 0:
            print("Valor de saque incorreto, tente novamente.")
        elif saldo < valor_saque:
            print("Saldo insuficiente para saque.")
        elif valor_saque > limite:
            print("Você exedeu o limite máximo por saque")
        else:
            while numero_saques < LIMITE_SAQUES:
                numero_saques += 1
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print("Saque realizado com sucesso!")
                break
            else:
                print("Você exedeu seu limite de saques diários.")
            



    elif opcao == "e":
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================================")



    elif opcao == "q":
        break



    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
