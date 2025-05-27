from random import randint

def gerar_cpf():
    numero = str(randint(100000000, 999999999))
    novo_cpf = numero
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1

        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    print(f'CPF Gerado: {novo_cpf}')


def validar_cpf():
    cpf = input('Digite um CPF: ').strip().replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido (formato incorreto).")
        return

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1

        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = cpf == cpf[0] * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')


def menu():
    while True:
        print('\n=== MENU ===')
        print('1 - Gerar CPF')
        print('2 - Validar CPF')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            gerar_cpf()
        elif opcao == '2':
            validar_cpf()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

# Executar o menu
menu()
