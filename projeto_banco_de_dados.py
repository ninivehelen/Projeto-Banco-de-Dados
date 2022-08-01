import mysql.connector
import os
from time import sleep
from datetime import datetime
con = mysql.connector.connect(host='localhost',database='cinema',user='root',password='password@')
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
        for tabelas in tabela:
          print("\n",tabelas) 
    except:
        print("Não foi possível imprimir os dados da tabela")

def view_tabela(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("View de gasto dos clientes criada")
       
    except:
        print("Não foi possivel criar a view de gastos dos clientes")

def create_function(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Function para visualizar horario do filme criada")
       
    except:
        print("Não foi possivel criar a function de visualizar horaáio do filme")


def create_procedure(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Procedure para visualizar os clientes criado")
    except:
        print("Não foi possível criar o procedure para visualizar os clientes")

def inserir_tabela(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Registro Inserido")
       
    except:
        print("Registro não Inserido")

def atualizar_tabela(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Registro alterado ")
       
    except:
        print("Não foi possível alterar o registro")

def excluir_dado(conexao, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        con.commit()
        print("Dado excluído ")
    except:
        print("Não foi possível excluir o dado")

def inserir_tabelas():
 op = 0
 while(op !=10):
    print("######## Inserir dados ##########")
    print("[1] Inserir dados na tabela cliente")
    print("[2] Inserir dados na tabela funcionário")
    print("[3] Inserir dados na tabela cinema")
    print("[4] Inserir dados na tabela filme")
    print("[5] Inserir dados na tabela sessao")
    print("[6] Inserir dados na tabela ingresso")
    print("[7] Para voltar ao menu inicial")
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
         quant_ingresso = input("Digite a quantidade de ingresos: ")
         f_pagamento = input("Digite a forma de pagamento: ")
         insere ="INSERT INTO ingresso (cod_ingresso, cod_cliente, cod_sessao, quantidade_ingressos, forma_pagamento)VALUES('"+cod_ingresso+"','"+cod_cliente+"','"+cod_sessao+"','"+quant_ingresso+"','"+f_pagamento+"')"
         inserir_tabela(mycursor,insere)
    if(op == 7):
        menu()

def atualizar_tabelas():
 op = 0
 while(op !=10):
    print("######## Atualizar tabelas ##########")
    print("[1] Alterar dados da tabela cliente")
    print("[2] Alterar dados da tabela funcionário")
    print("[3] Alterar dados da tabela cinema")
    print("[4] Alterar dados da tabela filme")
    print("[5] Alterar dados da tabela sessao")
    print("[6] Alterar dados da tabela ingresso")
    print("[7] Para voltar ao menu inicial")
    op =int (input("Op = "))
    if(op ==1):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE clientes SET "+coluna+" = '"+valor+"' WHERE cod_cliente = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op ==2):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE funcionarios SET "+coluna+" = '"+valor+"' WHERE cod_funcionario = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op ==3):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE cinema SET "+coluna+" = '"+valor+"' WHERE cod_cinema = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op ==4):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE filme SET "+coluna+" = '"+valor+"' WHERE cod_filme = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op ==5):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE sessao SET "+coluna+" = '"+valor+"' WHERE cod_sessao = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op ==6):
        coluna = input("Digite o nome da coluna  que voce deseja alterar: ")
        valor = input("Digite o valor novo: ")
        codigo = input("Digite o codigo que corresponde a coluna: ")
        insere = "UPDATE ingressos SET "+coluna+" = '"+valor+"' WHERE cod_ingresso = "+codigo+""
        print(insere)
        atualizar_tabela(mycursor,insere)
    if(op == 7):
        menu()

def view_tabelas():
 op = 0
 while(op !=10):
    print("######## View de Gastos dos Clientes ##########")
    insere="CREATE VIEW gastos_clientes_ingresso AS SELECT C.cod_cliente, C.nome, SUM(I.quantidade_ingressos * S.preco) AS TOTAL FROM clientes C INNER JOIN ingresso I ON C.cod_cliente = I.cod_cliente INNER JOIN sessao S on S.cod_sessao = I.cod_sessao  GROUP BY C.cod_cliente, C.nome"
    view_tabela(mycursor,insere)
    print("[7] Para voltar ao menu inicial")
    op =int (input("Op = "))
    if(op == 7):
       menu()

def create_functions():
 op = 0
 while(op !=10):
    print("######## View de Gastos dos Clientes ##########")
    insere = "CREATE FUNCTION ver_filme_hora(titulo char(30))RETURNS VARCHAR(60) DETERMINISTIC RETURN (SELECT CONCAT(F.titulo,  S.hora) from filme F inner join sessao S on F.cod_filme = S.cod_filme where titulo=F.titulo);"
    print()
    create_function(mycursor,insere)
    print("[7] Para voltar ao menu inicial")
    op =int (input("Op = "))
    if(op == 7):
       menu()

def create_procedures():
 op = 0
 while(op !=10):
    print("######## Procedure de Selecionar dados com limite  ##########")
    insere =  "DELIMITER\nCREATE PROCEDURE selecionar_clientes(IN quantidade INT)\nBEGIN SELECT * FROM clientes\nLIMIT\nquantidade;\nEND"
    print(insere)
    create_procedure(mycursor,insere)
    print("[7] Para voltar ao menu inicial")
    op =int (input("Op = "))
    if(op == 7):
       menu()

def imprimir_view_clientes():
 op = 0
 while(op !=10):
    print("######## Imprimir  a view de gastos dos clientes ##########")
    print("[7] Para voltar ao menu inicial")
    insere="SELECT *FROM gastos_clientes_ingresso"
    imprimir_tabela(mycursor,insere)
    op =int (input("Op = "))
    if(op ==7):
       menu()


def imprimir_function():
 op = 0
 while(op !=10):
    print("######## Imprimir  a view de gastos dos clientes ##########")
    print("[7] Para voltar ao menu inicial")
    nome_filme = input("Digite  o titulo do filme que deseja saber o horário: ")
    insere="select ver_filme_hora('"+nome_filme+"')"
    print(insere)
    imprimir_tabela(mycursor,insere)
    op =int (input("Op = "))
    if(op ==7):
       menu()

def imprimir_procedure():
 op = 0
 while(op !=10):
    print("######## Imprimir  o procedure com limite dos dados da tabela ingresso ##########")
    print("[7] Para voltar ao menu inicial")
    limite= input("Digite o limite que deseja imprimir: ")
    insere="CALL selecionar_clientes("+limite+")"
    print(insere)
    imprimir_tabela(mycursor,insere)
    op =int (input("Op = "))
    if(op ==7):
       menu()


def excluir_dados():
    print("######## Excluir dados de uma coluna ##########")
    print("[1] Excluir dados da tabela cliente")
    print("[2] Excluir dados da tabela funcionário")
    print("[3] Excluir dados da tabela cinema")
    print("[4] Excluir dados da tabela filme")
    print("[5] Excluir dados da tabela sessao")
    print("[6] Excluir dados da tabela ingresso")
    print("[7] Para voltar ao menu inicial")
    op =int (input("Op = "))
    if(op ==1):
        codigo = input("Digite o codigo do cliente que deseja exclui: ")
        insere = "DELETE FROM clientes WHERE cod_cliente = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op ==2):
        codigo = input("Digite o codigo do funcionário que deseja exclui: ")
        insere = "DELETE FROM funcionarios  WHERE cod_funcionario = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op ==3):
        codigo = input("Digite o codigo do cinema que deseja exclui: ")
        insere = "DELETE FROM cinema WHERE cod_cinema = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op ==4):
        codigo = input("Digite o codigo do filme que deseja exclui: ")
        insere = "DELETE FROM filme WHERE cod_filme = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op ==5):
        codigo = input("Digite o codigo da sessao que deseja exclui: ")
        insere = "DELETE FROM sessao WHERE cod_sessao = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op ==6):
        codigo = input("Digite o codigo do ingresso que deseja exclui: ")
        insere = "DELETE FROM ingresso WHERE cod_ingresso = "+codigo+""
        excluir_dado(mycursor,insere)
    if(op == 7):
        menu()

def imprimir_dados_tabela():
 op = 0
 while(op !=10):
    print("######## Imprimir dados  ##########")
    print("[1] Imprimir dados da tabela cliente")
    print("[2] Imprimir dados da tabela funcionário")
    print("[3] Imprimir dados da tabela cinema")
    print("[4] Imprimir dados da tabela filme")
    print("[5] Imprimir dados da tabela sessao")
    print("[6] Imprimir dados da tabela ingresso")
    print("[7] Para voltar ao menu inicial")
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
    if(op == 7):
        menu()
    
def menu():
 op = 0
 while(op !=13):
    print("#################################################")
    print("######## Menu Inicial ##########")
    print("[1]  Inserir dados nas tabelas")
    print("[2]  Atualizar dados das tabelas")
    print("[3]  Excluir dados das tabelas")
    print("[4]  Criar a view de gastos dos clientes")
    print("[5]  Imprimir a view de gastos dos clientes")
    print("[6]  Criar o tigger")
    print("[7]  Imprimir o tigger")
    print("[8]  Criar o procedure")
    print("[9]  Imprimir o procedure")
    print("[10]  Cria função ")
    print("[11]  Imprimir função")
    print("[12] Imprimir informações das tabelas")
    print("[13] Para sair do sistema")
    print("#################################################")
    op =int (input("Op = "))
    if(op ==1):
         inserir_tabelas()
    if(op ==2):
         atualizar_tabelas()
    if(op==3):
        excluir_dados()
    if(op ==4):
         view_tabelas()
    if(op == 5):
        imprimir_view_clientes()
    if(op == 6):
        print("Falta ser imprementado a criaçao da tigger")
    if(op == 7):
        print("Falta ser imprementado função imprimir tigger")
    if(op==8):
        create_procedures()
    if(op==9):
       imprimir_procedure()
    if(op==10):
        create_functions()
    if(op==11):
        imprimir_function()
    if(op==12):
        imprimir_dados_tabela()
if(__name__ == '__main__'):
   menu()
