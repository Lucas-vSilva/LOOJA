import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ''
this.opcao1 = -1
def menu():
    print('\nEscolha uma das opções abaixo:  \n\n' +
          '1. Cadastrar \n'                        +
          '2. Consultar \n'                        +
          '3. Atualizar Nome\n'                    +
          '4. Atualizar Preço\n'                   +
          '5. Atualizar Quantidade\n'              +
          '6. Deletar\n'                           +
          '0. Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe o nome: ')
            nome = input()
            print('Informe o preço: ')
            preco = input()
            print('Informe a quantidade: ')
            quantidade = input()
            operacoes.inserir(nome, preco, quantidade)
        elif this.opcao == 2:
            #print('Informe o codigo que deseja consultar:')
            #this.codigo = int(input())
            operacoes.consultar()
        elif this.opcao == 3:
            print('Informe o codigo que deseja atualizar:')
            this.codigo = int(input())
            print('Informe o novo nome:')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print('Informe o codigo que deseja atualizar:')
            this.codigo = int(input())
            print('Informe o novo preço:')
            this.campo = float(input())
            operacoes.atualizar(this.codigo, 'preco', this.campo)
        elif this.opcao == 5:
            print('Informe o codigo que deseja atualizar:')
            this.codigo = int(input())
            print('Informe o nova quantidade:')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'quantidade', this.campo)
        elif this.opcao == 6:
            print('Informe o codigo que deseja deletar')
            this.codigo = int(input())
            operacoes.excluir(this.codigo)
    else:
        print('Opção escolhida não é válida!')

def menu1():
    print('\nEscolha uma das opções abaixo:  \n\n' +
          '1. Cadastrar Login \n'                  +
          '2. Login \n'                            +
          '0. Sair\n')
    this.opcao1 = int(input())

def operacao1():
        while (this.opcao1 != 0):
            menu1()
            if this.opcao1 == 1:
                print('Informe o CPF: ')
                cpf = input()
                print('Informe a Senha: ')
                senha = input()
                operacoes.cadastrar(cpf, senha)
            elif this.opcao1 == 2:
                print('Insira o CPF:')
                this.cpf = int(input())
                print('Insira a Senha:')
                this.senha = input()
                operacoes.loginCpf()
                operacoes.loginSenha()
                operacao()
        else:
            print('Opção escolhida não é válida!')
        operacao()