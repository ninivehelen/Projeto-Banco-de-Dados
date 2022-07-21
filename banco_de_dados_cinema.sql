use cinema;

create table cinema(
cod_cinema numeric(5) primary key,
nome char(30) not null,
sala numeric(5) not null,
capacidade numeric(20) not null,
cidade char(30) not null
);


create table filme(
cod_filme numeric(5) primary key,
titulo char(30) not null,
genero char(30) not null,
duracao time not null
);


create table sessao(
cod_sessao numeric(5) primary key,
cod_filme numeric (5) not null,
cod_cinema numeric(5),
constraint fk_cod_filme FOREIGN KEY (cod_filme) REFERENCES filme(cod_filme),
constraint fk_cod_cinema FOREIGN KEY (cod_cinema) REFERENCES cinema(cod_cinema),
data date not null,
hora time not null,
preco double(5,2) not null
);

create table clientes(
cod_cliente numeric(5) primary key,
nome char(30) not null,
cpf text(11) not null,
sexo char(10) not null,
telefone numeric(20)
);

create table ingresso(
cod_ingresso numeric(5) primary key,
cod_cliente numeric(5),
cod_sessao numeric(5) not null,
constraint fk_cod_cliente FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente),
constraint fk_cod_sessao FOREIGN KEY (cod_sessao) REFERENCES sessao(cod_sessao),
quantidade_inteira numeric(10) not null,
quantidade_meia numeric(10) not null,
forma_pagamento char(5) not null
);

create table funcionarios(
cod_funcionario numeric(5) primary key,
nome char(30) not null,
endereco char(30) not null,
cidade char(30) not null,
telefone numeric(20) not null
);

