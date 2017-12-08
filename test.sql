-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: test
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
INSERT INTO `gift` VALUES (1,'风扇','2017-09-20 08:16:33','2017-09-20 08:20:33',100,''),(2,'风扇','2017-09-20 08:16:34','2017-09-20 08:20:38',100,''),(3,'风扇','2017-09-20 08:16:34','2017-10-08 15:14:46',100,''),(4,'风扇','2017-09-20 08:16:34',NULL,100,''),(5,'风扇','2017-09-20 08:16:34',NULL,100,''),(6,'冰箱','2017-09-20 15:27:53',NULL,200,''),(7,'电脑','2017-09-20 15:28:05',NULL,500,''),(8,'电脑','2017-09-20 15:28:05',NULL,500,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile`
--

LOCK TABLES `mobile` WRITE;
/*!40000 ALTER TABLE `mobile` DISABLE KEYS */;
INSERT INTO `mobile` VALUES (1,'啊','啊','123','2017-09-18 08:40:18','2017-09-18 09:55:24',1000,21,'支付宝','了'),(2,'大','我去','111','2017-09-18 09:44:23','2017-09-18 09:55:35',1111,11,'11','1'),(3,'sad','ads','123','2017-09-18 14:43:55',NULL,123,NULL,NULL,''),(4,'啊','啊','0987654321','2017-09-24 14:33:39','2017-09-24 14:34:01',1111,2000,'支付宝','１'),(5,'啊搜索','xx','1234','2017-10-07 12:23:48','2017-10-07 12:24:04',300,500,'None','');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile_card`
--

LOCK TABLES `mobile_card` WRITE;
/*!40000 ALTER TABLE `mobile_card` DISABLE KEYS */;
INSERT INTO `mobile_card` VALUES (2,'神州行','13111112222','2017-09-20 08:05:46','2017-09-20 08:06:31',20,50,'威信',''),(3,'全球通','15111111111','2017-09-20 08:06:16','2017-10-08 16:30:14',20,50,'None',''),(4,'啊','123456','2017-10-08 15:45:33','2017-10-08 16:32:11',20,50,'None',''),(5,'动感地带','13111111111','2017-10-08 16:14:14','2017-10-09 14:43:20',20,50,'QQ',''),(6,'动感地带','123456','2017-10-08 16:17:57',NULL,20,NULL,NULL,'');
/*!40000 ALTER TABLE `mobile_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msg`
--

DROP TABLE IF EXISTS `msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pp` varchar(10) NOT NULL,
  `xh` varchar(50) NOT NULL,
  `ch` varchar(50) NOT NULL,
  `rkrq` varchar(10) NOT NULL,
  `ckrq` varchar(10) NOT NULL,
  `je` varchar(10) NOT NULL,
  `fkfs` varchar(10) NOT NULL,
  `bz` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msg`
--

LOCK TABLES `msg` WRITE;
/*!40000 ALTER TABLE `msg` DISABLE KEYS */;
INSERT INTO `msg` VALUES (12,'vivo','x7','0987654321','8-2','8-3','2000','QQ','ly'),(13,'vivo','x7','0987654321','8-2','8-3','2000','QQ','lyly'),(18,'a','a','a','a','a','a','a','a'),(19,'b','b','b','b','bb','b','b','bb'),(20,'sad','ads','dsa','ads','sad','adsads','dsa','ads');
/*!40000 ALTER TABLE `msg` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parts`
--

LOCK TABLES `parts` WRITE;
/*!40000 ALTER TABLE `parts` DISABLE KEYS */;
INSERT INTO `parts` VALUES (1,'1','1','2017-09-19 08:07:59','2017-09-19 08:24:40',11,20,'威信','1'),(2,'1','1','2017-09-19 08:07:59','2017-10-08 15:17:47',11,20,'None',''),(3,'１','１','2017-09-24 14:28:11','2017-10-08 16:32:22',5,20,'None',''),(4,'速度','的','2017-10-08 15:44:48',NULL,10,NULL,NULL,'');
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
  `username` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL,
  `power` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'usr1','pwd1','admin'),(2,'usr2','pwd2','normal');
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

-- Dump completed on 2017-10-09 22:02:58
