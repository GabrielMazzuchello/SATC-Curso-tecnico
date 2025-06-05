-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tempo de Geração: 05/06/2025 às 22h20min
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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `autor`
--

INSERT INTO `autor` (`codigo`, `nome`, `pais`) VALUES
(1, 'Machado de Assis', 'Brazil');

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `categoria`
--

INSERT INTO `categoria` (`codigo`, `nome`) VALUES
(1, 'RomÃ¢nce');

-- --------------------------------------------------------

--
-- Estrutura da tabela `editora`
--

CREATE TABLE IF NOT EXISTS `editora` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Extraindo dados da tabela `editora`
--

INSERT INTO `editora` (`codigo`, `nome`) VALUES
(1, 'haga'),
(2, 'haga2');

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `livro`
--

INSERT INTO `livro` (`codigo`, `titulo`, `nrpaginas`, `ano`, `codautor`, `codcategoria`, `codeditora`, `resenha`, `preco`, `fotocapa1`, `fotocapa2`) VALUES
(1, 'Dom Casmurro', 256, 1899, 1, 1, 1, 'teste', 45, 'assets/img/68389fea8bf1f7.01234391.jpg', 'assets/img/68389fea8c9e55.70687898.jpg');

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
  ADD CONSTRAINT `livro_ibfk_1` FOREIGN KEY (`codautor`) REFERENCES `categoria` (`codigo`),
  ADD CONSTRAINT `livro_ibfk_2` FOREIGN KEY (`codeditora`) REFERENCES `editora` (`codigo`),
  ADD CONSTRAINT `livro_ibfk_3` FOREIGN KEY (`codcategoria`) REFERENCES `categoria` (`codigo`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
