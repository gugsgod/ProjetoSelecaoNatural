CREATE DATABASE IF NOT EXISTS jogodb;

USE jogodb;

CREATE TABLE IF NOT EXISTS usuarios(
	idUsuario INT,
    nome VARCHAR(255),
    email VARCHAR(255) UNIQUE,
	senha VARCHAR(255),
    ident INT,
    PRIMARY KEY (idUsuario)
    );

CREATE TABLE IF NOT EXISTS pontuacao(
	idUsuario INT,
    pontos INT,
    rodada INT,
    FOREIGN KEY (idUsuario) REFERENCES usuarios(idUsuario)
); 

CREATE TABLE IF NOT EXISTS questoes(
	idQuestao int,
    pergunta VARCHAR(120),
    alternativa_a VARCHAR(160),
    alternativa_b VARCHAR(160),
	alternatica_c VARCHAR(160),
	alternatica_d VARCHAR(160)
);