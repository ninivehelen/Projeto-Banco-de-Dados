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
duracao char(30) not null
);


create table sessao(
cod_sessao numeric(5) primary key,
cod_filme numeric (5) not null,
cod_cinema numeric(5),
constraint fk_cod_filme FOREIGN KEY (cod_filme) REFERENCES filme(cod_filme),
constraint fk_cod_cinema FOREIGN KEY (cod_cinema) REFERENCES cinema(cod_cinema),
data char(30) not null,
hora char(30) not null,
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
quantidade_ingressos numeric(10) not null,
forma_pagamento char(5) not null
);

create table funcionarios(
cod_funcionario numeric(5) primary key,
nome char(30) not null,
endereco char(30) not null,
cidade char(30) not null,
telefone numeric(20) not null
);


DELIMITER $
CREATE TRIGGER capacidade_sala AFTER INSERT ON ingresso
FOR EACH ROW
BEGIN
	update cinema C
    inner join sessao S
    on C.cod_cinema= S.cod_cinema
    INNER JOIN ingresso I
    on I.cod_sessao = S.cod_sessao
    set capacidade = capacidade - quantidade_ingressos;
END $
DELIMITER ;


DELIMITER
CREATE PROCEDURE selecionar_clientes(IN quantidade INT)
BEGIN SELECT * FROM clientes
LIMIT
quantidade;
END

CREATE FUNCTION ver_filme_hora(titulo char(30))
RETURNS VARCHAR(60) DETERMINISTIC 
RETURN (SELECT CONCAT(F.titulo,  S.hora) from filme F inner join sessao S on F.cod_filme = S.cod_filme
where titulo=F.titulo)


insert into clientes values (2,'pedro',12345, 'M', 98765);

insert into cinema values (2,'cineflix',12, 14, 'brasilia');

insert into filme values (2,'vingadores','ação e aventura', '2');

insert into ingresso values (2,2,2,5,'c');

insert into sessao values(2,2,2, '27/07/2022','14h','15');
