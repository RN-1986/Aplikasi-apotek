# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardAdmin.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QWidget)
import logo-apotek_rc
import logo-apotek_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 608)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 40, 41, 31))
        self.label_4.setStyleSheet(u"image: url(:/Icons/medication.png);\n"
"border-radius: 15px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 530, 31, 31))
        self.label_6.setStyleSheet(u"image: url(:/logoKasir/circle-user.png);\n"
"border-radius: 15px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 230, 41, 41))
        self.label.setStyleSheet(u"image: url(:/logo-admin/money-check-edit.png);\n"
"\n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 10, 661, 501))
        self.frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(187, 255, 253);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 561, 81))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border radius: 30px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 71, 20))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(125, 202, 211);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 40, 261, 41))
        self.lineEdit.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(125, 202, 211);")
        self.pushButton_search = QPushButton(self.frame)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(420, 50, 41, 21))
        self.pushButton_search.setStyleSheet(u"border-radius: 50px;\n"
"background-color: rgba(255, 255, 255, 80);\n"
"image: url(:/logo-admin/search.png);")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(480, 40, 71, 41))
        self.pushButton_4.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(125, 202, 211);")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font1 = QFont()
        font1.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 150, 561, 331))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(112)
        self.verticalScrollBar = QScrollBar(self.frame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(600, 160, 20, 311))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.pushButton_tambah = QPushButton(self.frame)
        self.pushButton_tambah.setObjectName(u"pushButton_tambah")
        self.pushButton_tambah.setGeometry(QRect(40, 110, 91, 31))
        self.pushButton_tambah.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(49, 245, 46);")
        self.pushButton_edit = QPushButton(self.frame)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(140, 110, 91, 31))
        self.pushButton_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 216, 23);")
        self.pushButton_delete = QPushButton(self.frame)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(240, 110, 91, 31))
        self.pushButton_delete.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_kelolaObat = QPushButton(self.centralwidget)
        self.pushButton_kelolaObat.setObjectName(u"pushButton_kelolaObat")
        self.pushButton_kelolaObat.setGeometry(QRect(70, 170, 161, 41))
        self.pushButton_kelolaObat.setFont(font)
        self.pushButton_kelolaObat.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 10px;\n"
"hover-color: rgb(160, 230, 228); \n"
"pressed-color: rgb(120, 200, 198); ")
        self.pushButton_riwayatTransaksi = QPushButton(self.centralwidget)
        self.pushButton_riwayatTransaksi.setObjectName(u"pushButton_riwayatTransaksi")
        self.pushButton_riwayatTransaksi.setGeometry(QRect(70, 230, 161, 41))
        self.pushButton_riwayatTransaksi.setFont(font)
        self.pushButton_riwayatTransaksi.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 10px;\n"
"hover-color: rgb(160, 230, 228); \n"
"pressed-color: rgb(120, 200, 198); ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 520, 131, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 41, 41))
        font3 = QFont()
        font3.setPointSize(6)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"image: url(:/logo-admin/admin-alt.png);\n"
"border-radius: 5px;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 20, 191, 61))
        self.textBrowser.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 30px;")
        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        self.pushButton_keluar.setGeometry(QRect(770, 530, 151, 31))
        self.pushButton_keluar.setFont(font2)
        self.pushButton_keluar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 520, 41, 41))
        self.label_7.setStyleSheet(u"image: url(:/logo-admin/circle-user.png);\n"
"border-radius: 15px;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 40, 41, 31))
        self.label_8.setStyleSheet(u"\n"
"image: url(:/logo-admin/medication.png);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_6.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   Nama atau ID obat", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cari Obat", None))
        self.pushButton_search.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Obat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Harga Obat", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Kadaluarsa", None));
        self.pushButton_tambah.setText(QCoreApplication.translate("MainWindow", u"Tambah Data +", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Data -", None))
        self.pushButton_kelolaObat.setText(QCoreApplication.translate("MainWindow", u"Kelola Data Obat", None))
        self.pushButton_riwayatTransaksi.setText(QCoreApplication.translate("MainWindow", u"Riwayat Transaksi", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_5.setText("")
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
        self.label_8.setText("")
    # retranslateUi

