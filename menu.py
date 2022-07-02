import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ''

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
            #resp = str(input('Deseja continuar [S/N]'))
            #if resp in 'N':
                #break
            #elif resp in 'S':
                #return (this.opcao == 1):

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