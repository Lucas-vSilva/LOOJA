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
