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
