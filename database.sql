-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.14-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for school
CREATE DATABASE IF NOT EXISTS `school` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `school`;

-- Dumping structure for table school.abm11
CREATE TABLE IF NOT EXISTS `abm11` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.abm11: ~9 rows (approximately)
/*!40000 ALTER TABLE `abm11` DISABLE KEYS */;
INSERT INTO `abm11` (`subject`, `subject2`, `id`) VALUES
	('21st Century Literature', 'Physical Science', 1),
	('Earth Science', 'Pagbasa at Pagsusuri', 2),
	('General Mathematics', 'EASP\'', 3),
	('Komunikasyon at Pananaliksik', 'Practical Research 1', 4),
	('Oral Communication', 'Personal Development', 5),
	('Physical Education 1', 'PE 2', 6),
	('Empowerment Technologies', 'Reading and Writing', 7),
	('Applied Economics', 'Statistics and Probability', 8),
	('Bussines Math', '', 9);
/*!40000 ALTER TABLE `abm11` ENABLE KEYS */;

-- Dumping structure for table school.abm12
CREATE TABLE IF NOT EXISTS `abm12` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.abm12: ~8 rows (approximately)
/*!40000 ALTER TABLE `abm12` DISABLE KEYS */;
INSERT INTO `abm12` (`subject`, `subject2`, `id`) VALUES
	('Contemporary Philippine Arts', 'Media Information Literacy', 1),
	('Introduction to Philosophy', 'Media Information Literacy', 2),
	('PE 3', 'Understanding Culture,Society and Politics', 3),
	('Filipino sa Piling Larang', 'Entrepreneurship', 4),
	('Practical Research 2', 'Creative NON - Fiction', 5),
	('Creative Writting', 'Inquiries,Investigations and Immersion', 6),
	('Community Engagement', 'Trend,Networks and Critical Thinking', 7),
	('', 'Work Immersion', 8);
/*!40000 ALTER TABLE `abm12` ENABLE KEYS */;

-- Dumping structure for table school.hums11
CREATE TABLE IF NOT EXISTS `hums11` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.hums11: ~10 rows (approximately)
/*!40000 ALTER TABLE `hums11` DISABLE KEYS */;
INSERT INTO `hums11` (`subject`, `subject2`, `id`) VALUES
	('21st Century Literature', 'Physical Science', 1),
	('Earth Science', 'EASP', 2),
	('General Mathematics', 'Introduction to World Religions', 3),
	('Komunikasyon at Pananaliksik', 'Pagbasa at Pagsusuri', 4),
	('Oral Communication', 'Personal Development', 5),
	('Physical Education 1', 'PE 2', 6),
	('Empowerment Technologies', 'Reading and Writing', 7),
	('Phillippine Politics and Governance', 'Statistics and Probability', 8),
	('Discipline and Idea in the Social Sciences', 'Discipline and Ideas in the Applied Social Sciences', 9),
	('', 'Practical Research 1', 10);
/*!40000 ALTER TABLE `hums11` ENABLE KEYS */;

-- Dumping structure for table school.hums12
CREATE TABLE IF NOT EXISTS `hums12` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.hums12: ~7 rows (approximately)
/*!40000 ALTER TABLE `hums12` DISABLE KEYS */;
INSERT INTO `hums12` (`subject`, `subject2`, `id`) VALUES
	('1Contemporary Philippine Arts', 'Media Information Literacy', 1),
	('Introduction to Philosophy', 'Physical Education 4', 2),
	('PE 3', 'Understanding Culture,Society and Politics', 3),
	('Filipino sa Piling Larang', 'Entrepreneurship', 4),
	('Practical Research 2', 'Creative NON - Fiction', 5),
	('Creative Writting', 'Trend,Networks and Critical Thinking', 6),
	('Community Engagement', 'Work Immersion', 7);
/*!40000 ALTER TABLE `hums12` ENABLE KEYS */;

-- Dumping structure for table school.stem11
CREATE TABLE IF NOT EXISTS `stem11` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.stem11: ~10 rows (approximately)
/*!40000 ALTER TABLE `stem11` DISABLE KEYS */;
INSERT INTO `stem11` (`subject`, `subject2`, `id`) VALUES
	('21st Century Literature', 'DRRR', 1),
	('Earth Science', 'EASP', 2),
	('General Mathematics', 'Basic Calculus', 3),
	('Komunikasyon at Pananaliksik', 'General Biology 2', 4),
	('Oral Communication', 'Practical Research 1', 5),
	('Physical Education 1', 'Pagbasa at Pagsusuri', 6),
	('Empowerment Technologies', 'Personal Development', 7),
	('General Biology 1', 'PE 2', 8),
	('Pre - Calculus', 'Reading and Writing', 9),
	('', 'Statistics and Probability', 10);
/*!40000 ALTER TABLE `stem11` ENABLE KEYS */;

-- Dumping structure for table school.stem12
CREATE TABLE IF NOT EXISTS `stem12` (
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.stem12: ~8 rows (approximately)
/*!40000 ALTER TABLE `stem12` DISABLE KEYS */;
INSERT INTO `stem12` (`subject`, `subject2`, `id`) VALUES
	('Contemporary Philippine Arts', 'Media Information Literacy', 1),
	('Introduction to Philosophy', 'Physical Education 4', 2),
	('PE 3', 'Understanding Culture,Society and Politics', 3),
	('Filipino sa Piling Larang', 'Entrepreneurship', 4),
	('Practical Research 2', 'Inquiries,Investigations and Immersion', 5),
	('General Chemistry 1', 'General Chemistry 2', 6),
	('General Physics 1', 'General Physics 2', 7),
	('', 'Work Immersion/Capstone Project', 8);
/*!40000 ALTER TABLE `stem12` ENABLE KEYS */;

-- Dumping structure for table school.stem13
CREATE TABLE IF NOT EXISTS `stem13` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) NOT NULL,
  `subject2` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table school.stem13: ~0 rows (approximately)
/*!40000 ALTER TABLE `stem13` DISABLE KEYS */;
/*!40000 ALTER TABLE `stem13` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

