
CREATE DATABASE IF NOT EXISTS base
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;


CREATE TABLE pessoas(
id int NOT NULL AUTO_INCREMENT,
nome varchar(30) NOT NULL,
nascimento date,
sexo enum('M','F'),
peso decimal(5,2),
altura decimal(3,2),
nascionalidade varchar(20) DEFAULT 'Brasil',
PRIMARY KEY (id)
)DEFAULT CHARSET = utf8mb4;


CREATE TABLE vendas(
id int NOT NULL AUTO_INCREMENT,
nome_produto varchar(30) NOT NULL,
valor decimal(3,2),
PRIMARY KEY (id)
)DEFAULT CHARSET = utf8mb4;



INSERT INTO pessoas
(nome, nascimento, sexo, peso, altura, nascionalidade)
VALUES
('Godofredo','1984-01-02','M', '78.5', '1.83','Brasil');



INSERT INTO pessoas VALUES
(DEFAULT,'Matheus','2018-08-12','M', '18', '0.8','Brasil'),
(DEFAULT,'Pietro','2015-11-09','M', '30', '1.20','Brasil'),
(DEFAULT,'Ana Clara','2011-02-08','F', '50', '1.50','Brasil');



ALTER TABLE pessoas
ADD COLUMN profissao VARCHAR(10);

ALTER TABLE pessoas
DROP COLUMN profissao;

ALTER TABLE pessoas
ADD COLUMN profissao VARCHAR(10) AFTER nome;

ALTER TABLE pessoas
ADD COLUMN profissao VARCHAR(10) FIRST;

ALTER TABLE pessoas
ADD codigo VARCHAR(10) FIRST;

ALTER TABLE pessoas
MODIFY profissao VARCHAR(20) NOT NULL DEFAULT '';

ALTER TABLE pessoas
CHANGE COLUMN profissao prof VARCHAR(20) NOT NULL DEFAULT '';

ALTER TABLE pessoas
RENAME TO gafamhotos;


DESCRIBE pessoas;

DROP DATABASE cadastro;
DROP TABLE cursos;

SELECT * FROM pessoas;

DESC pessoas;


SELECT * FROM vendas;



DDL
	CREATE DATABASE cadastro
	CREATE TABLE pessoas
	ALTER TABLE pessoas
	DROP DATABASE cadastro;
	DROP TABLE cursos;
	

DML
	INSERT INTO pessoas VALUES


