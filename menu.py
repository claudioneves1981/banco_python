
import textwrap
from deposito import Deposito
from saque import Saque
from pessoafisica import PessoaFisica
from contacorrente import ContaCorrente

def menu(): 
    menu = """\n
    =================Menu=================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    =>"""

    return input(textwrap.dedent(menu))

def filtrar_clientes(clientes, cpf):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nO cliente não possui contas.")
        return
    #FIXME: Não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n=============== Extrato ================")

    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}\tR$ {transacao['valor']:.2f}\n"
    
    print(extrato)
    print(f"Saldo:\tR$ {conta.saldo:.2f}")
    print("=======================================")
    
    
def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(clientes, cpf)

    if cliente:
        print("\nJá existe um cliente com esse CPF.")
        return
    
    nome = input("Informe o nome completo do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente (dd-mm-aaaa): ")
    endereco = input("Informe o endereço do cliente: ")

    cliente = PessoaFisica(nome =nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\nCliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(clientes, cpf)
    
    if not cliente:
        print("\nCliente não encontrado.")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("\n" + "-"*100)
        print(textwrap.dedent(str(conta)))

    
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            criar_conta(len(contas)+1, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'q':
            print("\nObrigado por usar nosso sistema bancário!")
            break
        else:
            print("\nOpção inválida. Por favor, selecione uma opção válida.")

main()