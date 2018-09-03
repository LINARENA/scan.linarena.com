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
-- Table structure for table `account_tbl`
--

DROP TABLE IF EXISTS `account_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_tbl` (
  `idx` bigint(20) NOT NULL AUTO_INCREMENT,
  `account_name` varchar(40) DEFAULT NULL,
  `created` varchar(40) DEFAULT NULL,
  `block_num` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `action_tbl`
--

DROP TABLE IF EXISTS `action_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_tbl` (
  `idx` bigint(20) NOT NULL AUTO_INCREMENT,
  `action_name` varchar(40) DEFAULT NULL,
  `txn_id` varchar(64) DEFAULT NULL,
  `authorization` varchar(80) DEFAULT NULL,
  `contract` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `block_tbl`
--

DROP TABLE IF EXISTS `block_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `block_tbl` (
  `idx` bigint(20) NOT NULL AUTO_INCREMENT,
  `block_num` bigint(20) unsigned DEFAULT NULL,
  `block_id` varchar(64) DEFAULT NULL,
  `timestamp` varchar(30) DEFAULT NULL,
  `transactions` int(11) DEFAULT NULL,
  `producer` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idx`),
  UNIQUE KEY `block_num` (`block_num`),
  UNIQUE KEY `block_id` (`block_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `transaction_tbl`
--

DROP TABLE IF EXISTS `transaction_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction_tbl` (
  `idx` bigint(20) NOT NULL AUTO_INCREMENT,
  `txn_id` varchar(64) DEFAULT NULL,
  `expiration` varchar(40) DEFAULT NULL,
  `actions` int(11) DEFAULT NULL,
  `block_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`idx`),
  UNIQUE KEY `txn_id` (`txn_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-01  4:04:17
