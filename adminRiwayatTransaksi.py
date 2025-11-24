# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminRiwayatTransaksi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 605)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 160, 41, 41))
        font = QFont()
        font.setPointSize(6)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"image: url(:/logo-admin/admin-alt.png);\n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 510, 131, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(240, 0, 661, 501))
        self.frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(187, 255, 253);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 561, 71))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border radius: 30px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 30, 61, 51))
        self.label_3.setStyleSheet(u"image: url(:/logo-admin/trading.png);")
        self.tableWidget_2 = QTableWidget(self.frame)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 140, 611, 321))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(152)
        self.verticalScrollBar = QScrollBar(self.frame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(630, 140, 16, 311))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.pushButton_semuTransaksi = QPushButton(self.frame)
        self.pushButton_semuTransaksi.setObjectName(u"pushButton_semuTransaksi")
        self.pushButton_semuTransaksi.setGeometry(QRect(20, 100, 111, 31))
        self.pushButton_semuTransaksi.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 10px;\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(48, 93, 124);\n"
"       }")
        self.pushButton_detailriwayatTransaksi = QPushButton(self.frame)
        self.pushButton_detailriwayatTransaksi.setObjectName(u"pushButton_detailriwayatTransaksi")
        self.pushButton_detailriwayatTransaksi.setGeometry(QRect(140, 100, 141, 31))
        self.pushButton_detailriwayatTransaksi.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 10px;\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(48, 93, 124);\n"
"       }")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 220, 41, 41))
        self.label.setStyleSheet(u"image: url(:/logo-admin/money-check-edit.png);\n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;")
        self.pushButton_kelolaObat = QPushButton(self.centralwidget)
        self.pushButton_kelolaObat.setObjectName(u"pushButton_kelolaObat")
        self.pushButton_kelolaObat.setGeometry(QRect(70, 160, 161, 41))
        font3 = QFont()
        font3.setPointSize(10)
        self.pushButton_kelolaObat.setFont(font3)
        self.pushButton_kelolaObat.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 10px;\n"
"hover-color: rgb(160, 230, 228); \n"
"pressed-color: rgb(120, 200, 198); ")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 510, 41, 41))
        self.label_6.setStyleSheet(u"image: url(:/logo-admin/circle-user.png);\n"
"border-radius: 15px;")
        self.pushButton_riwayatTransaksi = QPushButton(self.centralwidget)
        self.pushButton_riwayatTransaksi.setObjectName(u"pushButton_riwayatTransaksi")
        self.pushButton_riwayatTransaksi.setGeometry(QRect(70, 220, 161, 41))
        self.pushButton_riwayatTransaksi.setFont(font3)
        self.pushButton_riwayatTransaksi.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 10px;\n"
"hover-color: rgb(160, 230, 228); \n"
"pressed-color: rgb(120, 200, 198); ")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 30, 41, 31))
        self.label_4.setStyleSheet(u"image: url(:/Icons/medication.png);\n"
"border-radius: 15px;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 10, 191, 61))
        self.textBrowser.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 30px;")
        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        self.pushButton_keluar.setGeometry(QRect(750, 510, 151, 31))
        self.pushButton_keluar.setFont(font1)
        self.pushButton_keluar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 30, 41, 31))
        self.label_7.setStyleSheet(u"image: url(:/logo-admin/medication.png);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 949, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                      RIWAYAT TRANSAKSI", None))
        self.label_3.setText("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Transaksi", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kasir", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total Harga(Rp)", None));
        self.pushButton_semuTransaksi.setText(QCoreApplication.translate("MainWindow", u"Semua Transaksi", None))
        self.pushButton_detailriwayatTransaksi.setText(QCoreApplication.translate("MainWindow", u"Detail Riwayat Transaksi", None))
        self.label.setText("")
        self.pushButton_kelolaObat.setText(QCoreApplication.translate("MainWindow", u"Kelola Data Obat", None))
        self.label_6.setText("")
        self.pushButton_riwayatTransaksi.setText(QCoreApplication.translate("MainWindow", u"Riwayat Transaksi", None))
        self.label_4.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DASHBOARD</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ADMIN</span></p></body></html>", None))
        self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.label_7.setText("")
    # retranslateUi

