import mysql.connector
con = mysql.connector.connect(host='localhost',database='teste',user='root',password='nHH36232585@')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

mycursor = con.cursor()

def inserir_tabela(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Registro Inserido")
    except:
        print("Registro Não Inserido")

def inserir_tabela2(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Registro Inserido")
    except:
        print("Registro Não Inserido")

def inserir_tabelas():
   op = 0
   while(op !=10):
     op =int (input("Digite a opção desejada. Aperte\n 1: Inserir dados na cinema 2: Para inserir dados na tabela sala. 10: Para voltar para o menu"))
     if(op ==1):
        nome = input("Digite seu nome ")
        sobrenome = input("Digite seu endereco ")
        insere="INSERT INTO clientes (nome, sobrenome)VALUES('"+nome+"','"+sobrenome+"')"
        inserir_tabela(mycursor,insere)
     if(op == 2):
         nome = input("Digite seu nome ")
         sobrenome = input("Digite seu endereco ")
         insere="INSERT INTO funcionario (nome, sobrenome)VALUES('"+nome+"','"+sobrenome+"')"
         inserir_tabela2(mycursor,insere)

def menu():
    op = 0
    while(op !=10):
     op =int (input("Digite a opção desejada Aperte\n 1: Para inserir dados em uma tabela\n 2: Excluir dados de uma tabela"))
     if(op ==1):
         inserir_tabelas()
     if(op==2):
         break

if(__name__ == '__main__'):
   menu()