CREATE DATABASE bliblioteca;

CREATE TABLE bliblioteca(
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    PRIMARY KEY (codigo));

CREATE TABLE categoria (
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (codigo)
);

CREATE TABLE estante (
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    localizacao VARCHAR(50) NOT NULL,
    capacidade INT(5) NOT NULL,
    PRIMARY KEY (codigo)
);

CREATE TABLE atendente (
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOTot  NULL,
    estado CHAR(2) NOT NULL,
    telefone INT(10) NOT NULL,
    salario FLOAT(8,2) NOT NULL,
    codbiblioteca int(5) NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codbiblioteca) REFERENCES bliblioteca(codigo) 
);
CREATE TABLE livro (
    codigo INT(5) NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    editora VARCHAR(50) NOT NULL,
    edicao VARCHAR(50) not NULL,
    anopublicacao INT(4) NOT NULL,
    npagina INT(4) NOT NULL,
    codestante INT(5) NOT NULL,
    
);
