import mysql.connector
import ConexaoBD #Classe que faz a conexão com o banco de dados
import menu

db_connection = ConexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, preco, quantidade):
    try:
        sql = "insert into item(codigo, nome, preco, quantidade) values('', '{}', '{}', '{}')".format(nome, preco, quantidade)
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def consultar():
    try:
        sql = 'select * from item'
        con.execute(sql)

        for(codigo, nome, preco, quantidade) in con:
            print('Código: {}, Nome: {}, Preço: {}, Quantidade: {}'.format(codigo, nome, preco, quantidade))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update item set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete FROM item WHERE codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def cadastrar(cpf, senha):
    try:
        sql = "insert into login(codigo, cpf, senha) values('', '{}', '{}')".format(cpf, senha)
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def loginCpfSenha(CPFDigitado, senhaDigitada):
    try:
        sql = 'select * from login'
        con.execute(sql)
        for (codigo, cpf, senha) in con:
            if cpf == CPFDigitado and senha == senhaDigitada:
                return True
            else:
                print('\n')
                return False

    except Exception as erro:
        print(erro)


def login(cpf, senha):
    try:
        if loginCpfSenha(cpf, senha) == True:
            print('Logado com Sucesso !')
            print('\n')
            menu.operacao()
        else:
            print('Login e Senha incorretos!')
            print('\n')
    except Exception as erro:
        print(erro)

