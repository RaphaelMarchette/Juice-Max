SELECT * FROM Sucos;

CREATE DATABASE IF NOT EXISTS JuiceMax
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;


CREATE TABLE Sucos(
id INT NOT NULL,
Nome varchar(30) NOT NULL,
Estoque decimal(3),
valor decimal(3,2),
PRIMARY KEY (id)
)DEFAULT CHARSET = utf8mb4;



CREATE TABLE `funcionarios` (
  `id` Int DEFAULT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(110) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `data_nasc` datetime NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `endereco` varchar(45) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci