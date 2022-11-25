-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.24-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para farmaciamaromba
CREATE DATABASE IF NOT EXISTS `farmaciamaromba` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `farmaciamaromba`;

-- Copiando estrutura para tabela farmaciamaromba.laboratorios
CREATE TABLE IF NOT EXISTS `laboratorios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `cnpj` varchar(14) NOT NULL,
  `tel` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela farmaciamaromba.laboratorios: ~1 rows (aproximadamente)
INSERT INTO `laboratorios` (`id`, `nome`, `cnpj`, `tel`, `email`) VALUES
	(1, 'Pfizer', '1234567891111', NULL, NULL);

-- Copiando estrutura para tabela farmaciamaromba.produtos
CREATE TABLE IF NOT EXISTS `produtos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `desc` text DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `preco` int(11) DEFAULT NULL,
  `lab_id` int(11) NOT NULL,
  `desconto` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_laboratorio` (`lab_id`),
  CONSTRAINT `from_laboratorio` FOREIGN KEY (`lab_id`) REFERENCES `laboratorios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela farmaciamaromba.produtos: ~3 rows (aproximadamente)
INSERT INTO `produtos` (`id`, `nome`, `desc`, `tipo`, `preco`, `lab_id`, `desconto`) VALUES
	(1, 'Whey sabor Pipoca', 'Whey sem sabor que dizem ter sabor de pipoca', 'Suplemento', 290, 1, 10),
	(6, 'Hoje', 'é um novo dia', 'que começou', 12, 1, 10),
	(7, 'assd', 'sadasd', '112sad', 132, 1, 123),
	(8, 'Whey de Morango', 'Sabor Tutifruti', 'Suplemento', 100, 1, 0);

-- Copiando estrutura para tabela farmaciamaromba.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL DEFAULT '',
  `senha` char(32) NOT NULL,
  `nivel` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela farmaciamaromba.usuarios: ~0 rows (aproximadamente)
INSERT INTO `usuarios` (`id`, `nome`, `senha`, `nivel`) VALUES
	(1, '0', 'admin', 0),
	(2, 'admin', 'admin', 0);

-- Copiando estrutura para tabela farmaciamaromba.vendas
CREATE TABLE IF NOT EXISTS `vendas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total` int(11) DEFAULT NULL,
  `vendedor_id` int(11) DEFAULT NULL,
  `horario` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__usuario` (`vendedor_id`),
  CONSTRAINT `FK__usuario` FOREIGN KEY (`vendedor_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela farmaciamaromba.vendas: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
