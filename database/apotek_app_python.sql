/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 8.0.43 : Database - apotek_app_python
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
  `subtotal` decimal(12,2) DEFAULT '0.00',
  PRIMARY KEY (`detailId`),
  KEY `transaksiId` (`transaksiId`),
  KEY `obatId` (`obatId`),
  CONSTRAINT `detailtransaksi_ibfk_1` FOREIGN KEY (`transaksiId`) REFERENCES `transaksi` (`transaksiId`),
  CONSTRAINT `detailtransaksi_ibfk_2` FOREIGN KEY (`obatId`) REFERENCES `obat` (`obatId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `detailtransaksi` */

insert  into `detailtransaksi`(`detailId`,`transaksiId`,`obatId`,`jumlah`,`subtotal`) values 
(1,1,1,21,63.00),
(2,1,6,2,46.00),
(3,2,7,1,10000.00),
(4,3,1,1,3.00),
(5,4,6,12,27600.00),
(6,5,26,2,70000.00),
(7,5,30,2,24000.00),
(8,6,51,3,36000.00),
(9,6,58,2,13000.00),
(10,7,99,2,28000.00),
(11,7,16,12,24000.00);

/*Table structure for table `kategoriobat` */

DROP TABLE IF EXISTS `kategoriobat`;

CREATE TABLE `kategoriobat` (
  `kategoriId` int NOT NULL AUTO_INCREMENT,
  `namaKategori` varchar(100) NOT NULL,
  PRIMARY KEY (`kategoriId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `kategoriobat` */

insert  into `kategoriobat`(`kategoriId`,`namaKategori`) values 
(1,'Obat Bebas'),
(2,'Obat Bebas Terbatas'),
(3,'Obat Keras'),
(4,'Obat Narkotika & Psikotropika');

/*Table structure for table `keranjang` */

DROP TABLE IF EXISTS `keranjang`;

CREATE TABLE `keranjang` (
  `keranjangId` int NOT NULL AUTO_INCREMENT,
  `apotekerId` int DEFAULT NULL,
  `namaPembeli` varchar(100) DEFAULT NULL,
  `totalHarga` decimal(12,2) DEFAULT '0.00',
  `status` enum('draft','dikirim','dibatalkan','bayar') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'draft',
  `tanggalDibuat` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`keranjangId`),
  KEY `apotekerId` (`apotekerId`),
  CONSTRAINT `keranjang_ibfk_1` FOREIGN KEY (`apotekerId`) REFERENCES `user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `keranjang` */

insert  into `keranjang`(`keranjangId`,`apotekerId`,`namaPembeli`,`totalHarga`,`status`,`tanggalDibuat`) values 
(7,10,'budiono siregar',109.00,'bayar','2025-10-27 12:19:16'),
(9,10,'we',10000.00,'bayar','2025-10-27 13:00:20'),
(11,10,'su',3.00,'bayar','2025-10-27 13:00:36'),
(16,13,'sa',27600.00,'bayar','2025-12-12 17:02:31'),
(20,13,'nova',94000.00,'bayar','2025-12-13 20:43:47'),
(21,13,'nova',20000.00,'dibatalkan','2025-12-13 21:38:35'),
(22,13,'mawar',49000.00,'bayar','2025-12-13 22:09:15'),
(23,13,'tama',52000.00,'bayar','2025-12-13 22:53:54');

/*Table structure for table `keranjangdetail` */

DROP TABLE IF EXISTS `keranjangdetail`;

CREATE TABLE `keranjangdetail` (
  `detailKeranjangId` int NOT NULL AUTO_INCREMENT,
  `keranjangId` int DEFAULT NULL,
  `obatId` int DEFAULT NULL,
  `jumlah` int DEFAULT NULL,
  `subtotal` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`detailKeranjangId`),
  KEY `keranjangId` (`keranjangId`),
  KEY `obatId` (`obatId`),
  CONSTRAINT `keranjangdetail_ibfk_1` FOREIGN KEY (`keranjangId`) REFERENCES `keranjang` (`keranjangId`),
  CONSTRAINT `keranjangdetail_ibfk_2` FOREIGN KEY (`obatId`) REFERENCES `obat` (`obatId`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `keranjangdetail` */

insert  into `keranjangdetail`(`detailKeranjangId`,`keranjangId`,`obatId`,`jumlah`,`subtotal`) values 
(9,7,1,21,63.00),
(10,7,6,2,46.00),
(11,9,7,1,10000.00),
(12,11,1,1,3.00),
(13,16,6,12,27600.00),
(19,20,26,2,70000.00),
(20,20,30,2,24000.00),
(21,21,7,2,16000.00),
(22,21,16,2,4000.00),
(23,22,51,3,36000.00),
(24,22,58,2,13000.00),
(25,23,99,2,28000.00),
(26,23,16,12,24000.00);

/*Table structure for table `obat` */

DROP TABLE IF EXISTS `obat`;

CREATE TABLE `obat` (
  `obatId` int NOT NULL AUTO_INCREMENT,
  `namaObat` varchar(100) NOT NULL,
  `jenis` varchar(50) DEFAULT NULL,
  `kategoriId` int DEFAULT NULL,
  `harga` decimal(10,2) NOT NULL,
  `stok` int DEFAULT '0',
  `tgl_produksi` date DEFAULT NULL,
  `kadaluarsa` date DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`obatId`),
  KEY `fk_obat_kategori` (`kategoriId`),
  CONSTRAINT `fk_obat_kategori` FOREIGN KEY (`kategoriId`) REFERENCES `kategoriobat` (`kategoriId`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `obat` */

insert  into `obat`(`obatId`,`namaObat`,`jenis`,`kategoriId`,`harga`,`stok`,`tgl_produksi`,`kadaluarsa`,`createdAt`) values 
(1,'Simvastatin 20mg','Tablet',3,21000.00,130,'2024-04-05','2027-04-05','2025-10-19 11:42:41'),
(6,'MST Continus (Morphine)','Tablet',4,120000.00,26,'2023-08-20','2026-08-20','2025-10-18 12:41:14'),
(7,'Amoxicillin 500mg','Kapsul',3,8000.00,124,'2023-11-20','2026-11-20','2025-10-27 12:35:44'),
(8,'Paracetamol 500mg','Tablet',1,3500.00,250,'2024-01-15','2027-01-15','2025-12-11 21:51:17'),
(12,'OBH Combi Anak','Sirup',2,18500.00,85,'2024-03-10','2026-03-10','2025-12-12 12:08:22'),
(13,'Asam Mefenamat','Tablet',3,4500.00,150,'2024-02-05','2027-02-05','2025-12-12 12:09:15'),
(16,'Vitacimin C 500mg','Tablet',1,2000.00,488,'2024-05-12','2026-05-12','2025-12-13 00:45:16'),
(17,'CTM (Chlorpheniramine)','Tablet',2,1500.00,300,'2023-12-01','2026-12-01','2025-12-13 00:45:58'),
(18,'Ibuprofen Sirup','Sirup',2,22000.00,60,'2024-04-18','2026-04-18','2025-12-13 00:46:40'),
(19,'Amlodipine 10mg','Tablet',3,15000.00,90,'2023-10-10','2026-10-10','2025-12-13 00:47:47'),
(20,'Alprazolam 1mg','Tablet',4,45000.00,40,'2024-01-20','2027-01-20','2025-12-13 00:49:03'),
(21,'Codeine 10mg','Tablet',4,65000.00,25,'2023-09-15','2026-09-15','2025-12-13 00:49:44'),
(22,'Antasida Doen','Tablet',1,3000.00,200,'2024-06-01','2027-06-01','2025-12-13 00:50:27'),
(23,'Ambroxol HCL','Sirup',3,12500.00,75,'2024-02-28','2026-02-28','2025-12-13 00:51:43'),
(24,'Omeprazole 20mg','Kapsul',3,14000.00,110,'2023-12-15','2026-12-15','2025-12-13 00:53:14'),
(25,'Sanmol Sirup','Sirup',1,25000.00,95,'2024-05-20','2027-05-20','2025-12-13 00:54:13'),
(26,'Betadine Gargle','Sirup (Cair)',2,35000.00,48,'2023-11-05','2026-11-05','2025-12-13 00:55:20'),
(27,'Diazepam 2mg','Tablet',4,38000.00,35,'2024-03-01','2027-03-01','2025-12-13 00:56:20'),
(28,'Metformin 500mg','Tablet',3,10000.00,180,'2024-01-10','2027-01-10','2025-12-13 00:57:25'),
(29,'Curcuma Plus','Sirup',1,19500.00,100,'2024-07-01','2026-07-01','2025-12-13 00:58:28'),
(30,'Panadol Extra','Tablet',1,12000.00,198,'2024-02-10','2027-02-10','2025-12-13 16:27:12'),
(31,'Cefadroxil 500mg','Kapsul',3,11500.00,140,'2023-11-25','2026-11-25','2025-12-13 16:30:40'),
(32,'Siladex Cough & Cold','Sirup',2,16000.00,80,'2024-04-05','2027-04-05','2025-12-13 16:51:07'),
(34,'Ranitidine 150mg','Tablet',3,3000.00,160,'2024-01-15','2027-01-15','2025-12-13 21:18:13'),
(35,'Diapet','Kapsul',1,4500.00,110,'2024-06-10','2027-06-10','2025-12-13 21:18:13'),
(36,'Tremenza Sirup','Sirup',3,28000.00,60,'2023-12-20','2026-12-20','2025-12-13 21:18:13'),
(37,'Neuralgin RX','Tablet',3,25000.00,90,'2024-03-12','2027-03-12','2025-12-13 21:18:13'),
(38,'Imboost Force','Tablet',1,45000.00,75,'2024-05-01','2026-05-01','2025-12-13 21:18:13'),
(39,'Braxidin','Tablet',4,55000.00,30,'2023-10-05','2026-10-05','2025-12-13 21:18:13'),
(40,'Codipront','Kapsul',4,85000.00,20,'2023-09-10','2026-09-10','2025-12-13 21:18:13'),
(41,'Mylanta Cair','Sirup',1,17500.00,120,'2024-02-28','2026-02-28','2025-12-13 21:18:13'),
(42,'Cetirizine Sirup','Sirup',3,22000.00,65,'2024-03-20','2026-03-20','2025-12-13 21:18:13'),
(43,'Lansoprazole 30mg','Kapsul',3,18000.00,100,'2023-12-05','2026-12-05','2025-12-13 21:18:13'),
(44,'Bodrex Migra','Tablet',2,3500.00,250,'2024-07-15','2027-07-15','2025-12-13 21:18:13'),
(45,'Rhinos SR','Kapsul',3,65000.00,50,'2023-11-15','2026-11-15','2025-12-13 21:18:13'),
(46,'Valisanbe 5mg','Tablet',4,42000.00,40,'2024-01-25','2027-01-25','2025-12-13 21:18:13'),
(47,'New Diatabs','Tablet',1,4000.00,180,'2024-04-10','2027-04-10','2025-12-13 21:18:13'),
(48,'Stimuno Sirup','Sirup',1,28500.00,70,'2024-05-05','2026-05-05','2025-12-13 21:18:13'),
(49,'Fentanyl 100mcg','Tablet',4,150000.00,10,'2023-08-15','2026-08-15','2025-12-13 21:18:13'),
(50,'Spasminal','Tablet',3,12000.00,130,'2024-02-18','2027-02-18','2025-12-13 21:18:13'),
(51,'Ciprofloxacin 500mg','Tablet',3,12000.00,147,'2024-01-10','2027-01-10','2025-12-13 21:21:56'),
(52,'Azithromycin 500mg','Tablet',3,18000.00,100,'2023-11-05','2026-11-05','2025-12-13 21:21:56'),
(53,'Methylprednisolone 4mg','Tablet',3,6000.00,300,'2024-03-01','2027-03-01','2025-12-13 21:21:56'),
(54,'Polysilane Cair','Sirup',1,28000.00,80,'2024-05-15','2026-05-15','2025-12-13 21:21:56'),
(55,'Captopril 25mg','Tablet',3,2500.00,400,'2024-02-20','2027-02-20','2025-12-13 21:21:56'),
(56,'Bisolvon Extra','Sirup',2,42000.00,60,'2023-12-10','2026-12-10','2025-12-13 21:21:56'),
(57,'Candesartan 8mg','Tablet',3,5000.00,250,'2024-04-05','2027-04-05','2025-12-13 21:21:56'),
(58,'Enervon C','Tablet',1,6500.00,498,'2024-06-01','2026-06-01','2025-12-13 21:21:56'),
(59,'Dextral','Tablet',2,3500.00,180,'2023-10-25','2026-10-25','2025-12-13 21:21:56'),
(60,'Riklona 2mg (Clonazepam)','Tablet',4,55000.00,30,'2024-01-15','2027-01-15','2025-12-13 21:21:56'),
(61,'Pethidine Injection','Kapsul',4,120000.00,10,'2023-09-01','2025-09-01','2025-12-13 21:21:56'),
(62,'Sukralfat Suspensi','Sirup',3,24000.00,90,'2024-02-12','2026-02-12','2025-12-13 21:21:56'),
(63,'Glimepiride 2mg','Tablet',3,8000.00,200,'2024-03-20','2027-03-20','2025-12-13 21:21:56'),
(64,'Bisoprolol 5mg','Tablet',3,9000.00,180,'2023-11-30','2026-11-30','2025-12-13 21:21:56'),
(65,'Tempra Drops','Sirup',1,48000.00,50,'2024-05-10','2026-05-10','2025-12-13 21:21:56'),
(66,'Sumagesic','Tablet',1,3000.00,300,'2024-01-05','2027-01-05','2025-12-13 21:21:56'),
(67,'Doxycycline 100mg','Kapsul',3,7500.00,120,'2023-12-05','2026-12-05','2025-12-13 21:21:56'),
(68,'Esilgan (Estazolam)','Tablet',4,60000.00,25,'2024-02-01','2027-02-01','2025-12-13 21:21:56'),
(69,'Durogesic (Fentanyl)','Tablet',4,250000.00,5,'2023-08-10','2025-08-10','2025-12-13 21:21:56'),
(70,'Proris Sirup','Sirup',2,32000.00,75,'2024-04-15','2026-04-15','2025-12-13 21:21:56'),
(71,'Becom-Zet','Tablet',1,28000.00,150,'2024-03-10','2026-03-10','2025-12-13 21:21:56'),
(72,'Allopurinol 100mg','Tablet',3,2000.00,220,'2024-01-25','2027-01-25','2025-12-13 21:21:56'),
(73,'Salbutamol 2mg','Tablet',3,1500.00,180,'2023-10-15','2026-10-15','2025-12-13 21:21:56'),
(74,'Decolgen','Tablet',2,2500.00,300,'2024-06-20','2027-06-20','2025-12-13 21:21:56'),
(75,'Ketoconazole 200mg','Tablet',3,5500.00,100,'2023-12-15','2026-12-15','2025-12-13 21:21:56'),
(76,'Zink Tablet','Tablet',1,1000.00,400,'2024-05-01','2026-05-01','2025-12-13 21:21:56'),
(77,'Caviplex','Kapsul',1,4000.00,250,'2024-02-28','2026-02-28','2025-12-13 21:21:56'),
(78,'Clindamycin 300mg','Kapsul',3,14000.00,110,'2024-01-18','2027-01-18','2025-12-13 21:21:56'),
(79,'Dumolid 5mg','Tablet',4,75000.00,20,'2023-09-20','2026-09-20','2025-12-13 21:21:56'),
(80,'Oxcontin','Tablet',4,180000.00,8,'2023-07-15','2025-07-15','2025-12-13 21:21:56'),
(81,'Vicks Formula 44','Sirup',2,21000.00,95,'2024-04-10','2026-04-10','2025-12-13 21:21:56'),
(82,'Acyclovir 400mg','Tablet',3,8500.00,130,'2023-11-20','2026-11-20','2025-12-13 21:21:56'),
(83,'Meloxicam 15mg','Tablet',3,6500.00,140,'2024-03-05','2027-03-05','2025-12-13 21:21:56'),
(84,'Furosemide 40mg','Tablet',3,1800.00,160,'2024-01-30','2027-01-30','2025-12-13 21:21:56'),
(85,'Elkana','Sirup',1,35000.00,70,'2024-05-25','2026-05-25','2025-12-13 21:21:56'),
(86,'Incidal-OD','Kapsul',3,26000.00,85,'2023-12-01','2026-12-01','2025-12-13 21:21:56'),
(87,'Atorvastatin 20mg','Tablet',3,18500.00,115,'2024-02-15','2027-02-15','2025-12-13 21:21:56'),
(88,'Xanax 0.5mg','Tablet',4,50000.00,35,'2024-01-12','2027-01-12','2025-12-13 21:21:56'),
(89,'Morfin Sulfat 10mg','Tablet',4,95000.00,12,'2023-10-10','2026-10-10','2025-12-13 21:21:56'),
(90,'Ozen (Cetirizine)','Sirup',3,45000.00,55,'2024-04-20','2026-04-20','2025-12-13 21:21:56'),
(91,'Hufagripp Flu','Sirup',2,15000.00,150,'2024-06-05','2026-06-05','2025-12-13 21:21:56'),
(92,'Cefixime 100mg','Kapsul',3,12000.00,120,'2023-11-10','2026-11-10','2025-12-13 21:21:56'),
(93,'Imodium (Loperamide)','Tablet',3,8000.00,100,'2024-03-15','2027-03-15','2025-12-13 21:21:56'),
(94,'Neurobion Forte','Tablet',1,38000.00,200,'2024-01-05','2026-01-05','2025-12-13 21:21:56'),
(95,'Lacto-B','Kapsul',1,7000.00,300,'2024-05-18','2026-05-18','2025-12-13 21:21:56'),
(96,'Tramadol 50mg','Kapsul',3,6000.00,80,'2023-12-25','2026-12-25','2025-12-13 21:21:56'),
(97,'Valium 5mg','Tablet',4,40000.00,30,'2024-02-05','2027-02-05','2025-12-13 21:21:56'),
(98,'Methadone','Sirup',4,80000.00,15,'2023-08-30','2025-08-30','2025-12-13 21:21:56'),
(99,'Sangobion','Kapsul',1,14000.00,248,'2024-04-01','2026-04-01','2025-12-13 21:21:56'),
(100,'Voltaren 50mg','Tablet',3,9500.00,140,'2024-01-20','2027-01-20','2025-12-13 21:21:56');

/*Table structure for table `transaksi` */

DROP TABLE IF EXISTS `transaksi`;

CREATE TABLE `transaksi` (
  `transaksiId` int NOT NULL AUTO_INCREMENT,
  `tanggalTransaksi` datetime DEFAULT CURRENT_TIMESTAMP,
  `kasirId` int DEFAULT NULL,
  `totalHarga` decimal(12,2) DEFAULT NULL,
  `keranjangId` int DEFAULT NULL,
  PRIMARY KEY (`transaksiId`),
  KEY `kasirId` (`kasirId`),
  CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`kasirId`) REFERENCES `user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `transaksi` */

insert  into `transaksi`(`transaksiId`,`tanggalTransaksi`,`kasirId`,`totalHarga`,`keranjangId`) values 
(1,'2025-10-27 12:27:49',1,109.00,NULL),
(2,'2025-10-27 13:01:11',1,10000.00,NULL),
(3,'2025-10-27 13:01:14',1,3.00,NULL),
(4,'2025-12-13 17:28:01',14,27600.00,16),
(5,'2025-12-13 21:11:53',14,94000.00,20),
(6,'2025-12-13 22:11:09',14,49000.00,22),
(7,'2025-12-13 22:55:18',14,52000.00,23);

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`userId`,`nama`,`username`,`password`,`role`,`createdAt`) values 
(1,'budi','budi','1221','admin','2025-10-17 18:09:37'),
(2,'ayu','weru','123','admin','2025-10-18 12:37:40'),
(3,'aw','a','123','admin','2025-10-18 12:42:40'),
(4,'qwe','12','$2b$12$kmQoGw7BUSbTyOTWp31N1ejs0q6ez.Svjb1OM.C.2ibvvBGBK45pC','admin','2025-10-18 13:09:04'),
(5,'2','we','$2b$12$./ItsfLwbrZ21PZiDJ5IZun.ojqMF5GVRW2/WMQSF4l2w5D9.pEca','apoteker','2025-10-19 10:46:19'),
(6,'Budi','budi001','$2b$12$aIDp6DSOrzJ2cMhD/Au6U.NVNFYsscC3elgliJwOd8rJJewGQTGIq','admin','2025-10-23 09:49:45'),
(7,'krisn','uy','$2b$12$IBy4UyGjWslur90J/v20p.5Cn3MixthFtglcPMLG0pHTsFhjqzk82','kasir','2025-10-23 11:02:11'),
(8,'qw','qwe','$2b$12$PUh2XIqsSA.prlq2QQW1duNTpS7XN1uQ1SfwvK0htntg6ZaTiCywe','apoteker','2025-10-23 20:33:10'),
(9,'a','ad','$2b$12$cyk4zDY6cxGKOa7ttdMW4.r611Z4Mb7lQMqHv5Gzl/8AKvjCuaso2','admin','2025-10-27 12:14:02'),
(10,'ap','ap','$2b$12$qlSrKdEJ/5Sm3B9OwLxdu.0vk0LgFQXoo9zq/JNMV73qbUsfG3XG.','apoteker','2025-10-27 12:19:01'),
(11,'kas','ka','$2b$12$afPzU2Ge5wPr9w0ANmlIb.P2eYU0Fp84r8Pm4EvSdfLwRpgxbZ99i','kasir','2025-10-27 12:19:57'),
(12,'s','s','$2b$12$Wa./Y5AwdGcsozRjOLMSVuYx0rk2qlWsIOGUoK58wzthF.anP7tWy','admin','2025-12-11 20:54:38'),
(13,'q','q','$2b$12$v1bORxSR.Ag7a2B0ZJSg2OiOZ5OGsd7hPmL0hoe87nROWy2xOntyW','apoteker','2025-12-11 20:55:29'),
(14,'w','w','$2b$12$UYivul3yIYnWFSOHATjUEu1OD4IAzd2MIS9sZua/GGcnH6fn4Mn0a','kasir','2025-12-11 21:10:33');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
