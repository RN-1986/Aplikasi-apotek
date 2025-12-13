# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateObatKeranjang.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 485)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
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
        font1.setPointSize(8)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 8px 8px;")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
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
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(172)

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_hapus = QPushButton(self.centralwidget)
        self.pushButton_hapus.setObjectName(u"pushButton_hapus")
        self.pushButton_hapus.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 8px 8px;\n"
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

        self.gridLayout_2.addWidget(self.pushButton_hapus, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.pushButton_simpan = QPushButton(self.centralwidget)
        self.pushButton_simpan.setObjectName(u"pushButton_simpan")
        self.pushButton_simpan.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(49, 245, 46);\n"
"	border-radius: 5px;\n"
"padding: 8px 8px;\n"
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

        self.gridLayout_2.addWidget(self.pushButton_simpan, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.pushButton_batal = QPushButton(self.centralwidget)
        self.pushButton_batal.setObjectName(u"pushButton_batal")
        self.pushButton_batal.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 8px 20px;\n"
"min-width: 100px;   \n"
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

        self.verticalLayout.addWidget(self.pushButton_batal, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 877, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update Data Keranjang", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        self.pushButton_hapus.setText(QCoreApplication.translate("MainWindow", u"Hapus Data", None))
        self.pushButton_simpan.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
    # retranslateUi


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from backend.apoteker import lihatKeranjang, updateJumlahObatYangDiBeli, hapusObatDariKeranjang

class UpdateObatKeranjangWindow(QMainWindow):
    def __init__(self, keranjang_id, nama_pembeli, parent=None):
        super().__init__()
        self.parent = parent
        self.keranjang_id = keranjang_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window title
        self.setWindowTitle(f"Edit Keranjang - {nama_pembeli}")
        
        # Set nama pembeli (read-only)
        self.ui.lineEdit.setText(nama_pembeli)
        self.ui.lineEdit.setReadOnly(True)
        
        # Connect buttons
        self.ui.pushButton_simpan.clicked.connect(self.simpan_perubahan)
        self.ui.pushButton_hapus.clicked.connect(self.hapus_obat)
        self.ui.pushButton_batal.clicked.connect(self.close)
        
        # Load data keranjang
        self.load_data_keranjang()
    
    def load_data_keranjang(self):
        """Load data obat di keranjang ke table"""
        try:
            data = lihatKeranjang(self.keranjang_id)
            
            if isinstance(data, str):
                QMessageBox.warning(self, "Error", data)
                return
            
            detail_obat = data.get('detailObat', [])
            self.ui.tableWidget.setRowCount(0)
            
            for obat in detail_obat:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                
                if isinstance(obat, dict):
                    detail_id = obat.get('detailKeranjangId', '')
                    nama_obat = obat.get('namaObat', '')
                    kategori = obat.get('namaKategori', '-')
                    jenis = obat.get('jenis', '-')
                    jumlah = obat.get('jumlah', '')
                else:
                    # Query result: detailKeranjangId, namaObat, jenis, namaKategori, jumlah, subtotal
                    detail_id = obat[0]
                    nama_obat = obat[1]
                    jenis = obat[2] if obat[2] else "-"
                    kategori = obat[3] if obat[3] else "-"
                    jumlah = obat[4]
                
                # Column 0: detail_keranjang_id (hidden, for reference)
                item_id = QTableWidgetItem(str(detail_id))
                item_id.setFlags(item_id.flags() & ~Qt.ItemIsEditable)  # Not editable
                self.ui.tableWidget.setItem(row, 0, item_id)
                
                # Column 1: Nama Obat (not editable)
                item_nama = QTableWidgetItem(str(nama_obat))
                item_nama.setFlags(item_nama.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 1, item_nama)
                
                # Column 2: Kategori (not editable)
                item_kategori = QTableWidgetItem(str(kategori))
                item_kategori.setFlags(item_kategori.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 2, item_kategori)
                
                # Column 3: Jenis (not editable)
                item_jenis = QTableWidgetItem(str(jenis))
                item_jenis.setFlags(item_jenis.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 3, item_jenis)
                
                # Column 4: Jumlah (EDITABLE)
                item_jumlah = QTableWidgetItem(str(jumlah))
                self.ui.tableWidget.setItem(row, 4, item_jumlah)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load data keranjang: {e}")
    
    def simpan_perubahan(self):
        """Simpan semua perubahan jumlah di table"""
        try:
            if self.ui.tableWidget.rowCount() == 0:
                QMessageBox.warning(self, "Peringatan", "Tidak ada data obat di keranjang!")
                return
            
            updated_count = 0
            error_messages = []
            
            for row in range(self.ui.tableWidget.rowCount()):
                detail_keranjang_id = self.ui.tableWidget.item(row, 0).text()
                nama_obat = self.ui.tableWidget.item(row, 1).text()
                jumlah_baru_str = self.ui.tableWidget.item(row, 4).text().strip()
                
                if not jumlah_baru_str:
                    error_messages.append(f"Baris {row+1} ({nama_obat}): Jumlah kosong")
                    continue
                
                try:
                    jumlah_baru = int(jumlah_baru_str)
                    if jumlah_baru <= 0:
                        error_messages.append(f"Baris {row+1} ({nama_obat}): Jumlah harus > 0")
                        continue
                except ValueError:
                    error_messages.append(f"Baris {row+1} ({nama_obat}): Jumlah harus angka")
                    continue
                
                # Update ke database
                pesan = updateJumlahObatYangDiBeli(detail_keranjang_id, jumlah_baru)
                
                if "berhasil" in pesan.lower():
                    updated_count += 1
                else:
                    error_messages.append(f"{nama_obat}: {pesan}")
            
            # Show result
            result_msg = f"Berhasil update {updated_count} dari {self.ui.tableWidget.rowCount()} obat"
            if error_messages:
                result_msg += f"\n\nError:\n" + "\n".join(error_messages[:5])  # Show max 5 errors
            
            if updated_count > 0:
                QMessageBox.information(self, "Hasil Update", result_msg)
                
                # Refresh parent dashboard
                if self.parent and hasattr(self.parent, 'refresh_data_keranjang'):
                    self.parent.refresh_data_keranjang()
                
                # Reload data to show updated values
                self.load_data_keranjang()
            else:
                QMessageBox.warning(self, "Tidak Ada Update", result_msg)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal simpan perubahan: {e}")
    
    def hapus_obat(self):
        """Hapus obat yang dipilih dari keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat yang akan dihapus!")
                return
            
            detail_keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_obat = self.ui.tableWidget.item(selected, 1).text()
            
            reply = QMessageBox.question(
                self,
                "Konfirmasi Hapus",
                f"Yakin ingin menghapus obat '{nama_obat}' dari keranjang?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = hapusObatDariKeranjang(detail_keranjang_id)
                QMessageBox.information(self, "Info", pesan)
                
                # Reload table
                self.load_data_keranjang()
                
                # Refresh parent dashboard
                if self.parent and hasattr(self.parent, 'refresh_data_keranjang'):
                    self.parent.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal hapus obat: {e}")

