-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09/06/2025 às 14:47
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `livraria`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `autor`
--

CREATE TABLE `autor` (
  `codigo` int(5) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `pais` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Despejando dados para a tabela `autor`
--

INSERT INTO `autor` (`codigo`, `nome`, `pais`) VALUES
(1, 'Machado de Assis', 'Brazil'),
(2, 'Junior Rostirola', 'Brazil'),
(3, 'teste', 'teste');

-- --------------------------------------------------------

--
-- Estrutura para tabela `categoria`
--

CREATE TABLE `categoria` (
  `codigo` int(5) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Despejando dados para a tabela `categoria`
--

INSERT INTO `categoria` (`codigo`, `nome`) VALUES
(1, 'RomÃ¢nce'),
(2, 'Ficção Científica');

-- --------------------------------------------------------

--
-- Estrutura para tabela `editora`
--

CREATE TABLE `editora` (
  `codigo` int(5) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Despejando dados para a tabela `editora`
--

INSERT INTO `editora` (`codigo`, `nome`) VALUES
(1, 'haga'),
(2, 'haga2'),
(3, 'Vélos');

-- --------------------------------------------------------

--
-- Estrutura para tabela `livro`
--

CREATE TABLE `livro` (
  `codigo` int(5) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `nrpaginas` int(5) NOT NULL,
  `ano` int(11) NOT NULL,
  `codautor` int(5) NOT NULL,
  `codcategoria` int(5) NOT NULL,
  `codeditora` int(5) NOT NULL,
  `resenha` varchar(300) NOT NULL,
  `preco` float NOT NULL,
  `fotocapa1` varchar(100) NOT NULL,
  `fotocapa2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Despejando dados para a tabela `livro`
--

INSERT INTO `livro` (`codigo`, `titulo`, `nrpaginas`, `ano`, `codautor`, `codcategoria`, `codeditora`, `resenha`, `preco`, `fotocapa1`, `fotocapa2`) VALUES
(1, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(3, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(5, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(6, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(7, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(8, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(9, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(10, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(11, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(12, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(13, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(14, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024\", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(15, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(16, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `codigo` int(5) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`codigo`, `login`, `senha`) VALUES
(1, 'gabriel', '123456');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices de tabela `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`codigo`) USING BTREE;

--
-- Índices de tabela `editora`
--
ALTER TABLE `editora`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices de tabela `livro`
--
ALTER TABLE `livro`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `codautor` (`codautor`),
  ADD KEY `codeditora` (`codeditora`),
  ADD KEY `codcategoria` (`codcategoria`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `autor`
--
ALTER TABLE `autor`
  MODIFY `codigo` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `categoria`
--
ALTER TABLE `categoria`
  MODIFY `codigo` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `editora`
--
ALTER TABLE `editora`
  MODIFY `codigo` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `livro`
--
ALTER TABLE `livro`
  MODIFY `codigo` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `livro`
--
ALTER TABLE `livro`
  ADD CONSTRAINT `fk_livro_autor` FOREIGN KEY (`codautor`) REFERENCES `autor` (`codigo`),
  ADD CONSTRAINT `fk_livro_categoria` FOREIGN KEY (`codcategoria`) REFERENCES `categoria` (`codigo`),
  ADD CONSTRAINT `fk_livro_editora` FOREIGN KEY (`codeditora`) REFERENCES `editora` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
