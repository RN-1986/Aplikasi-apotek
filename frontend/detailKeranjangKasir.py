# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailKeranjangKasir.ui'
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
        MainWindow.resize(742, 526)
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

        self.gridLayout.addWidget(self.label_namaPembeli, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_buttons = QGridLayout()
        self.gridLayout_buttons.setObjectName(u"gridLayout_buttons")
        
        self.pushButton_update = QPushButton(self.centralwidget)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px; \n"
"	background-color: rgb(125, 202, 211);\n"
"    color: white;\n"
"padding: 6px 20px;\n"
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
        self.gridLayout_buttons.addWidget(self.pushButton_update, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px; \n"
"	background-color: rgb(255, 0, 0);\n"
"    color: white;\n"
"padding: 6px 20px;\n"
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
        self.gridLayout_buttons.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_buttons)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton { \n"
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

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 742, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detail Data Keranjang Kasir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        self.label_namaPembeli.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Silahkan pilih data obat yang akan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID Obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Sub Total", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"Update Keranjang", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Hapus Dari Keranjang", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
    # retranslateUi


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QGridLayout
from backend.kasir import lihatDetailKeranjangUntukKasir, hapusItemDiKasir, updateJumlahObatYangDiBeli

class DetailKeranjangKasir(QMainWindow):
    def __init__(self, keranjang_id, parent=None):
        super().__init__()
        self.parent = parent
        self.keranjang_id = keranjang_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.pushButton.clicked.connect(self.close)  # Tombol Kembali
        self.ui.pushButton_2.clicked.connect(self.hapus_item)  # Tombol Hapus
        self.ui.pushButton_update.clicked.connect(self.update_keranjang)  # Tombol Update
        
        # Load data
        self.load_detail_keranjang()
    
    def load_detail_keranjang(self):
        """Load detail keranjang ke tabel"""
        try:
            data = lihatDetailKeranjangUntukKasir(self.keranjang_id)
            
            if isinstance(data, str):
                QMessageBox.warning(self, "Peringatan", data)
                self.close()
                return
            
            # Set nama pembeli
            nama_pembeli = data.get('namaPembeli', '')
            self.ui.label_namaPembeli.setText(nama_pembeli)
            
            # Set judul dengan info keranjang
            self.ui.label.setText(f"Detail Keranjang #{self.keranjang_id} - {nama_pembeli}")
            
            # Load detail obat ke tabel
            self.ui.tableWidget.setRowCount(0)
            total_keseluruhan = 0
            
            detail_items = data.get('detail', [])
            for item in detail_items:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                
                if isinstance(item, dict):
                    detail_id = item.get('detailKeranjangId', '')
                    obat_id = item.get('obatId', '')
                    nama_obat = item.get('namaObat', '')
                    jenis = item.get('jenis', '-')
                    kategori = item.get('namaKategori', '-')
                    jumlah = item.get('jumlah', 0)
                    subtotal = float(item.get('subtotal', 0))
                else:
                    # Tuple format: detailKeranjangId, obatId, namaObat, jenis, namaKategori, jumlah, subtotal
                    detail_id = item[0] if len(item) > 0 else ''
                    obat_id = item[1] if len(item) > 1 else ''
                    nama_obat = item[2] if len(item) > 2 else ''
                    jenis = item[3] if len(item) > 3 else '-'
                    kategori = item[4] if len(item) > 4 else '-'
                    jumlah = item[5] if len(item) > 5 else 0
                    subtotal = float(item[6]) if len(item) > 6 else 0
                
                total_keseluruhan += float(subtotal)
                
                # Kolom: Keranjang ID, ID Obat, Nama Obat, Jenis, Kategori, Jumlah, Sub Total, Total
                # Semua kolom tidak bisa diedit kecuali Jumlah
                item_keranjang_id = QTableWidgetItem(str(self.keranjang_id))
                item_keranjang_id.setFlags(item_keranjang_id.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 0, item_keranjang_id)
                
                item_obat_id = QTableWidgetItem(str(obat_id))
                item_obat_id.setFlags(item_obat_id.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 1, item_obat_id)
                
                item_nama_obat = QTableWidgetItem(str(nama_obat))
                item_nama_obat.setFlags(item_nama_obat.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 2, item_nama_obat)
                
                item_jenis = QTableWidgetItem(str(jenis))
                item_jenis.setFlags(item_jenis.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 3, item_jenis)
                
                item_kategori = QTableWidgetItem(str(kategori))
                item_kategori.setFlags(item_kategori.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 4, item_kategori)
                
                # Kolom Jumlah - BISA DIEDIT
                item_jumlah = QTableWidgetItem(str(jumlah))
                self.ui.tableWidget.setItem(row, 5, item_jumlah)
                
                item_subtotal = QTableWidgetItem(f"Rp {subtotal:,.0f}")
                item_subtotal.setFlags(item_subtotal.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 6, item_subtotal)
                
                # Simpan detailKeranjangId di kolom tersembunyi (untuk keperluan hapus dan update)
                item_detail_id = QTableWidgetItem(str(detail_id))
                item_detail_id.setFlags(item_detail_id.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget.setItem(row, 7, item_detail_id)
            
            # Update label total di header tabel (gunakan kolom terakhir untuk total)
            self.ui.label_3.setText(f"Total Keseluruhan: Rp {total_keseluruhan:,.0f}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load detail: {e}")
            self.close()
    
    def hapus_item(self):
        """Hapus item yang dipilih dari keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih item yang akan dihapus!")
                return
            
            # Ambil data item
            nama_obat = self.ui.tableWidget.item(selected, 2).text()
            detail_keranjang_id = self.ui.tableWidget.item(selected, 7).text()  # Kolom terakhir (hidden)
            
            # Konfirmasi hapus
            reply = QMessageBox.question(
                self,
                "Konfirmasi Hapus",
                f"Yakin ingin menghapus '{nama_obat}' dari keranjang?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = hapusItemDiKasir(detail_keranjang_id)
                QMessageBox.information(self, "Info", pesan)
                
                # Reload data
                self.load_detail_keranjang()
                
                # Refresh parent dashboard jika ada
                if self.parent and hasattr(self.parent, 'refresh_keranjang_dikirim'):
                    self.parent.refresh_keranjang_dikirim()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal hapus item: {e}")
    
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
                        # Ambil detail_keranjang_id dari kolom tersembunyi (kolom 7)
                        detail_keranjang_id = self.ui.tableWidget.item(row, 7).text()
                        
                        # Ambil jumlah baru dari kolom 5 (Jumlah)
                        jumlah_item = self.ui.tableWidget.item(row, 5)
                        if jumlah_item:
                            jumlah_baru_str = jumlah_item.text().strip()
                            
                            # Validasi jumlah adalah angka
                            try:
                                jumlah_baru = int(jumlah_baru_str)
                                if jumlah_baru <= 0:
                                    nama_obat = self.ui.tableWidget.item(row, 2).text()
                                    errors.append(f"{nama_obat}: Jumlah harus lebih dari 0")
                                    continue
                                
                                # Update ke database
                                pesan = updateJumlahObatYangDiBeli(detail_keranjang_id, jumlah_baru)
                                if "berhasil" in pesan.lower() or "sukses" in pesan.lower():
                                    updated_count += 1
                                else:
                                    nama_obat = self.ui.tableWidget.item(row, 2).text()
                                    errors.append(f"{nama_obat}: {pesan}")
                            except ValueError:
                                nama_obat = self.ui.tableWidget.item(row, 2).text()
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
                if self.parent and hasattr(self.parent, 'refresh_keranjang_dikirim'):
                    self.parent.refresh_keranjang_dikirim()
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal update keranjang: {e}")

