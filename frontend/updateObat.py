# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateObat.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform,QIntValidator)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget,QDateEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 402)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"border-radius: 20px;")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setValidator(QIntValidator())
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit_6 = QDateEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setCalendarPopup(True)
        self.lineEdit_6.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_6.setStyleSheet(u"""
            /* 1. Style Kotak Input Utama */
            QDateEdit {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 6px 8px;
                color: black; /* Pastikan teks input item */
            }

            /* 3. Style POPUP KALENDER (Bagian Paling Penting) */
            QCalendarWidget QToolButton {
                color: black;        /* Warna teks bulan/tahun */
                background-color: transparent; 
                icon-size: 20px;
            }
            
            QCalendarWidget QMenu {
                background-color: white; /* Latar menu bulan jadi PUTIH */
                color: black;            /* Teks menu bulan jadi HITAM */
            }

            QCalendarWidget QSpinBox {
                background-color: white; /* Latar ganti tahun jadi PUTIH */
                color: black;
                selection-background-color: #31f52e;
            }
            
            /* Warna angka tanggal di kalender */
            QCalendarWidget QAbstractItemView:enabled {
                color: black;
                background-color: white;
                selection-background-color: #31f52e; /* Hijau pas tanggal dipilih */
                selection-color: black;
            }
        """)

        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setValidator(QIntValidator())
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_5 = QDateEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setCalendarPopup(True)
        self.lineEdit_5.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_5.setStyleSheet(u"""
            /* 1. Style Kotak Input Utama */
            QDateEdit {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 6px 8px;
                color: black; /* Pastikan teks input item */
            }
    

            /* 3. Style POPUP KALENDER (Bagian Paling Penting) */
            QCalendarWidget QToolButton {
                color: black;        /* Warna teks bulan/tahun */
                background-color: transparent; 
                icon-size: 20px;
            }
            
            QCalendarWidget QMenu {
                background-color: white; /* Latar menu bulan jadi PUTIH */
                color: black;            /* Teks menu bulan jadi HITAM */
            }

            QCalendarWidget QSpinBox {
                background-color: white; /* Latar ganti tahun jadi PUTIH */
                color: black;
                selection-background-color: #31f52e;
            }
            
            /* Warna angka tanggal di kalender */
            QCalendarWidget QAbstractItemView:enabled {
                color: black;
                background-color: white;
                selection-background-color: #31f52e; /* Hijau pas tanggal dipilih */
                selection-color: black;
            }
        """)

        self.gridLayout.addWidget(self.lineEdit_5, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_simpan = QPushButton(self.centralwidget)
        self.pushButton_simpan.setObjectName(u"pushButton_simpan")
        self.pushButton_simpan.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(255, 255, 0);\n"
"	border-radius: 5px;\n"
"padding: 8px 8px; \n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"\tbackground-color: rgb(255, 255, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"\tbackground-color: rgb(255, 255, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_simpan, 0, 2, 1, 1)

        self.pushButton_batal = QPushButton(self.centralwidget)
        self.pushButton_batal.setObjectName(u"pushButton_batal")
        self.pushButton_batal.setStyleSheet(u"QPushButton { \n"
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

        self.gridLayout_2.addWidget(self.pushButton_batal, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(88, 25, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update Obat ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Harga                :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kategori Obat     :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stok                   :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Obat Bebas", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Obat Bebas Terbatas", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Obat Keras", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Obat Narkotika & Psikotropika", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jenis Obat         :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tgl Produksi        :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Obat       :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tgl Kadaluarsa     :", None))
        self.pushButton_simpan.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
    # retranslateUi


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QMessageBox
from backend.admin import updateObat, ambilDataObatYangAkanDiUpdate

class UpdateObatWindow(QMainWindow):
    def __init__(self, obat_id, parent=None):
        super().__init__()
        self.parent = parent
        self.obat_id = obat_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Load data obat yang akan diupdate
        self.load_data_obat()
        
        # Connect buttons
        self.ui.pushButton_simpan.clicked.connect(self.update_obat)
        self.ui.pushButton_batal.clicked.connect(self.close)
    
    def load_data_obat(self):
        """Load data obat ke form"""
        try:
            data = ambilDataObatYangAkanDiUpdate(self.obat_id)
            if isinstance(data, str):
                QMessageBox.warning(self, "Peringatan", data)
                self.close()
                return
            
            # --- FUNGSI BANTUAN KONVERSI STRING KE QDATE ---
            def set_date_from_string(date_edit_widget, date_string):
                # Format dari database biasanya "yyyy-MM-dd" (contoh: 2025-12-31)
                qdate = QDate.fromString(str(date_string), "yyyy-MM-dd")
                if qdate.isValid():
                    date_edit_widget.setDate(qdate)
                else:
                    date_edit_widget.setDate(QDate.currentDate()) # Default hari ini kalau error

            # Isi form dengan data existing
            if isinstance(data, dict):
                self.ui.lineEdit.setText(str(data.get('namaObat', '')))
                self.ui.lineEdit_2.setText(str(data.get('jenis', '')))
                # Konversi harga dan stok ke integer tanpa desimal
                harga_value = int(float(data.get('harga', 0)))
                stok_value = int(float(data.get('stok', 0)))
                self.ui.lineEdit_3.setText(str(harga_value))
                self.ui.lineEdit_4.setText(str(stok_value))
                
                # --- REVISI: Pake setDate bukan setText ---
                # lineEdit_6 = tgl_produksi (row 4)
                set_date_from_string(self.ui.lineEdit_6, data.get('tgl_produksi', ''))
                
                # lineEdit_5 = kadaluarsa (row 5)
                set_date_from_string(self.ui.lineEdit_5, data.get('kadaluarsa', ''))
                
                # Set kategori di comboBox - handle None
                kategori_id = data.get('kategoriId')
                if kategori_id is None:
                    kategori_id = 1
                kategori_index = max(0, int(kategori_id) - 1)
                self.ui.comboBox.setCurrentIndex(kategori_index)
            else:
                # Data tuple format
                self.ui.lineEdit.setText(str(data[1]))  # namaObat
                self.ui.lineEdit_2.setText(str(data[2]))  # jenis
                # Konversi harga dan stok ke integer tanpa desimal
                harga_value = int(float(data[3]))
                stok_value = int(float(data[4]))
                self.ui.lineEdit_3.setText(str(harga_value))
                self.ui.lineEdit_4.setText(str(stok_value))
                
                # --- REVISI: Pake setDate bukan setText ---
                set_date_from_string(self.ui.lineEdit_6, data[5]) # tgl_produksi
                set_date_from_string(self.ui.lineEdit_5, data[6]) # kadaluarsa
                
                # Handle None untuk kategoriId
                kategori_id = data[7] if len(data) > 7 and data[7] is not None else 1
                kategori_index = max(0, int(kategori_id) - 1)
                self.ui.comboBox.setCurrentIndex(kategori_index)
            
            # Set focus ke field Nama Obat agar tidak auto focus ke field lain
            self.ui.lineEdit.setFocus()
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load data: {e}")
            self.close()
    
    def update_obat(self):
        """Update data obat"""
        try:
            # Ambil data dari form
            nama_obat = self.ui.lineEdit.text().strip()
            jenis = self.ui.lineEdit_2.text().strip()
            harga_str = self.ui.lineEdit_3.text().strip()
            stok_str = self.ui.lineEdit_4.text().strip()
            tgl_produksi = self.ui.lineEdit_6.text().strip()  # lineEdit_6 = tgl_produksi (row 4)
            tgl_kadaluarsa = self.ui.lineEdit_5.text().strip()  # lineEdit_5 = kadaluarsa (row 5)
            kategori = self.ui.comboBox.currentText()
            
            # Validasi input
            if not all([nama_obat, jenis, harga_str, stok_str, tgl_produksi, tgl_kadaluarsa]):
                QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
                return
            
            # Convert kategori text ke kategoriId
            kategori_map = {
                "Obat Bebas": 1,
                "Obat Bebas Terbatas": 2,
                "Obat Keras": 3,
                "Obat Narkotika & Psikotropika": 4
            }
            kategori_id = kategori_map.get(kategori, 1)
            
            # Validasi dan convert angka
            try:
                # Convert to float first to handle decimal, then to int for integer values
                harga = int(float(harga_str.replace(',', '').strip()))
                stok = int(float(stok_str.replace(',', '').strip()))
            except ValueError as e:
                QMessageBox.warning(self, "Peringatan", f"Harga dan Stok harus berupa angka!\nError: {e}")
                return
            
            # Update ke database
            pesan = updateObat(self.obat_id, nama_obat, jenis, harga, stok, tgl_produksi, tgl_kadaluarsa, kategori_id)
            QMessageBox.information(self, "Info", pesan)
            
            # Refresh parent dashboard
            if self.parent and hasattr(self.parent, 'refresh_data_obat'):
                self.parent.refresh_data_obat()
            
            # Tutup window
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal update data: {e}")

