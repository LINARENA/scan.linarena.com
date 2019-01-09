-- MySQL dump 10.15  Distrib 10.0.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: scanner
-- ------------------------------------------------------
-- Server version	10.0.34-MariaDB-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `producer_tbl`
--

DROP TABLE IF EXISTS `producer_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producer_tbl` (
  `idx` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(120) NOT NULL,
  `article` text NOT NULL,
  `accnt_name` varchar(13) NOT NULL,
  `slogan` varchar(60) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  `homepage` varchar(60) DEFAULT NULL,
  `maps_lat` varchar(20) DEFAULT NULL,
  `maps_lng` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idx`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producer_tbl`
--

LOCK TABLES `producer_tbl` WRITE;
/*!40000 ALTER TABLE `producer_tbl` DISABLE KEYS */;
INSERT INTO `producer_tbl` VALUES (1,'Reponse-pda','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pda','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(2,'Reponse-pdb','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdb','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(3,'Reponse-pdc','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdc','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(4,'Reponse-pdd','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdd','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(5,'Reponse-pde','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pde','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(6,'Reponse-pdf','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdf','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(7,'Reponse-pdg','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdg','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(8,'Reponse-pdh','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdh','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244'),(9,'Reponse-pdi','support@reponse.co','Reponse. A QnA blockchain service which provides direct compensation and copyright protection for the person that asks the question and for the person that answers the question. Reponse is a service utilized to ask and answer questions. We encourage everyone to utilize the \'question\' space for asking and the \'answer\' space for answering. It\'s as simple as that. Ask questions and receive points. Answer questions and receive points. The points earned can be exchanged for Reponse crypto currency. All questions and answers will utilize blockchain technology deeming the content copyright and therefore cannot be changed.','reponse.pdi','Blockchian Based Q&A service','Republic of Korea, Seoul','https://reponse.co','37.4748809','126.88244');
/*!40000 ALTER TABLE `producer_tbl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-13 20:30:33
