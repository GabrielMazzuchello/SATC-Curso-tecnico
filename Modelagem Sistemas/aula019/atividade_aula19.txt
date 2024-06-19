create database cadastro_engenheiros;

create table escritorio (
    cnpj VARCHAR(14) NOT NULL,
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    telefone INT(10) NOT NULL,
    PRIMARY KEY (cnpj));

create table setor (
    codigo INT(5) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    gerente VARCHAR(50) NOT NULL,
    telefone NUMERIC(11) NOT NULL,
    cnpjescritorio VARCHAR(14) NOT NULL,
    PRIMARY KEY (codigo),
    foreign KEY (cnpjescritorio) REFERENCES escritorio(cnpj));

create table engenheiro (
    cpf INT(11) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario FLOAT(7) NOT NULL,
    telefone INT(10) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    codcodigo INT(5) NOT NULL,
    PRIMARY KEY (cpf),
    FOREIGN KEY (codcodigo) REFERENCES setor(codigo),
);

create table projeto (
    codigo INT(5) NOT NULL,
    descricao VARCHAR(1000) NOT null,
    data_inicio date not NULL,
    data_fim date not NULL,
    valor FLOAT(11),
    codcpf INT(5) NOT NULL,
    codcodigo INT(5) NOT NULL,
    codcpf INT(5) NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codcpf) REFERENCES engenheiro(cpf),
    FOREIGN KEY (codcodigo) REFERENCES tipos(codigo),
    FOREIGN KEY (codcpf) REFERENCES clientes(cpf),
);

create table tipos (
    codigo INT(5) NOT NULL,
    descricao VARCHAR(1000) NOT null,
    area VARCHAR(50) NOT NULL,
    PRIMARY KEY (codigo)
);

create table clientes (
    cpf INT(11) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    telefone INT(10) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    PRIMARY KEY (cpf)
);






