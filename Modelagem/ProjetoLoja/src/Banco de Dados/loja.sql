-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tempo de Geração: 10/04/2025 às 19h07min
-- Versão do Servidor: 5.5.20
-- Versão do PHP: 5.3.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `loja`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Extraindo dados da tabela `categoria`
--

INSERT INTO `categoria` (`codigo`, `nome`) VALUES
(2, 'roupas'),
(3, 'acessorios'),
(4, 'tenes');

-- --------------------------------------------------------

--
-- Estrutura da tabela `marca`
--

CREATE TABLE IF NOT EXISTS `marca` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Extraindo dados da tabela `marca`
--

INSERT INTO `marca` (`codigo`, `nome`) VALUES
(1, 'nike'),
(2, 'adidas'),
(3, 'lacoste');

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE IF NOT EXISTS `produto` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(100) NOT NULL,
  `cor` varchar(50) NOT NULL,
  `tamanho` varchar(3) NOT NULL,
  `preco` float(8,2) NOT NULL,
  `codmarca` int(5) NOT NULL,
  `codcategoria` int(5) NOT NULL,
  `codtipo` int(5) NOT NULL,
  `foto1` varchar(150) NOT NULL,
  `foto2` varchar(150) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `codmarca` (`codmarca`),
  KEY `codtipo` (`codtipo`),
  KEY `foto1` (`foto1`),
  KEY `codtipo_2` (`codtipo`),
  KEY `codcategoria` (`codcategoria`),
  KEY `codcategoria_2` (`codcategoria`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Extraindo dados da tabela `produto`
--

INSERT INTO `produto` (`codigo`, `descricao`, `cor`, `tamanho`, `preco`, `codmarca`, `codcategoria`, `codtipo`, `foto1`, `foto2`) VALUES
(12, 'Camiseta Lacoste Infantil', 'branca', 'M', 150.00, 3, 2, 3, 'bae00f60004d94fe9aa831a0e241224b.jpg', 'bae00f60004d94fe9aa831a0e241224b.jpg'),
(13, 'TÃªnis Lacoste Infantil', 'branca', '30', 150.00, 3, 4, 3, '8dff5a0c7dec9c2585b5872c02c21efa.jpg', '8dff5a0c7dec9c2585b5872c02c21efa.jpg'),
(14, 'Jaqueta Adidas Masculina', 'branca', 'M', 349.00, 2, 2, 1, '75879a14c8ba3e6cda2da1888bf3a539.jpg', '75879a14c8ba3e6cda2da1888bf3a539.jpg'),
(15, 'TÃªnis Adidas Masculino', 'preto', '40', 549.00, 2, 4, 1, '81dfb2340d493d911f3a41d8dedddf22.jpg', '81dfb2340d493d911f3a41d8dedddf22.jpg'),
(16, 'Bolsa Nike Feminina', 'preto', 'G', 549.00, 1, 3, 2, '38c2d353bfed9c0c6dea4de2beec9765.jpg', '38c2d353bfed9c0c6dea4de2beec9765.jpg'),
(17, ' BonÃ© Nike Infantil', 'preto', 'p', 49.00, 1, 3, 3, 'b0b77721d9c1fe536d0b55640e985e7b.jpg', 'b0b77721d9c1fe536d0b55640e985e7b.jpg'),
(18, 'TÃªnis Adidas Runfalcon 3.0', 'Preto com detalhes em branco', '41', 279.00, 2, 4, 1, 'cdb20722d058ee8c3a1587434c4689e3.jpg', 'cdb20722d058ee8c3a1587434c4689e3.jpg'),
(19, 'Camiseta Nike Dri-FIT Academy', 'Branco com logo preto', 'G', 139.00, 1, 2, 1, 'ad25f153fca9a0590827483bdfd0a919.jpg', 'ad25f153fca9a0590827483bdfd0a919.jpg');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo`
--

CREATE TABLE IF NOT EXISTS `tipo` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Extraindo dados da tabela `tipo`
--

INSERT INTO `tipo` (`codigo`, `nome`) VALUES
(1, 'masculino'),
(2, 'feminino'),
(3, 'infantil');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`codigo`, `login`, `senha`) VALUES
(1, 'gabriel', '123');

--
-- Restrições para as tabelas dumpadas
--

--
-- Restrições para a tabela `produto`
--
ALTER TABLE `produto`
  ADD CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`codmarca`) REFERENCES `marca` (`codigo`),
  ADD CONSTRAINT `produto_ibfk_2` FOREIGN KEY (`codcategoria`) REFERENCES `categoria` (`codigo`),
  ADD CONSTRAINT `produto_ibfk_3` FOREIGN KEY (`codtipo`) REFERENCES `tipo` (`codigo`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
