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

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(191) NOT NULL,
  `full_name` varchar(191) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_customers_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `customers` */

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `detailtransaksi` */

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `keranjang` */

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `keranjangdetail` */

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `obat` */

insert  into `obat`(`obatId`,`namaObat`,`jenis`,`harga`,`stok`,`kadaluarsa`,`createdAt`) values 
(1,'w3er','incar',3.00,534,NULL,'2025-10-19 11:42:41'),
(6,'12elprimo','super',23.00,72,'2029-08-13','2025-10-18 12:41:14');

/*Table structure for table `order_items` */

DROP TABLE IF EXISTS `order_items`;

CREATE TABLE `order_items` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `order_id` bigint unsigned NOT NULL,
  `product_id` bigint unsigned NOT NULL,
  `qty` int NOT NULL,
  `price_cents` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_items_order` (`order_id`),
  KEY `idx_items_product` (`product_id`),
  CONSTRAINT `fk_items_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `fk_items_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `order_items` */

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` bigint unsigned NOT NULL,
  `status` enum('pending','paid','shipped','cancelled') NOT NULL,
  `ordered_at` datetime NOT NULL,
  `total_cents` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_orders_customer_status_date` (`customer_id`,`status`,`ordered_at`),
  CONSTRAINT `fk_orders_customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `orders` */

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `sku` varchar(64) NOT NULL,
  `name` varchar(191) NOT NULL,
  `price_cents` int NOT NULL,
  `category_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_products_sku` (`sku`),
  KEY `idx_products_category_created` (`category_id`,`created_at`),
  KEY `idx_products_price` (`price_cents`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `products` */

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`userId`,`nama`,`username`,`password`,`role`,`createdAt`) values 
(1,'aku','anjai','1221','admin','2025-10-17 18:09:37'),
(2,'ayu','weru','123','admin','2025-10-18 12:37:40'),
(3,'aw','a','123','admin','2025-10-18 12:42:40'),
(4,'qwe','12','$2b$12$kmQoGw7BUSbTyOTWp31N1ejs0q6ez.Svjb1OM.C.2ibvvBGBK45pC','admin','2025-10-18 13:09:04'),
(5,'2','we','$2b$12$./ItsfLwbrZ21PZiDJ5IZun.ojqMF5GVRW2/WMQSF4l2w5D9.pEca','apoteker','2025-10-19 10:46:19');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
