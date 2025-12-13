# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailRiwayatTransaksi.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 405)
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

        self.verticalLayout.addWidget(self.label)

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
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(117)

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton { \n"
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

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 607, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"                                    DETAIL RIWAYAT TRANSAKSI", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Detail ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sub Total", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from backend.admin import lihatDetailTransaksi

class DetailRiwayatWindow(QMainWindow):
    def __init__(self, transaksi_id, parent=None):
        super().__init__()
        self.parent = parent
        self.transaksi_id = transaksi_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Load data detail transaksi
        self.load_detail_transaksi()
        
        # Connect button keluar
        self.ui.pushButton.clicked.connect(self.close)
    
    def load_detail_transaksi(self):
        """Load detail transaksi ke table"""
        try:
            data = lihatDetailTransaksi(self.transaksi_id)
            
            if isinstance(data, str):
                QMessageBox.warning(self, "Peringatan", data)
                return
            
            # Set jumlah row
            self.ui.tableWidget.setRowCount(len(data))
            
            total_keseluruhan = 0
            
            # Isi data ke table
            for row_idx, row_data in enumerate(data):
                # Support dict dan tuple format
                if isinstance(row_data, dict):
                    detail_id = row_data.get('detailId', '')
                    nama_obat = row_data.get('namaObat', '')
                    jumlah = row_data.get('jumlah', 0)
                    subtotal = row_data.get('subtotal', 0)
                else:
                    detail_id = row_data[0]
                    nama_obat = row_data[1]
                    jumlah = row_data[2]
                    subtotal = row_data[3]
                
                total_keseluruhan += subtotal
                
                # Set items ke table
                self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(detail_id)))
                self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(nama_obat)))
                self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(jumlah)))
                self.ui.tableWidget.setItem(row_idx, 3, QTableWidgetItem(f"Rp {subtotal:,}"))
                self.ui.tableWidget.setItem(row_idx, 4, QTableWidgetItem(f"Rp {total_keseluruhan:,}"))
            
            # Update label dengan total
            self.ui.label.setText(f"DETAIL RIWAYAT TRANSAKSI - Total: Rp {total_keseluruhan:,}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load detail: {e}")

