# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailKeranjangApoteker.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(573, 509)
        MainWindow.resize(666, 526)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_namaPembeli = QLabel(self.centralwidget)
        self.label_namaPembeli.setObjectName(u"label_namaPembeli")
        self.label_namaPembeli.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"alternate-background-color: rgb(187, 255, 253);")

        self.gridLayout.addWidget(self.label_namaPembeli, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(138)

        self.verticalLayout.addWidget(self.tableWidget)

        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(92)

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_buttons = QGridLayout()
        self.gridLayout_buttons.setObjectName(u"gridLayout_buttons")
        
        self.pushButton_updateKeranjang = QPushButton(self.centralwidget)
        self.pushButton_updateKeranjang.setObjectName(u"pushButton_updateKeranjang")
        self.pushButton_updateKeranjang.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"	background-color: rgb(125, 202, 211);\n"
"    color: white;\n"
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
"}")
        self.gridLayout_buttons.addWidget(self.pushButton_updateKeranjang, 0, 0, 1, 1)

        self.pushButton_hapusDataKeranjang = QPushButton(self.centralwidget)
        self.pushButton_hapusDataKeranjang.setObjectName(u"pushButton_hapusDataKeranjang")
        self.pushButton_hapusDataKeranjang.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 6px 8px; \n"
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
        self.gridLayout_buttons.addWidget(self.pushButton_hapusDataKeranjang, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_buttons)

        self.pushButton_kembali = QPushButton(self.centralwidget)
        self.pushButton_kembali.setObjectName(u"pushButton_kembali")
        self.pushButton_kembali.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px; \n"
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

        self.verticalLayout.addWidget(self.pushButton_kembali, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 573, 22))
        self.menubar.setGeometry(QRect(0, 0, 666, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detail Data Keranjang", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        self.label_namaPembeli.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detail Data Keranjang Apoteker", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        self.label_namaPembeli.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Silakan pilih data obat yang akan dihapus dari keranjang!", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None));
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.pushButton_updateKeranjang.setText(QCoreApplication.translate("MainWindow", u"Update Keranjang", None))
        self.pushButton_hapusDataKeranjang.setText(QCoreApplication.translate("MainWindow", u"Hapus Dari Keranjang", None))
        self.pushButton_kembali.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
    # retranslateUi


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QGridLayout
from PySide6.QtCore import Qt
from backend.apoteker import lihatKeranjang, hapusObatDariKeranjang, updateJumlahObatYangDiBeli

class DetailKeranjangApotekerWindow(QMainWindow):
    def __init__(self, keranjang_id, parent=None):
        super().__init__()
        self.parent = parent
        self.keranjang_id = keranjang_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Load detail keranjang
        self.load_detail_keranjang()
        
        # Connect buttons
        self.ui.pushButton_updateKeranjang.clicked.connect(self.update_keranjang)
        self.ui.pushButton_hapusDataKeranjang.clicked.connect(self.hapus_obat_keranjang)
        self.ui.pushButton_kembali.clicked.connect(self.close)
    
    def load_detail_keranjang(self):
        """Load detail keranjang ke tabel"""
        try:
            data = lihatKeranjang(self.keranjang_id)
            
            if isinstance(data, str):
                QMessageBox.warning(self, "Peringatan", data)
                self.close()
                return
            
            # Set nama pembeli
            self.ui.label_namaPembeli.setText(data.get('namaPembeli', ''))
            
            # Load detail obat
            detail_obat = data.get('detailObat', [])
            self.ui.tableWidget.setRowCount(len(detail_obat))
            
            total_keseluruhan = 0
            
            for row_idx, item in enumerate(detail_obat):
                if isinstance(item, dict):
                    detail_id = item.get('detailKeranjangId', '')
                    nama_obat = item.get('namaObat', '')
                    jenis = item.get('jenis', '')
                    kategori = item.get('namaKategori', '')
                    jumlah = item.get('jumlah', 0)
                    subtotal = item.get('subtotal', 0)
                else:
                    # Query result: detailKeranjangId, namaObat, jenis, namaKategori, jumlah, subtotal
                    detail_id = item[0]
                    nama_obat = item[1]
                    jenis = item[2]
                    kategori = item[3]
                    jumlah = item[4]
                    subtotal = item[5]
                
                total_keseluruhan += subtotal
                
                # Kolom: detailKeranjangId, namaObat, Jenis, Kategori, Jumlah, Subtotal, Total
                # Semua kolom tidak bisa diedit kecuali Jumlah
                item_detail_id = QTableWidgetItem(str(detail_id))
                item_detail_id.setFlags(item_detail_id.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 0, item_detail_id)
                
                item_nama = QTableWidgetItem(str(nama_obat))
                item_nama.setFlags(item_nama.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 1, item_nama)
                
                item_jenis = QTableWidgetItem(str(jenis) if jenis else "-")
                item_jenis.setFlags(item_jenis.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 2, item_jenis)
                
                item_kategori = QTableWidgetItem(str(kategori) if kategori else "-")
                item_kategori.setFlags(item_kategori.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 3, item_kategori)
                
                # Kolom Jumlah - BISA DIEDIT
                item_jumlah = QTableWidgetItem(str(jumlah))
                self.ui.tableWidget.setItem(row_idx, 4, item_jumlah)
                
                item_subtotal = QTableWidgetItem(f"Rp {subtotal:,}")
                item_subtotal.setFlags(item_subtotal.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 5, item_subtotal)
                
                item_total = QTableWidgetItem(f"Rp {total_keseluruhan:,}")
                item_total.setFlags(item_total.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row_idx, 6, item_total)
            
            # Update label header
            self.ui.label.setText(f"Detail Data Keranjang Apoteker - Total: Rp {total_keseluruhan:,}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load detail: {e}")
    
    def hapus_obat_keranjang(self):
        """Hapus obat dari keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat yang akan dihapus!")
                return
            
            detail_id = self.ui.tableWidget.item(selected, 0).text()
            nama_obat = self.ui.tableWidget.item(selected, 1).text()
            
            # Konfirmasi hapus
            reply = QMessageBox.question(
                self,
                "Konfirmasi Hapus",
                f"Yakin ingin menghapus '{nama_obat}' dari keranjang?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = hapusObatDariKeranjang(detail_id)
                QMessageBox.information(self, "Info", pesan)
                
                # Reload detail keranjang
                self.load_detail_keranjang()
                
                # Refresh parent (dashboard apoteker)
                if self.parent and hasattr(self.parent, 'refresh_data_keranjang'):
                    self.parent.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal hapus obat: {e}")
    
    def update_keranjang(self):
        """Update jumlah obat yang telah diubah di tabel"""
        try:
            # Konfirmasi update
            reply = QMessageBox.question(
                self,
                "Konfirmasi Update",
                "Yakin ingin menyimpan semua perubahan?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                updated_count = 0
                errors = []
                
                # Loop semua baris di tabel
                for row in range(self.ui.tableWidget.rowCount()):
                    try:
                        # Ambil detail_keranjang_id dari kolom 0
                        detail_keranjang_id = self.ui.tableWidget.item(row, 0).text()
                        
                        # Ambil jumlah baru dari kolom 4 (Jumlah)
                        jumlah_item = self.ui.tableWidget.item(row, 4)
                        if jumlah_item:
                            jumlah_baru_str = jumlah_item.text().strip()
                            
                            # Validasi jumlah adalah angka
                            try:
                                jumlah_baru = int(jumlah_baru_str)
                                if jumlah_baru <= 0:
                                    nama_obat = self.ui.tableWidget.item(row, 1).text()
                                    errors.append(f"{nama_obat}: Jumlah harus lebih dari 0")
                                    continue
                                
                                # Update ke database
                                pesan = updateJumlahObatYangDiBeli(detail_keranjang_id, jumlah_baru)
                                if "berhasil" in pesan.lower() or "sukses" in pesan.lower():
                                    updated_count += 1
                                else:
                                    nama_obat = self.ui.tableWidget.item(row, 1).text()
                                    errors.append(f"{nama_obat}: {pesan}")
                            except ValueError:
                                nama_obat = self.ui.tableWidget.item(row, 1).text()
                                errors.append(f"{nama_obat}: Jumlah harus berupa angka")
                    except Exception as e:
                        errors.append(f"Baris {row + 1}: {str(e)}")
                
                # Tampilkan hasil
                if errors:
                    error_msg = "\n".join(errors)
                    QMessageBox.warning(self, "Peringatan", f"Beberapa update gagal:\n\n{error_msg}")
                else:
                    QMessageBox.information(self, "Sukses", f"{updated_count} item berhasil diupdate!")
                
                # Reload data untuk sinkronisasi
                self.load_detail_keranjang()
                
                # Refresh parent dashboard jika ada
                if self.parent and hasattr(self.parent, 'refresh_data_keranjang'):
                    self.parent.refresh_data_keranjang()
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal update keranjang: {e}")

