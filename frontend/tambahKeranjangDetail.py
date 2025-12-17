# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tambahKeranjangDetail.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        
        # Label Nama Pembeli
        self.label_namaPembeliText = QLabel(self.centralwidget)
        self.label_namaPembeliText.setObjectName(u"label_namaPembeliText")
        font_bold = QFont()
        font_bold.setPointSize(10)
        font_bold.setBold(True)
        self.label_namaPembeliText.setFont(font_bold)
        self.gridLayout.addWidget(self.label_namaPembeliText, 0, 0, 1, 1)
        
        self.label_namaPembeli = QLabel(self.centralwidget)
        self.label_namaPembeli.setObjectName(u"label_namaPembeli")
        self.label_namaPembeli.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 6px 8px;")
        self.gridLayout.addWidget(self.label_namaPembeli, 0, 1, 1, 2)
        
        # Label Instruksi
        self.label_instruksi = QLabel(self.centralwidget)
        self.label_instruksi.setObjectName(u"label_instruksi")
        self.label_instruksi.setStyleSheet(u"color: rgb(50, 50, 50);")
        self.gridLayout.addWidget(self.label_instruksi, 1, 0, 1, 3)
        
        # Tabel Obat
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(173, 216, 230);\n"
"    selection-color: black;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(173, 216, 230);\n"
"    color: black;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(125, 202, 211);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(131)

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 3)
        
        # Button Simpan
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(49, 245, 46);\n"
"	border-radius: 5px;\n"
"padding: 6px 40px; \n"
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
        
        # Button Batal
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 6px 20px;\n"
"    min-width: 100px;\n"
"    max-width: 200px;\n"
"	background-color: rgb(255, 0, 0);\n"
"    color: white;\n"
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
        
        # Label Masukkan Nama Obat
        self.label_namaObat = QLabel(self.centralwidget)
        self.label_namaObat.setObjectName(u"label_namaObat")
        self.gridLayout.addWidget(self.label_namaObat, 3, 0, 1, 1)
        
        # Input Nama Obat
        self.lineEdit_namaObat = QLineEdit(self.centralwidget)
        self.lineEdit_namaObat.setObjectName(u"lineEdit_namaObat")
        self.lineEdit_namaObat.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border-radius: 5px;\n"
"padding: 6px 8px;")
        self.lineEdit_namaObat.setPlaceholderText("Ketik nama obat...")
        self.gridLayout.addWidget(self.lineEdit_namaObat, 3, 1, 1, 1)
        
        # Button Cari
        self.pushButton_cari = QPushButton(self.centralwidget)
        self.pushButton_cari.setObjectName(u"pushButton_cari")
        self.pushButton_cari.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;\n"
"padding: 6px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 190);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 170, 190);\n"
"color: white;\n"
"}")
        self.gridLayout.addWidget(self.pushButton_cari, 3, 2, 1, 1)
        
        # Label Masukkan Jumlah Obat
        self.label_jumlahObat = QLabel(self.centralwidget)
        self.label_jumlahObat.setObjectName(u"label_jumlahObat")
        self.gridLayout.addWidget(self.label_jumlahObat, 4, 0, 1, 1)
        
        # Input Jumlah Obat
        self.lineEdit_jumlahObat = QLineEdit(self.centralwidget)
        self.lineEdit_jumlahObat.setObjectName(u"lineEdit_jumlahObat")
        self.lineEdit_jumlahObat.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border-radius: 5px;\n"
"padding: 6px 8px;")
        self.lineEdit_jumlahObat.setPlaceholderText("Contoh: 5")
        self.gridLayout.addWidget(self.lineEdit_jumlahObat, 4, 1, 1, 2)

        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tambah Obat ke Keranjang", None))
        self.label_namaPembeliText.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        self.label_namaPembeli.setText("")
        self.label_instruksi.setText(QCoreApplication.translate("MainWindow", u"Silahkan pilih obat yang akan ditambah", None))
        self.label_namaObat.setText(QCoreApplication.translate("MainWindow", u"Masukkan Nama Obat  :", None))
        self.pushButton_cari.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        self.label_jumlahObat.setText(QCoreApplication.translate("MainWindow", u"Masukkan Jumlah Obat  :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Kadaluarsa", None));
    # retranslateUi

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QLabel
from PySide6.QtCore import Qt
from backend.apoteker import cariObatLayakJual, tambahObatKeKeranjang, lihatKeranjang

class TambahKeranjangDetailWindow(QMainWindow):
    def __init__(self, keranjang_id, parent=None):
        super().__init__()
        self.parent = parent
        self.keranjang_id = keranjang_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle("Tambah Obat ke Keranjang")
        
        # Load nama pembeli
        self.load_nama_pembeli()
        
        # Load data obat
        self.load_obat_layak_jual()
        
        # Connect buttons
        self.ui.pushButton.clicked.connect(self.simpan_obat)  # Button Simpan
        self.ui.pushButton_2.clicked.connect(self.close)  # Button Batal
        self.ui.pushButton_cari.clicked.connect(self.cari_obat)  # Button Cari
        
        # Double click to select
        self.ui.tableWidget.cellDoubleClicked.connect(self.pilih_obat_dan_simpan)
    
    def load_nama_pembeli(self):
        """Load nama pembeli dari keranjang"""
        try:
            data = lihatKeranjang(self.keranjang_id)
            if isinstance(data, dict):
                nama_pembeli = data.get('namaPembeli', '')
                self.ui.label_namaPembeli.setText(nama_pembeli)
        except Exception as e:
            self.ui.label_namaPembeli.setText("Tidak diketahui")
    
    def cari_obat(self):
        """Cari obat berdasarkan nama"""
        keyword = self.ui.lineEdit_namaObat.text().strip()
        if not keyword:
            QMessageBox.warning(self, "Peringatan", "Masukkan nama obat terlebih dahulu!")
            return
        
        try:
            data = cariObatLayakJual(keyword)
            
            if isinstance(data, str):
                QMessageBox.information(self, "Info", data)
                return
            
            # Tampilkan hasil pencarian
            self.tampilkan_data_obat(data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal cari obat: {e}")
    
    def load_obat_layak_jual(self):
        """Load data obat yang layak jual ke tabel"""
        try:
            data = cariObatLayakJual()  # Ambil semua obat layak jual
            
            if isinstance(data, str):
                QMessageBox.warning(self, "Peringatan", data)
                return
            
            self.tampilkan_data_obat(data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load obat: {e}")
    
    def tampilkan_data_obat(self, data):
        """Tampilkan data obat ke tabel"""
        try:
            self.ui.tableWidget.setRowCount(len(data))
            
            for row_idx, item in enumerate(data):
                if isinstance(item, dict):
                    obat_id = item.get('obatId', '')
                    nama_obat = item.get('namaObat', '')
                    jenis = item.get('jenis', '')
                    kategori = item.get('namaKategori', '-')
                    harga = item.get('harga', 0)
                    stok = item.get('stok', 0)
                    kadaluarsa = item.get('kadaluarsa', '')
                else:
                    # d[0]=obatId, d[1]=namaObat, d[2]=jenis, d[3]=kategoriId, d[4]=harga, d[5]=stok, d[6]=tgl_produksi, d[7]=kadaluarsa, d[8]=namaKategori
                    obat_id = item[0]
                    nama_obat = item[1]
                    jenis = item[2]
                    kategori = item[8] if len(item) > 8 and item[8] else '-'
                    harga = item[4]
                    stok = item[5]
                    kadaluarsa = item[7]
                
                # Kolom: Nama Obat | Jenis | Kategori | Harga | Stok | Kadaluarsa
                # Semua kolom tidak bisa diedit
                item_nama = QTableWidgetItem(str(nama_obat).title())
                item_nama.setData(Qt.UserRole, obat_id)  # Simpan obatId
                item_nama.setFlags(item_nama.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 0, item_nama)
                
                item_jenis = QTableWidgetItem(str(jenis).title() if jenis else "-")
                item_jenis.setFlags(item_jenis.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 1, item_jenis)
                
                item_kategori = QTableWidgetItem(str(kategori))
                item_kategori.setFlags(item_kategori.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 2, item_kategori)
                
                item_harga = QTableWidgetItem(f"Rp {harga:,}")
                item_harga.setFlags(item_harga.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 3, item_harga)
                
                item_stok = QTableWidgetItem(str(stok))
                item_stok.setFlags(item_stok.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 4, item_stok)
                
                item_kadaluarsa = QTableWidgetItem(str(kadaluarsa))
                item_kadaluarsa.setFlags(item_kadaluarsa.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 5, item_kadaluarsa)
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal tampilkan data: {e}")
    
    def pilih_obat_dan_simpan(self, row, column):
        """Double click untuk langsung pilih obat dan input jumlah"""
        self.simpan_obat()
    
    def simpan_obat(self):
        """Simpan obat yang dipilih ke keranjang"""
        try:
            # Validasi obat dipilih
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat dari tabel terlebih dahulu!")
                return
            
            # Ambil obat_id dari data tersembunyi
            obat_id = self.ui.tableWidget.item(selected, 0).data(Qt.UserRole)
            nama_obat = self.ui.tableWidget.item(selected, 0).text()
            
            # Ambil jumlah dari input field
            jumlah_str = self.ui.lineEdit_jumlahObat.text().strip()
            if not jumlah_str:
                QMessageBox.warning(self, "Peringatan", "Jumlah obat harus diisi!")
                return
            
            try:
                jumlah = int(jumlah_str)
                if jumlah <= 0:
                    QMessageBox.warning(self, "Peringatan", "Jumlah harus lebih dari 0!")
                    return
            except ValueError:
                QMessageBox.warning(self, "Peringatan", "Jumlah harus berupa angka!")
                return
            
            # Konfirmasi
            reply = QMessageBox.question(
                self,
                "Konfirmasi",
                f"Tambah {jumlah} {nama_obat} ke keranjang?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                # Tambahkan obat ke keranjang
                pesan = tambahObatKeKeranjang(self.keranjang_id, obat_id, jumlah)
                
                if "berhasil" in pesan.lower() or "sukses" in pesan.lower():
                    QMessageBox.information(self, "Sukses", pesan)
                    
                    # Refresh data di parent
                    if self.parent and hasattr(self.parent, 'load_detail_keranjang'):
                        self.parent.load_detail_keranjang()
                    
                    # Reset form
                    self.ui.lineEdit_jumlahObat.clear()
                    self.ui.lineEdit_namaObat.clear()
                    
                    # Refresh data obat
                    self.load_obat_layak_jual()
                    
                    # Close window
                    self.close()
                else:
                    QMessageBox.warning(self, "Peringatan", pesan)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal simpan obat: {e}")

