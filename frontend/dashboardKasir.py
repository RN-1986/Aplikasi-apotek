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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
import logo-apotek_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(967, 601)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 65))
        self.textBrowser.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.textBrowser)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 450))
        self.frame.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.gridLayout.addWidget(self.pushButton_Bayar, 3, 3, 1, 1)

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

        self.gridLayout.addWidget(self.pushButton_lihatDetail, 3, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(186)

        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

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

        self.gridLayout.addWidget(self.pushButton_refresh, 3, 1, 1, 1)

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

        self.gridLayout.addWidget(self.pushButton_Batalkan, 3, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_keluar.setFont(font1)
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
        self.menubar.setGeometry(QRect(0, 0, 967, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DASHBOARD</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">KASIR</span></p></body></html>", None))
        self.pushButton_Bayar.setText(QCoreApplication.translate("MainWindow", u"Bayar", None))
        self.pushButton_lihatDetail.setText(QCoreApplication.translate("MainWindow", u"Lihat Detail", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total Harga", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nama Apoteker", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"DAFTAR KERANJANG DIKIRIM", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_Batalkan.setText(QCoreApplication.translate("MainWindow", u"Batalkan Pemesanan", None))
        self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi

