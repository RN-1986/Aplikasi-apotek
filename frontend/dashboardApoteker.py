# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardApoteker.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import logo_apotek_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 657)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(16777215, 60))
        self.textBrowser.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.textBrowser)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
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
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border radius: 5px;")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"background-color: rgb(226, 226, 226);")

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius:5px;\n"
"padding: 6px 8px; \n"
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
"\n"
"")

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius:5px;\n"
"padding: 6px 8px; \n"
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
"\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_editKeranjang = QPushButton(self.tab)
        self.pushButton_editKeranjang.setObjectName(u"pushButton_editKeranjang")
        self.pushButton_editKeranjang.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"	border-radius: 5px;\n"
"padding: 6px 8px; \n"
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

        self.gridLayout_3.addWidget(self.pushButton_editKeranjang, 1, 3, 1, 1)

        self.pushButton_lihatDetail = QPushButton(self.tab)
        self.pushButton_lihatDetail.setObjectName(u"pushButton_lihatDetail")
        self.pushButton_lihatDetail.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius:5px;\n"
"	border-radius: 5px;\n"
"padding: 6px 8px; \n"
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

        self.gridLayout_3.addWidget(self.pushButton_lihatDetail, 1, 4, 1, 1)

        self.pushButton_kirimKasir = QPushButton(self.tab)
        self.pushButton_kirimKasir.setObjectName(u"pushButton_kirimKasir")
        self.pushButton_kirimKasir.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(255, 255, 0);	\n"
"	border-radius: 5px;\n"
"padding: 6px 8px; \n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	background-color: rgb(255, 255, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"	background-color: rgb(255, 255, 127);\n"
"    color: black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_kirimKasir, 1, 6, 1, 1)

        self.pushButton_batalKeranjang = QPushButton(self.tab)
        self.pushButton_batalKeranjang.setObjectName(u"pushButton_batalKeranjang")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_batalKeranjang.sizePolicy().hasHeightForWidth())
        self.pushButton_batalKeranjang.setSizePolicy(sizePolicy1)
        self.pushButton_batalKeranjang.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 6px 8px; ;\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	\n"
"	background-color: rgb(190, 0, 0);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */\n"
"	\n"
"	background-color: rgb(190, 0, 0);\n"
"    color: white;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_batalKeranjang, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.pushButton_buatKeranjang = QPushButton(self.tab_2)
        self.pushButton_buatKeranjang.setObjectName(u"pushButton_buatKeranjang")
        self.pushButton_buatKeranjang.setStyleSheet(u"QPushButton { \n"
"		background-color: rgb(85, 255, 0);\n"
"	border-radius: 5px;\n"
"padding: 6px 8px; \n"
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

        self.gridLayout.addWidget(self.pushButton_buatKeranjang, 0, 3, 1, 1)

        self.pushButton_refresh = QPushButton(self.tab_2)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius:5px;\n"
"	border-radius: 5px;\n"
"padding: 6px 8px; \n"
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

        self.gridLayout.addWidget(self.pushButton_refresh, 0, 4, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 120))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"\n"
"border-radius: 2px;\n"
"")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 6)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(450, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_namaObat = QLabel(self.tab_2)
        self.label_namaObat.setObjectName(u"label_namaObat")
        self.label_namaObat.setMaximumSize(QSize(450, 16777215))
        self.label_namaObat.setFont(font3)
        self.label_namaObat.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_namaObat, 7, 0, 1, 1)

        self.lineEdit_namaObat = QLineEdit(self.tab_2)
        self.lineEdit_namaObat.setObjectName(u"lineEdit_namaObat")
        self.lineEdit_namaObat.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 6px 8px; \n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.lineEdit_namaObat, 7, 2, 1, 1)

        self.pushButton_cariObat = QPushButton(self.tab_2)
        self.pushButton_cariObat.setObjectName(u"pushButton_cariObat")
        self.pushButton_cariObat.setMaximumSize(QSize(700, 16777215))
        self.pushButton_cariObat.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"	border-radius: 5px;\n"
"padding: 6px 40px; \n"
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

        self.gridLayout.addWidget(self.pushButton_cariObat, 7, 3, 1, 2)

        self.lineEdit_jumlahObat = QLineEdit(self.tab_2)
        self.lineEdit_jumlahObat.setObjectName(u"lineEdit_jumlahObat")
        self.lineEdit_jumlahObat.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 6px 8px; \n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.lineEdit_jumlahObat, 8, 2, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
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
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(163)

        self.gridLayout.addWidget(self.tableWidget_2, 6, 0, 1, 6)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(226, 226, 226);\n"
"border-radius: 5px;\n"
"padding: 6px 8px;")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.pushButton_simpan = QPushButton(self.tab_2)
        self.pushButton_simpan.setObjectName(u"pushButton_simpan")
        self.pushButton_simpan.setMaximumSize(QSize(700, 16777215))
        self.pushButton_simpan.setStyleSheet(u"QPushButton { \n"
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

        self.gridLayout.addWidget(self.pushButton_simpan, 8, 3, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        self.pushButton_keluar.setMaximumSize(QSize(240, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.pushButton_keluar.setFont(font4)
        self.pushButton_keluar.setStyleSheet(u"QPushButton { \n"
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

        self.verticalLayout.addWidget(self.pushButton_keluar, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 854, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">APOTEKER</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Nama/ID :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Keranjang ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total Harga", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Apoteker", None));
        self.pushButton_editKeranjang.setText(QCoreApplication.translate("MainWindow", u"Edit Keranjang", None))
        self.pushButton_lihatDetail.setText(QCoreApplication.translate("MainWindow", u"Lihat Detail", None))
        self.pushButton_kirimKasir.setText(QCoreApplication.translate("MainWindow", u"Kirim Kasir", None))
        self.pushButton_batalKeranjang.setText(QCoreApplication.translate("MainWindow", u"Batalkan Keranjang", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lihat Keranjang", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Masukkan Jumlah Obat   :", None))
        self.pushButton_buatKeranjang.setText(QCoreApplication.translate("MainWindow", u"Buat Keranjang", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" Pilih obat yang ingin ditambahkan!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nama Pembeli  :", None))
        self.label_namaObat.setText(QCoreApplication.translate("MainWindow", u"Masukkan Nama Obat  :", None))
        self.pushButton_cariObat.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Kadaluarsa", None));
        self.pushButton_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tambah Data Keranjang", None))
        self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi


from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from backend.apoteker import (
    cariObatLayakJual, buatKeranjang, lihatKeranjang,
    tambahObatKeKeranjang, updateJumlahObatYangDiBeli,
    hapusObatDariKeranjang, kirimKeranjangKeKasir, batalkanKeranjang
)
from backend.login import session

class DashboardApoteker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.keranjang_id_aktif = None  # Track keranjang yang sedang aktif
        
        # Koneksi tombol logout
        if hasattr(self.ui, "pushButton_keluar"):
            self.ui.pushButton_keluar.clicked.connect(self.logout_to_login)
        
        # Connect buttons Tab Lihat Keranjang (tab index 0)
        if hasattr(self.ui, "pushButton"):  # Button Cari
            self.ui.pushButton.clicked.connect(self.cari_keranjang)
        if hasattr(self.ui, "pushButton_2"):  # Button Refresh
            self.ui.pushButton_2.clicked.connect(self.refresh_data_keranjang)
        if hasattr(self.ui, "pushButton_batalKeranjang"):
            self.ui.pushButton_batalKeranjang.clicked.connect(self.batal_keranjang)
        if hasattr(self.ui, "pushButton_lihatDetail"):
            self.ui.pushButton_lihatDetail.clicked.connect(self.lihat_detail_keranjang)
        if hasattr(self.ui, "pushButton_kirimKasir"):
            self.ui.pushButton_kirimKasir.clicked.connect(self.kirim_ke_kasir)
        if hasattr(self.ui, "pushButton_editKeranjang"):
            self.ui.pushButton_editKeranjang.clicked.connect(self.edit_keranjang)
        
        # Connect buttons Tab Tambah Data Keranjang (tab index 1)
        if hasattr(self.ui, "pushButton_buatKeranjang"):
            self.ui.pushButton_buatKeranjang.clicked.connect(self.buat_keranjang_baru)
        if hasattr(self.ui, "pushButton_simpan"):
            self.ui.pushButton_simpan.clicked.connect(self.tambah_obat_ke_keranjang)
        if hasattr(self.ui, "pushButton_refresh"):
            self.ui.pushButton_refresh.clicked.connect(self.refresh_form_tambah)
        
        if hasattr(self.ui, "pushButton_cariObat"):
            self.ui.pushButton_cariObat.clicked.connect(self.cari_obat)
        
        # Tampilkan info user
        try:
            username = session.get('dataUser', {}).get('username', 'Apoteker')
            self.ui.textBrowser.setHtml(f"<h2>Selamat Datang, {username}</h2><p>Dashboard Apoteker - Kelola Obat dan Keranjang</p>")
        except Exception:
            pass
        
        # Load data awal
        self.refresh_data_keranjang()
        self.refresh_data_obat()

    # ===== TAB LIHAT KERANJANG =====
    def refresh_data_keranjang(self):
        """Load semua data keranjang ke tableWidget"""
        try:
            if hasattr(self.ui, 'tableWidget'):
                self.ui.tableWidget.setRowCount(0)
                # Query semua keranjang yang statusnya 'pending' atau 'dikirim'
                from backend.koneksi import koneksiKeDatabase
                db = koneksiKeDatabase()
                if db is None:
                    return
                
                cursor = db.cursor()
                query = """
                    SELECT k.keranjangId, k.namaPembeli, k.totalHarga, k.status, u.nama
                    FROM keranjang k
                    JOIN user u ON k.apotekerId = u.userId
                    WHERE k.status IN ('draft', 'dikirim')
                    ORDER BY k.keranjangId DESC
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                db.close()
                
                for d in data:
                    row = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row)
                    
                    if isinstance(d, dict):
                        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d.get('keranjangId', ''))))
                        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d.get('namaPembeli', ''))))
                        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {d.get('totalHarga', 0):,}"))
                        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d.get('status', ''))))
                        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d.get('nama', ''))))
                    else:
                        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d[0])))
                        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d[1])))
                        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {d[2]:,}"))
                        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d[3])))
                        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d[4])))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load keranjang: {e}")
    
    def cari_keranjang(self):
        """Cari keranjang berdasarkan nama pembeli atau keranjang ID"""
        try:
            keyword = self.ui.lineEdit_2.text().strip()
            if not keyword:
                self.refresh_data_keranjang()
                return
            
            # Filter data keranjang
            from backend.koneksi import koneksiKeDatabase
            db = koneksiKeDatabase()
            if db is None:
                return
            
            cursor = db.cursor()
            # Cek apakah keyword adalah angka (keranjangId) atau string (nama pembeli)
            query = """
                SELECT k.keranjangId, k.namaPembeli, k.totalHarga, k.status, u.nama
                FROM keranjang k
                JOIN user u ON k.apotekerId = u.userId
                WHERE (k.namaPembeli LIKE %s OR k.keranjangId = %s)
                AND k.status IN ('draft', 'dikirim')
                ORDER BY k.keranjangId DESC
            """
            # Coba konversi ke int untuk keranjangId, jika gagal set ke -1
            try:
                keranjang_id_search = int(keyword)
            except ValueError:
                keranjang_id_search = -1
            
            cursor.execute(query, (f"%{keyword}%", keranjang_id_search))
            data = cursor.fetchall()
            cursor.close()
            db.close()
            
            self.ui.tableWidget.setRowCount(0)
            for d in data:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                
                if isinstance(d, dict):
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d.get('keranjangId', ''))))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d.get('namaPembeli', ''))))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {d.get('totalHarga', 0):,}"))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d.get('status', ''))))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d.get('nama', ''))))
                else:
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d[0])))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d[1])))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"Rp {d[2]:,}"))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d[3])))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d[4])))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal cari keranjang: {e}")
    
    def batal_keranjang(self):
        """Batalkan keranjang yang dipilih"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan dibatalkan!")
                return
            
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_pembeli = self.ui.tableWidget.item(selected, 1).text()
            
            reply = QMessageBox.question(
                self,
                "Konfirmasi Batal",
                f"Yakin ingin membatalkan keranjang '{nama_pembeli}'?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = batalkanKeranjang(keranjang_id)
                QMessageBox.information(self, "Info", pesan)
                self.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal batalkan keranjang: {e}")
    
    def lihat_detail_keranjang(self):
        """Buka window detail keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan dilihat detailnya!")
                return
            
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            
            from detailKeranjangApoteker import DetailKeranjangApotekerWindow
            self.detail_window = DetailKeranjangApotekerWindow(keranjang_id, parent=self)
            self.detail_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal buka detail: {e}")
    
    def edit_keranjang(self):
        """Buka window edit keranjang"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan diedit!")
                return
            
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_pembeli = self.ui.tableWidget.item(selected, 1).text()
            
            from updateObatKeranjang import UpdateObatKeranjangWindow
            self.edit_window = UpdateObatKeranjangWindow(keranjang_id, nama_pembeli, parent=self)
            self.edit_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal buka edit keranjang: {e}")
    
    def kirim_ke_kasir(self):
        """Kirim keranjang ke kasir"""
        try:
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih keranjang yang akan dikirim ke kasir!")
                return
            
            keranjang_id = self.ui.tableWidget.item(selected, 0).text()
            nama_pembeli = self.ui.tableWidget.item(selected, 1).text()
            
            reply = QMessageBox.question(
                self,
                "Konfirmasi Kirim",
                f"Yakin ingin mengirim keranjang '{nama_pembeli}' ke kasir?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = kirimKeranjangKeKasir(keranjang_id)
                QMessageBox.information(self, "Info", pesan)
                self.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal kirim ke kasir: {e}")
    
    # ===== TAB TAMBAH DATA KERANJANG =====
    def refresh_data_obat(self):
        """Load data obat layak jual ke tableWidget_2"""
        try:
            if hasattr(self.ui, 'tableWidget_2'):
                self.ui.tableWidget_2.setRowCount(0)
                data = cariObatLayakJual()  # Tanpa keyword = tampilkan semua
                
                if isinstance(data, str):
                    return
                
                for d in data:
                    row = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row)
                    
                    if isinstance(d, dict):
                        # Headers: Nama Obat | Jenis | Harga | Stok | Kadaluarsa
                        item_nama = QTableWidgetItem(str(d.get('namaObat', '')))
                        item_nama.setData(Qt.UserRole, d.get('obatId', ''))  # Simpan obatId sebagai data tersembunyi
                        self.ui.tableWidget_2.setItem(row, 0, item_nama)
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d.get('jenis', ''))))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(f"Rp {d.get('harga', 0):,}"))
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(d.get('stok', ''))))
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(d.get('kadaluarsa', ''))))
                    else:
                        # d[0]=obatId, d[1]=namaObat, d[2]=jenis, d[3]=kategoriId, d[4]=harga, d[5]=stok, d[6]=tgl_produksi, d[7]=kadaluarsa
                        # Headers: Nama Obat | Jenis | Harga | Stok | Kadaluarsa
                        item_nama = QTableWidgetItem(str(d[1]))  # namaObat
                        item_nama.setData(Qt.UserRole, d[0])  # Simpan obatId sebagai data tersembunyi
                        self.ui.tableWidget_2.setItem(row, 0, item_nama)
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d[2])))  # jenis
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(f"Rp {d[4]:,}"))  # harga
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(d[5])))  # stok
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(d[7])))  # kadaluarsa
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load obat: {e}")
    
    def buat_keranjang_baru(self):
        """Buat keranjang baru dengan nama pembeli"""
        try:
            nama_pembeli = self.ui.lineEdit.text().strip()
            
            if not nama_pembeli:
                QMessageBox.warning(self, "Peringatan", "Nama pembeli harus diisi!")
                return
            
            # Ambil apotekerId dari session
            apoteker_id = session.get('userId')
            if not apoteker_id:
                QMessageBox.warning(self, "Peringatan", "Session user tidak ditemukan!")
                return
            
            # Buat keranjang
            keranjang_id = buatKeranjang(apoteker_id, nama_pembeli)
            
            if isinstance(keranjang_id, str):
                QMessageBox.warning(self, "Error", keranjang_id)
                return
            
            self.keranjang_id_aktif = keranjang_id
            QMessageBox.information(self, "Sukses", f"Keranjang baru berhasil dibuat!\nID Keranjang: {keranjang_id}\nNama Pembeli: {nama_pembeli}\n\nSekarang pilih obat dan tambahkan ke keranjang.")
            
            # Update label info
            self.ui.label_3.setText(f"Keranjang Aktif - ID: {keranjang_id} | Pembeli: {nama_pembeli}\nPilih obat dari tabel, input jumlah, lalu klik Simpan.")
            
            # Refresh keranjang tab
            self.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal buat keranjang: {e}")
    
    def tambah_obat_ke_keranjang(self):
        """Tambahkan obat yang dipilih ke keranjang aktif"""
        try:
            if not self.keranjang_id_aktif:
                QMessageBox.warning(self, "Peringatan", "Buat keranjang terlebih dahulu!")
                return
            
            # Ambil obat yang dipilih dari tabel
            selected = self.ui.tableWidget_2.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat dari tabel!")
                return
            
            # Ambil obatId dari data tersembunyi di kolom 0 (Nama Obat)
            obat_id = self.ui.tableWidget_2.item(selected, 0).data(Qt.UserRole)
            nama_obat = self.ui.tableWidget_2.item(selected, 0).text()
            
            # Ambil jumlah
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
            
            # Tambahkan ke keranjang
            pesan = tambahObatKeKeranjang(self.keranjang_id_aktif, obat_id, jumlah)
            QMessageBox.information(self, "Info", pesan)
            
            # Clear input fields
            self.ui.lineEdit_jumlahObat.clear()
            self.ui.lineEdit_namaObat.clear()
            
            # Refresh data obat (untuk update stok dan reset tampilan ke semua obat)
            self.refresh_data_obat()
            
            # Refresh keranjang tab
            self.refresh_data_keranjang()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal tambah obat: {e}")
    
    def cari_obat(self):
        """Cari obat berdasarkan nama"""
        try:
            keyword = self.ui.lineEdit_namaObat.text().strip()
            
            if not keyword:
                QMessageBox.warning(self, "Peringatan", "Masukkan nama obat untuk dicari!")
                return
            
            # Cari obat dengan keyword
            if hasattr(self.ui, 'tableWidget_2'):
                self.ui.tableWidget_2.setRowCount(0)
                data = cariObatLayakJual(keyword)
                
                if isinstance(data, str):
                    QMessageBox.information(self, "Info", data)
                    return
                
                for d in data:
                    row = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row)
                    
                    if isinstance(d, dict):
                        # Headers: Nama Obat | Jenis | Harga | Stok | Kadaluarsa
                        item_nama = QTableWidgetItem(str(d.get('namaObat', '')))
                        item_nama.setData(Qt.UserRole, d.get('obatId', ''))  # Simpan obatId sebagai data tersembunyi
                        self.ui.tableWidget_2.setItem(row, 0, item_nama)
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d.get('jenis', ''))))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(f"Rp {d.get('harga', 0):,}"))
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(d.get('stok', ''))))
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(d.get('kadaluarsa', ''))))
                    else:
                        # d[0]=obatId, d[1]=namaObat, d[2]=jenis, d[3]=kategoriId, d[4]=harga, d[5]=stok, d[6]=tgl_produksi, d[7]=kadaluarsa
                        # Headers: Nama Obat | Jenis | Harga | Stok | Kadaluarsa
                        item_nama = QTableWidgetItem(str(d[1]))  # namaObat
                        item_nama.setData(Qt.UserRole, d[0])  # Simpan obatId sebagai data tersembunyi
                        self.ui.tableWidget_2.setItem(row, 0, item_nama)
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d[2])))  # jenis
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(f"Rp {d[4]:,}"))  # harga
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(d[5])))  # stok
                        self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(d[7])))  # kadaluarsa
                
                if self.ui.tableWidget_2.rowCount() == 0:
                    QMessageBox.information(self, "Info", f"Tidak ada obat dengan nama '{keyword}'")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal mencari obat: {e}")
    
    def refresh_form_tambah(self):
        """Reset form tambah keranjang"""
        self.ui.lineEdit.clear()
        self.ui.lineEdit_jumlahObat.clear()
        self.ui.label_3.setText("Silakan buat keranjang baru dengan mengisi nama pembeli dan klik 'Buat Keranjang'")
        self.keranjang_id_aktif = None
        self.refresh_data_obat()

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

