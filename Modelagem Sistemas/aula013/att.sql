CREATE TABLE fabricantes (
    codigo int(5) not null,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    codigo int(2) not null,
    codigo int(10) not null,
    codigo int(15) not null,
    PRIMARY KEY (codigo)
    );

CREATE TABLE produtos (
    codigo int(5) not null,
    nome VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    codigo int(5) not null,
    codigo float(8, 2) not null,
    codigo int(5) NOT null,
    primary key (codigo),
    foreign key (codfabricante) REFERENCES fabricantes(codigo)
    );
CREATE TABLE compras (
    codigo INT(5) NOT NULL,
    data date NOT NULL,
    notafiscal int(10) NOT NULL,
    totalcompra FLOAT(10,2) NOT NULL,
    codcliente int(5) NOT NULL,
    codproduto INT(5) NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codcliente) REFERENCES clientes (codigo),
    FOREIGN KEY (codproduto) REFERENCES produtos (codigo)
);