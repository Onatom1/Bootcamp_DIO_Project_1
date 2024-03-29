import textwrap

def menu():
    menu = '''
============= MENU =============
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Lista de contas
[6] Novo usuário
[7] Sair
===============================
=> '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('Operação falhou! O valor informado é inválido.')
    
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
        
    if excedeu_saldo and excedeu_limite:
        print('Operação falhou! Saldo e limite insuficientes.')
    elif excedeu_saldo:
        print('Operação falhou! Saldo insuficiente.')
    elif excedeu_limite:
        print('Operação falhou! Limite de crédito atingido.')
    elif excedeu_saques:
        print('Operação falhou! Limite de saques diários atingido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! O valor informado é inválido.')
    
    return saldo, extrato


def mostrar_extrato(saldo, extrato):
    print('\n============= EXTRATO =============')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')
    print('==================================')
    
    
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente os números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Já existe usuário com esse CPF!')
        return

    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
    endereco = input('Endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, "endereco": endereco})
    
    print('===== Usuário criado com sucesso =====')
    
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuário não encontrado, fluxo de criação de conta encerrado!')
    return None
    
def listar_contas(contas):
    print('\n=========== LISTA DE CONTAS ===========')
    for i, conta in enumerate(contas, start=1):
        print(f'Conta {i}: Agência: {conta["agencia"]}, Número: {conta["numero_conta"]}, CPF: {conta["usuario"]["cpf"]}')
    print('========================================')

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        op = menu()
        
        if op == '1':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif op == '2':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
        elif op == '3':
            mostrar_extrato(saldo, extrato)
            
        elif op == '6':
            criar_usuario(usuarios)
        
        elif op == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            
        elif op == '5':
            listar_contas(contas)
            
        elif op == '7':
            print('Saindo...')
            break
        
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()
