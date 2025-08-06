-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tempo de Geração: 16/06/2025 às 21h00min
-- Versão do Servidor: 5.5.20
-- Versão do PHP: 5.3.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `livraria`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `autor`
--

CREATE TABLE IF NOT EXISTS `autor` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `pais` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Extraindo dados da tabela `autor`
--

INSERT INTO `autor` (`codigo`, `nome`, `pais`) VALUES
(1, 'Machado de Assis', 'Brazil'),
(2, 'Junior Rostirola', 'Brazil'),
(3, 'teste', 'teste'),
(9, 'Colleen Hoover', 'Estados Unidos');

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Extraindo dados da tabela `categoria`
--

INSERT INTO `categoria` (`codigo`, `nome`) VALUES
(1, 'RomÃ¢nce'),
(2, 'Ficção Científica'),
(3, 'MistÃ©rio'),
(4, 'Drama'),
(5, 'MistÃ©rio2');

-- --------------------------------------------------------

--
-- Estrutura da tabela `editora`
--

CREATE TABLE IF NOT EXISTS `editora` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Extraindo dados da tabela `editora`
--

INSERT INTO `editora` (`codigo`, `nome`) VALUES
(1, 'haga'),
(2, 'haga2'),
(3, 'Vélos'),
(5, 'Galera Record');

-- --------------------------------------------------------

--
-- Estrutura da tabela `livro`
--

CREATE TABLE IF NOT EXISTS `livro` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `nrpaginas` int(5) NOT NULL,
  `ano` int(11) NOT NULL,
  `codautor` int(5) NOT NULL,
  `codcategoria` int(5) NOT NULL,
  `codeditora` int(5) NOT NULL,
  `resenha` varchar(300) NOT NULL,
  `preco` float NOT NULL,
  `fotocapa1` varchar(100) NOT NULL,
  `fotocapa2` varchar(100) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `codautor` (`codautor`),
  KEY `codeditora` (`codeditora`),
  KEY `codcategoria` (`codcategoria`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Extraindo dados da tabela `livro`
--

INSERT INTO `livro` (`codigo`, `titulo`, `nrpaginas`, `ano`, `codautor`, `codcategoria`, `codeditora`, `resenha`, `preco`, `fotocapa1`, `fotocapa2`) VALUES
(1, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(3, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(5, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(6, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(7, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(8, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(9, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(10, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(11, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(12, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(13, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(14, 'Café com Deus Pai 2024', 424, 2023, 2, 1, 3, 'Café com Deus Pai 2024", do autor Junior Rostirola, é um devocional diário que se tornou um fenômeno de vendas no Brasil. A proposta do livro é simples e poderosa: oferecer uma dose diária de encorajamento, sabedoria e fé para começar o dia conectado com Deus.\r\n\r\nPara cada dia do ano, o livro aprese', 67, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/6844a0d3adda61.45324040.jpg'),
(15, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(16, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/6844a1bc425f90.94874285.jpg', 'assets/img/68389fea8c9e55.70687898.jpg'),
(17, 'Ã‰ Assim que Acaba', 368, 2018, 9, 4, 5, '"Ã‰ Assim que Acaba" narra a histÃ³ria de Lily Bloom, uma jovem que se muda para Boston e abre sua prÃ³pria floricultura. Vinda de um lar conturbado, ela estÃ¡ determinada a construir uma vida diferente da que teve. Ao conhecer o brilhante neurocirurgiÃ£o Ryle Kincaid, Lily acredita ter encontrado o', 37.9, 'assets/img/6847360ad7c178.08252106.jpg', 'assets/img/6847360ad83ed0.55001053.jpg');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `codigo` int(5) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`codigo`, `login`, `senha`) VALUES
(1, 'gabriel', '123456');

--
-- Restrições para as tabelas dumpadas
--

--
-- Restrições para a tabela `livro`
--
ALTER TABLE `livro`
  ADD CONSTRAINT `fk_livro_autor` FOREIGN KEY (`codautor`) REFERENCES `autor` (`codigo`),
  ADD CONSTRAINT `fk_livro_categoria` FOREIGN KEY (`codcategoria`) REFERENCES `categoria` (`codigo`),
  ADD CONSTRAINT `fk_livro_editora` FOREIGN KEY (`codeditora`) REFERENCES `editora` (`codigo`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
