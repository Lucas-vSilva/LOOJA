import mysql.connector
import ConexaoBD #Classe que faz a conexão com o banco de dados

db_connection = ConexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, preco, quantidade):
    try:
        sql = "insert into itens(codigo, nome, preço, quantidade) values('', '{}', '{}', '{}')".format(nome, preco, quantidade)
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def consultar():
    try:
        sql = 'select * from itens'
        con.execute(sql)

        for(codigo, nome, preco, quantidade) in con:
            print('Código: {}, Nome: {}, Preço: {}, Quantidade: {}'.format(codigo, nome, preco, quantidade))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update itens set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete FROM itens WHERE codigo = '{}'".format(cod)
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

def loginCpf(CPFDigitado):
    try:
        sql = 'select cpf from login'
        con.execute(sql)

        for (codigo, cpf, senha) in con:
            if CPFDigitado == cpf:
                return True
        return False
    except Exception as erro:
        print(erro)


def loginSenha(senhaDigitada):
    try:
        sql = 'select senha from login'
        con.execute(sql)

        for(codigo, cpf, senha) in con:
            if senhaDigitada == senha:
                return True
        return False
    except Exception as erro:
        print(erro)


