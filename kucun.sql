-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: kucun
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gift`
--

DROP TABLE IF EXISTS `gift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gift` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mc` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `rkrq` datetime DEFAULT CURRENT_TIMESTAMP,
  `ckrq` datetime DEFAULT NULL,
  `jinjia` smallint(6) DEFAULT NULL,
  `bz` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gift`
--

LOCK TABLES `gift` WRITE;
/*!40000 ALTER TABLE `gift` DISABLE KEYS */;
/*!40000 ALTER TABLE `gift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobile`
--

DROP TABLE IF EXISTS `mobile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pp` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `xh` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `ch` varchar(20) DEFAULT NULL,
  `rkrq` datetime DEFAULT CURRENT_TIMESTAMP,
  `ckrq` datetime DEFAULT NULL,
  `jinjia` smallint(6) DEFAULT NULL,
  `shoujia` smallint(6) DEFAULT NULL,
  `fkfs` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `bz` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile`
--

LOCK TABLES `mobile` WRITE;
/*!40000 ALTER TABLE `mobile` DISABLE KEYS */;
INSERT INTO `mobile` VALUES (4,'OPPO','A37t金','865745031483799','2017-12-01 13:06:36',NULL,900,NULL,NULL,''),(5,'OPPO','A37t金','866488034455113','2017-12-01 13:06:48',NULL,900,NULL,NULL,''),(6,'OPPO','A57t黑','867461036025035','2017-12-01 13:11:52',NULL,1145,NULL,NULL,''),(7,'OPPO','A57t粉','866503030717439','2017-12-01 13:12:09',NULL,1145,NULL,NULL,'');
/*!40000 ALTER TABLE `mobile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobile_card`
--

DROP TABLE IF EXISTS `mobile_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobile_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lx` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `haoma` varchar(20) DEFAULT NULL,
  `rkrq` datetime DEFAULT CURRENT_TIMESTAMP,
  `ckrq` datetime DEFAULT NULL,
  `jinjia` smallint(6) DEFAULT NULL,
  `shoujia` smallint(6) DEFAULT NULL,
  `fkfs` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `bz` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile_card`
--

LOCK TABLES `mobile_card` WRITE;
/*!40000 ALTER TABLE `mobile_card` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobile_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parts`
--

DROP TABLE IF EXISTS `parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pp` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `mc` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `rkrq` datetime DEFAULT CURRENT_TIMESTAMP,
  `ckrq` datetime DEFAULT NULL,
  `jinjia` smallint(6) DEFAULT NULL,
  `shoujia` smallint(6) DEFAULT NULL,
  `fkfs` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `bz` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parts`
--

LOCK TABLES `parts` WRITE;
/*!40000 ALTER TABLE `parts` DISABLE KEYS */;
INSERT INTO `parts` VALUES (2,'飞毛腿','充电宝','2017-10-09 13:49:40','2017-10-09 13:55:06',50,80,'现金',''),(3,'飞毛腿','充电宝','2017-10-09 13:49:40',NULL,50,NULL,NULL,''),(4,'飞毛腿','充电宝','2017-10-09 13:49:40',NULL,50,NULL,NULL,''),(5,'飞毛腿','充电宝','2017-10-09 13:49:40',NULL,50,NULL,NULL,''),(6,'AA','AA','2017-12-03 05:17:46',NULL,11,NULL,NULL,''),(7,'AA','AA','2017-12-03 05:17:57',NULL,11,NULL,NULL,''),(8,'AA','AA','2017-12-03 05:25:46',NULL,11,NULL,NULL,'');
/*!40000 ALTER TABLE `parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `power` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','QWERqwer','admin'),(2,'fx123','QWERqwer','normal');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-03 15:20:01
