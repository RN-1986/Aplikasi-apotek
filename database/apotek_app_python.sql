/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 8.0.30 : Database - apotek_app_python
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`apotek_app_python` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `apotek_app_python`;

/*Table structure for table `detailtransaksi` */

DROP TABLE IF EXISTS `detailtransaksi`;

CREATE TABLE `detailtransaksi` (
  `detailId` int NOT NULL AUTO_INCREMENT,
  `transaksiId` int DEFAULT NULL,
  `obatId` int DEFAULT NULL,
  `jumlah` int DEFAULT NULL,
  `subtotal` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`detailId`),
  KEY `transaksiId` (`transaksiId`),
  KEY `obatId` (`obatId`),
  CONSTRAINT `detailtransaksi_ibfk_1` FOREIGN KEY (`transaksiId`) REFERENCES `transaksi` (`transaksiId`),
  CONSTRAINT `detailtransaksi_ibfk_2` FOREIGN KEY (`obatId`) REFERENCES `obat` (`obatId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `detailtransaksi` */

/*Table structure for table `obat` */

DROP TABLE IF EXISTS `obat`;

CREATE TABLE `obat` (
  `obatId` int NOT NULL AUTO_INCREMENT,
  `namaObat` varchar(100) NOT NULL,
  `jenis` varchar(50) DEFAULT NULL,
  `harga` decimal(10,2) NOT NULL,
  `stok` int DEFAULT '0',
  `kadaluarsa` date DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`obatId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `obat` */

insert  into `obat`(`obatId`,`namaObat`,`jenis`,`harga`,`stok`,`kadaluarsa`,`createdAt`) values 
(4,'abi','super',23.00,78,'2029-08-13','2025-10-17 17:20:18');

/*Table structure for table `transaksi` */

DROP TABLE IF EXISTS `transaksi`;

CREATE TABLE `transaksi` (
  `transaksiId` int NOT NULL AUTO_INCREMENT,
  `tanggalTransaksi` datetime DEFAULT CURRENT_TIMESTAMP,
  `kasirId` int DEFAULT NULL,
  `totalHarga` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`transaksiId`),
  KEY `kasirId` (`kasirId`),
  CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`kasirId`) REFERENCES `user` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `transaksi` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','kasir','apoteker') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'apoteker',
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`userId`,`nama`,`username`,`password`,`role`,`createdAt`) values 
(1,'aku','anjai','1221','admin','2025-10-17 18:09:37');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
