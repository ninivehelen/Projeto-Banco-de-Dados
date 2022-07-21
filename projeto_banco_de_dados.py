import mysql.connector
import os
from time import sleep
from datetime import datetime
con = mysql.connector.connect(host='localhost',database='cinema',user='root',password='nHH36232585@')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

mycursor = con.cursor()

def imprimir_tabela(conexao, sql):
    os.system("clear")
    try:
        c = con.cursor()
        c.execute(sql)
        tabela = c.fetchall()
        print(tabela)
        for tabelas in tabela:
          print("\n")   
          print(tabelas) 
    except:
        print("Não foi possível imprimir os dados da tabela")

def inserir_tabela(conexao, sql):
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
    print("****************")
    print("[1] Inserir dados na tabela cliente")
    print("[2] Inserir dados na tabela funcionário")
    print("[3] Inserir dados na tabela cinema")
    print("[4] Inserir dados na tabela filme")
    print("[5] Inserir dados na tabela sessao")
    print("[6] Inserir dados na tabela ingresso")
    op =int (input("Op = "))
    if(op ==1):
        cod_cli = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        sexo = input("Digite o sexo do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        insere="INSERT INTO clientes (cod_cliente, nome, cpf, sexo, telefone)VALUES('"+cod_cli+"','"+nome+"','"+cpf+"','"+sexo+"','"+telefone+"')"
        inserir_tabela(mycursor,insere)
    if(op == 2):
         cod_funcionario = input("Digite o código do funcionário: ")
         nome = input("Digite  o nome do funcionário: ")
         endereco = input("Digite o endereço do funcionário: ")
         cidade = input("Digite a cidade do funcionário: ")
         telefone = input("Digite o telefone do funcionário: ")
         insere="INSERT INTO funcionarios (cod_funcionario, nome, endereco, cidade, telefone)VALUES('"+cod_funcionario+"','"+nome+"','"+endereco+"','"+cidade+"','"+telefone+"')"
         inserir_tabela(mycursor,insere)
    if(op == 3):
         cod_cinema = input("Digite o código do cinema: ")
         nome = input("Digite  o nome do cinema: ")
         sala= input("Digite o codigo da sala: ")
         capacidade = input("Digite a  quantidade da capacidade do cinema: ")
         cidade = input("Digite a cidade que fica localizado o cinema: ")
         insere="INSERT INTO cinema (cod_cinema, nome, sala, capacidade, cidade)VALUES('"+cod_cinema+"','"+nome+"','"+sala+"','"+capacidade+"','"+cidade+"')"
         inserir_tabela(mycursor,insere)
    if(op == 4):
         cod_filme = input("Digite o código do filme: ")
         titulo = input("Digite  o titulo do filme: ")
         genero= input("Digite o genero do filme : ")
         duracao = input("Digite a duração do filme: ")
         insere="INSERT INTO filme (cod_filme, titulo, genero, duracao)VALUES('"+cod_filme+"','"+titulo+"','"+genero+"','"+duracao+"')"
         inserir_tabela(mycursor,insere)
    if(op == 5):
         cod_sessao = input("Digite o código da sessão: ")
         cod_filme = input("Digite  o código do filme : ")
         cod_cinema = input("Digite o código do cinema : ")
         data = input("Digite a data da sessao: ")
         hora = input("Digite a hora da sessao: ")
         preco = input("Digite o preço do ingresso: ")
         insere ="INSERT INTO sessao (cod_sessao, cod_filme, cod_cinema, data, hora, preco)VALUES('"+cod_sessao+"','"+cod_filme+"','"+cod_cinema+"','"+data+"','"+hora+"','"+preco+"')"
         inserir_tabela(mycursor,insere)
    if(op == 6):
         cod_ingresso = input("Digite o código do ingresso: ")
         cod_cliente = input("Digite  o código do do cliente : ")
         cod_sessao = input("Digite o código da sessao : ")
         quant_inteira = input("Digite a quantidade da inteira do ingresso: ")
         quant_meia = input("Digite a quantidade da meia do ingresso: ")
         f_pagamento = input("Digite a forma de pagamento: ")
         insere ="INSERT INTO ingresso (cod_ingresso, cod_cliente, cod_sessao, quantidade_inteira, quantidade_meia, forma_pagamento)VALUES('"+cod_ingresso+"','"+cod_cliente+"','"+cod_sessao+"','"+quant_inteira+"','"+quant_meia+"','"+f_pagamento+"')"
         inserir_tabela(mycursor,insere)

def imprimir_dados_tabela():
 op = 0
 while(op !=10):
    print("****************")
    print("[1] Imprimir dados da tabela cliente")
    print("[2] Imprimir dados da tabela funcionário")
    print("[3] Imprimir dados da tabela cinema")
    print("[4] Imprimir dados da tabela filme")
    print("[5] Imprimir dados da tabela sessao")
    print("[6] Imprimir dados da tabela ingresso")
    op =int (input("Op = "))
    if(op ==1):
        insere="SELECT *FROM clientes"
        imprimir_tabela(mycursor,insere)
    if(op ==2):
        insere="SELECT *FROM funcionarios"
        imprimir_tabela(mycursor,insere)
    if(op ==3):
        insere="SELECT *FROM cinema"
        imprimir_tabela(mycursor,insere)
    if(op ==4):
        insere="SELECT *FROM filme"
        imprimir_tabela(mycursor,insere)
    if(op ==5):
        insere="SELECT *FROM sessao"
        imprimir_tabela(mycursor,insere)
    if(op ==6):
        insere="SELECT *FROM ingresso"
        imprimir_tabela(mycursor,insere)
    
def menu():
 op = 0
 while(op !=10):
    print("****************")
    print("[1] Inserir dados nas tabelas")
    print("[2] Atualizar dados das tabelas")
    print("[3] Inserir dados na tabela cinema")
    print("[4] Inserir dados na tabela filme")
    print("[5] Inserir dados na tabela sessao")
    print("[6] Imprimir informações das tabelas")
    op =int (input("Op = "))
    if(op ==1):
         inserir_tabelas()
    if(op==6):
        imprimir_dados_tabela()
if(__name__ == '__main__'):
   menu()