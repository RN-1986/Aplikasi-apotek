# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardKasir.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout, QHeaderView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(962, 601)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 65))
        self.textBrowser.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.textBrowser)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab {       \n"
"	\n"
"	\n"
"	background-color: rgb(125, 192, 211);\n"
"         padding: 8px 20px;\n"
"         border-radius: 6px;\n"
"         margin-right: 5px;\n"
"       }\n"
"       QTabBar::tab:selected {\n"
"	background-color: rgb(48, 93, 124);\n"
"	color: rgb(255, 255, 255);\n"
"       }\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    /* samakan dengan QWidget */\n"
"	\n"
"	background-color: rgb(125, 202, 211);\n"
"}\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(125, 202, 211);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(173, 216, 230);\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(186)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 450))
        self.frame.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_Batalkan = QPushButton(self.frame)
        self.pushButton_Batalkan.setObjectName(u"pushButton_Batalkan")
        self.pushButton_Batalkan.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 8px 20px; \n"
"	background-color: rgb(255, 0, 0);\n"
"    color: white;\n"
"min-width: 60px;\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"background-color:rgb(213, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"background-color: rgb(213, 0, 0);\n"
"	color: white;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_Batalkan, 2, 4, 1, 1)

        self.pushButton_Bayar = QPushButton(self.frame)
        self.pushButton_Bayar.setObjectName(u"pushButton_Bayar")
        self.pushButton_Bayar.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(49, 245, 46);\n"
"	border-radius: 5px;\n"
"padding: 8px 8px; \n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	background-color: rgb(85, 255, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"		background-color: rgb(85, 255, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_Bayar, 2, 3, 1, 1)

        self.pushButton_lihatDetail = QPushButton(self.frame)
        self.pushButton_lihatDetail.setObjectName(u"pushButton_lihatDetail")
        self.pushButton_lihatDetail.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 79, 124);\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 79, 124);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_lihatDetail, 2, 2, 1, 1)

        self.pushButton_refresh = QPushButton(self.frame)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 79, 124);\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(36, 79, 124);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_refresh, 2, 1, 1, 1)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(125, 202, 211);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(173, 216, 230);\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(185)

        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_keluar.setFont(font)
        self.pushButton_keluar.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"	background-color: rgb(255, 0, 0);\n"
"    color: white;\n"
"padding: 6px 20px;\n"
"    min-width: 100px;\n"
"    max-width: 200px;\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"background-color:rgb(213, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"background-color: rgb(213, 0, 0);\n"
"	color: white;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_keluar, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 962, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">DASHBOARD</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">KASIR</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total Harga (Rp)", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nama Apoteker", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Daftar Keranjang Dikirim", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID Transaksi", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Total Harga (Rp)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Riwayat Transaksi Hari Ini", None))
        self.pushButton_Batalkan.setText(QCoreApplication.translate("MainWindow", u"Batalkan Pemesanan", None))
        self.pushButton_Bayar.setText(QCoreApplication.translate("MainWindow", u"Bayar", None))
        self.pushButton_lihatDetail.setText(QCoreApplication.translate("MainWindow", u"Lihat Detail", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi


from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QDialog, QVBoxLayout, QLabel
from backend.kasir import (
    lihatDaftarKeranjangDikirim, lihatDetailKeranjangUntukKasir,
    kondisiTransaksi, hapusItemDiKasir, cariKeranjangByJam
)
from backend.login import session
from datetime import datetime

class DashboardKasir(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Koneksi tombol logout
        if hasattr(self.ui, "pushButton_keluar"):
            self.ui.pushButton_keluar.clicked.connect(self.logout_to_login)
        
        # Koneksi tombol di tab Daftar Keranjang Dikirim
        if hasattr(self.ui, "pushButton_refresh"):
            self.ui.pushButton_refresh.clicked.connect(self.refresh_keranjang_dikirim)
        if hasattr(self.ui, "pushButton_lihatDetail"):
            self.ui.pushButton_lihatDetail.clicked.connect(self.lihat_detail_keranjang)
        if hasattr(self.ui, "pushButton_Bayar"):
            self.ui.pushButton_Bayar.clicked.connect(self.proses_bayar)
        if hasattr(self.ui, "pushButton_Batalkan"):
            self.ui.pushButton_Batalkan.clicked.connect(self.batalkan_keranjang)
        
        # Tampilkan info user
        try:
            username = session.get('dataUser', {}).get('username', 'Kasir')
            self.ui.textBrowser.setHtml(f"<h2 style='text-align:center'>DASHBOARD KASIR</h2><p style='text-align:center'>Selamat Datang, {username}</p>")
        except Exception:
            pass
        
        # Load data awal
        self.refresh_keranjang_dikirim()
        self.refresh_riwayat_transaksi()
    
    def refresh_keranjang_dikirim(self):
        """Load data keranjang dengan status dikirim"""
        try:
            if not hasattr(self.ui, 'tableWidget'):
                return
            
            self.ui.tableWidget.setRowCount(0)
            data = lihatDaftarKeranjangDikirim()
            
            if data and not isinstance(data, str) and len(data) > 0:
                if isinstance(data, str):
                    QMessageBox.information(self, "Info", data)
                    return
                
                if not data or len(data) == 0:
                    QMessageBox.information(self, "Info", "Belum ada keranjang yang dikirim dari apoteker")
                    return
                
                for i, d in enumerate(data):
                    row = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row)
                    
                    if isinstance(d, dict):
                        keranjang_id = d.get('keranjangId', '')
                        nama_pembeli = d.get('namaPembeli', '')
                        total_harga = float(d.get('totalHarga', 0))
                        nama_apoteker = d.get('namaApoteker', '')
                        status = d.get('status', '')
                        
                        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(keranjang_id)))
                        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(nama_pembeli)))
                        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {total_harga:,.0f}"))
                        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(nama_apoteker)))
                        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(status)))
                    else:
                        # Tuple format: keranjangId, namaPembeli, totalHarga, namaApoteker, status, tanggalDibuat
                        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d[0])))
                        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d[1])))
                        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {float(d[2]):,.0f}"))
                        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d[3])))
                        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d[4])))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load data: {e}")
    
    def refresh_riwayat_transaksi(self):
        """Load data transaksi hari ini (status bayar)"""
        try:
            if hasattr(self.ui, 'tableWidget_2'):
                self.ui.tableWidget_2.setRowCount(0)
                
                # Import dari kasir untuk dapat transaksi hari ini
                from backend.koneksi import koneksiKeDatabase
                db = koneksiKeDatabase()
                if db is None:
                    return
                
                cursor = db.cursor()
                # Ambil transaksi hari ini dan sertakan status + kategori obat pada transaksi
                query = """
                    SELECT 
                        t.tanggalTransaksi,
                        t.transaksiId,
                        k.namaPembeli,
                        k.status AS status,
                        t.totalHarga
                    FROM transaksi t
                    JOIN keranjang k ON k.keranjangId = t.keranjangId
                    WHERE DATE(t.tanggalTransaksi) = CURDATE()
                    ORDER BY t.tanggalTransaksi DESC
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                db.close()
                
                for d in data:
                    row = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row)
                    
                    if isinstance(d, dict):
                        tanggal = d.get('tanggalTransaksi', '')
                        if isinstance(tanggal, datetime):
                            tanggal_str = tanggal.strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            tanggal_str = str(tanggal)
                        
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(tanggal_str))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d.get('transaksiId', ''))))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d.get('namaPembeli', ''))))
                        # Show status column (human readable)
                        status_val = d.get('status', '')
                        # Map status 'bayar' -> 'Lunas' for display if desired
                        if status_val == 'bayar':
                            status_display = 'Lunas'
                        else:
                            status_display = str(status_val).capitalize() if status_val else '-'
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(status_display))
                        total = d.get('totalHarga', 0)
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(f"Rp {total:,.0f}"))
                    else:
                        tanggal = d[0]
                        if isinstance(tanggal, datetime):
                            tanggal_str = tanggal.strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            tanggal_str = str(tanggal)
                        
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(tanggal_str))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d[1])))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d[2])))
                        # d[3] = status, d[4] = total
                        status_val = d[3]
                        status_display = 'Lunas' if status_val == 'bayar' else (str(status_val).capitalize() if status_val else '-')
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(status_display))
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(f"Rp {d[4]:,.0f}"))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load riwayat: {e}")
    
    def lihat_detail_keranjang(self):
        """Buka window detail keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang ingin dilihat detailnya!")
                return
            
            # Ambil keranjangId dari kolom pertama
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            
            from detailKeranjangKasir import DetailKeranjangKasir
            self.detail_window = DetailKeranjangKasir(keranjang_id, parent=self)
            self.detail_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal membuka detail: {e}")
    
    def proses_bayar(self):
        """Proses pembayaran dan tampilkan struk"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan dibayar!")
                return
            
            # Ambil data keranjang
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_pembeli = self.ui.tableWidget.item(selected, 1).text()
            total_harga_str = self.ui.tableWidget.item(selected, 2).text()
            
            # Konfirmasi pembayaran
            reply = QMessageBox.question(
                self,
                "Konfirmasi Pembayaran",
                f"Proses pembayaran untuk {nama_pembeli}?\nTotal: {total_harga_str}",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                # Ambil detail keranjang
                detail_data = lihatDetailKeranjangUntukKasir(keranjang_id)
                
                if isinstance(detail_data, str):
                    QMessageBox.warning(self, "Error", detail_data)
                    return
                
                # Proses bayar
                pesan = kondisiTransaksi(keranjang_id, "dibayar")
                
                # Tampilkan struk
                self.tampilkan_struk(detail_data)
                
                # Refresh data
                self.refresh_keranjang_dikirim()
                self.refresh_riwayat_transaksi()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal proses bayar: {e}")
    
    def tampilkan_struk(self, data_keranjang):
        """Tampilkan struk pembelian dalam popup"""
        try:
            # Buat dialog struk
            dialog = QDialog(self)
            dialog.setWindowTitle("Struk Pembelian")
            dialog.setMinimumWidth(400)
            
            layout = QVBoxLayout()
            
            # Header struk
            now = datetime.now()
            struk_text = f"""
            <div style='font-family: Courier New; padding: 20px;'>
                <h2 style='text-align: center; margin: 0;'>APOTEK PRIMA</h2>
                <p style='text-align: center; margin: 5px 0;'>Jl Hayam Wuruk, No.20C, Balowerti, Kota Kediri</p>
                <p style='text-align: center; margin: 5px 0;'>Telp: (+62) 83863901736</p>
                <hr style='border: 1px dashed #000;'>
                
                <p style='margin: 5px 0;'>Tanggal: {now.strftime('%d-%m-%Y %H:%M:%S')}</p>
                <p style='margin: 5px 0;'>Kasir: {session.get('dataUser', {}).get('username', 'Kasir')}</p>
                <p style='margin: 5px 0;'>Pembeli: {data_keranjang.get('namaPembeli', '-')}</p>
                <p style='margin: 5px 0;'>Apoteker: {data_keranjang.get('namaApoteker', '-')}</p>
                <hr style='border: 1px dashed #000;'>
                
                <table style='width: 100%; border-collapse: collapse;'>
                    <tr>
                        <th style='text-align: left; padding: 5px 0;'>Item</th>
                        <th style='text-align: center;'>Jml</th>
                        <th style='text-align: right;'>Harga</th>
                        <th style='text-align: right;'>Subtotal</th>
                    </tr>
            """
            
            # Detail items
            total = 0
            for item in data_keranjang.get('detail', []):
                if isinstance(item, dict):
                    nama = item.get('namaObat', '').title()
                    jumlah = item.get('jumlah', 0)
                    subtotal = item.get('subtotal', 0)
                else:
                    nama = (item[2] if len(item) > 2 else '').title()
                    jumlah = item[4] if len(item) > 4 else 0
                    subtotal = item[5] if len(item) > 5 else 0
                
                # Hitung harga per unit
                harga_per_unit = float(subtotal) / float(jumlah) if float(jumlah) > 0 else 0
                total += float(subtotal)
                struk_text += f"""
                    <tr>
                        <td style='padding: 3px 0;'>{nama}</td>
                        <td style='text-align: center;'>{jumlah}</td>
                        <td style='text-align: right;'>Rp {harga_per_unit:,.0f}</td>
                        <td style='text-align: right;'>Rp {subtotal:,.0f}</td>
                    </tr>
                """
            
            # Footer struk
            struk_text += f"""
                </table>
                <hr style='border: 1px dashed #000;'>
                <h3 style='text-align: right; margin: 10px 0;'>TOTAL: Rp {total:,.0f}</h3>
                <hr style='border: 1px dashed #000;'>
                <p style='text-align: center; margin-top: 20px;'>Terima Kasih</p>
                <p style='text-align: center;'>Semoga Lekas Sembuh</p>
            </div>
            """
            
            # Label untuk menampilkan struk
            label = QLabel(struk_text)
            label.setWordWrap(True)
            layout.addWidget(label)
            
            # Tombol tutup
            from PySide6.QtWidgets import QPushButton
            btn_close = QPushButton("Tutup")
            btn_close.clicked.connect(dialog.close)
            btn_close.setStyleSheet("""
                QPushButton {
                    background-color: rgb(125, 202, 211);
                    color: black;
                    border-radius: 5px;
                    padding: 8px 20px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: rgb(36, 79, 124);
                    color: white;
                }
            """)
            layout.addWidget(btn_close)
            
            dialog.setLayout(layout)
            dialog.exec()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal tampilkan struk: {e}")
    
    def batalkan_keranjang(self):
        """Batalkan keranjang yang dipilih"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan dibatalkan!")
                return
            
            # Ambil data keranjang
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_pembeli = self.ui.tableWidget.item(selected, 1).text()
            
            # Konfirmasi pembatalan
            reply = QMessageBox.question(
                self,
                "Konfirmasi Pembatalan",
                f"Yakin ingin membatalkan pesanan {nama_pembeli}?\nStok obat akan dikembalikan.",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = kondisiTransaksi(keranjang_id, "dibatalkan")
                QMessageBox.information(self, "Info", pesan)
                
                # Refresh data
                self.refresh_keranjang_dikirim()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal batalkan keranjang: {e}")

    def logout_to_login(self):
        """Logout dan kembali ke halaman login"""
        try:
            from backend.logout import logout as backend_logout
            pesan = backend_logout()
            QMessageBox.information(self, "Logout", pesan)
        except Exception:
            pass
        
        try:
            self.close()
        except Exception:
            pass
        
        try:
            from Login import Ui_MainWindow as Ui_Login
            self._login_win = QMainWindow()
            self._login_ui = Ui_Login()
            self._login_ui.setupUi(self._login_win)
            self._login_win.show()
        except Exception:
            pass
