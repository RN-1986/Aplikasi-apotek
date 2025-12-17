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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import logo_apotek_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 632)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        self.pushButton_keluar.setMinimumSize(QSize(140, 0))
        self.pushButton_keluar.setMaximumSize(QSize(240, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_keluar.setFont(font)
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

        self.gridLayout_4.addWidget(self.pushButton_keluar, 3, 0, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 450))
        self.tabWidget.setMaximumSize(QSize(16777215, 450))
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
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_delete = QPushButton(self.tab)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setStyleSheet(u"QPushButton { \n"
"border-radius: 5px;\n"
"padding: 8px 8px; \n"
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

        self.gridLayout.addWidget(self.pushButton_delete, 0, 2, 1, 1)

        self.pushButton_tambah = QPushButton(self.tab)
        self.pushButton_tambah.setObjectName(u"pushButton_tambah")
        self.pushButton_tambah.setStyleSheet(u"QPushButton { \n"
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

        self.gridLayout.addWidget(self.pushButton_tambah, 0, 0, 1, 1)

        self.pushButton_edit = QPushButton(self.tab)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(255, 255, 0);	\n"
"	border-radius: 5px;\n"
"padding: 8px 8px; \n"
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

        self.gridLayout.addWidget(self.pushButton_edit, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        font2 = QFont()
        font2.setPointSize(11)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
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
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(121)

        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"\n"
"border radius: 5px;\n"
"")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_search = QPushButton(self.tab)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setStyleSheet(u"\n"
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

        self.gridLayout_2.addWidget(self.pushButton_search, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"background-color: rgb(226, 226, 226);")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton_refresh = QPushButton(self.tab)
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

        self.gridLayout_2.addWidget(self.pushButton_refresh, 1, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"border radius: 5px;")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QDateEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"background-color: rgb(226, 226, 226);")
        self.lineEdit_2.setCalendarPopup(True)
        self.lineEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_2.setDate(QDate.currentDate())

        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_jam = QLabel(self.tab_2)
        self.label_jam.setObjectName(u"label_jam")
        self.label_jam.setStyleSheet(u"\n"
"border radius: 5px;")

        self.gridLayout_5.addWidget(self.label_jam, 0, 2, 1, 1)

        self.spinBox_jam = QSpinBox(self.tab_2)
        self.spinBox_jam.setObjectName(u"spinBox_jam")
        self.spinBox_jam.setStyleSheet(u"border-radius: 5px;\n"
"padding: 6px 8px; \n"
"background-color: rgb(226, 226, 226);")
        self.spinBox_jam.setMinimum(-1)
        self.spinBox_jam.setMaximum(23)
        self.spinBox_jam.setValue(-1)
        self.spinBox_jam.setSpecialValueText("Semua")

        self.gridLayout_5.addWidget(self.spinBox_jam, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.tab_2)
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

        self.gridLayout_5.addWidget(self.pushButton, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_2)
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

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
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
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(210)

        self.verticalLayout.addWidget(self.tableWidget_2)

        self.pushButton_LihatDetail = QPushButton(self.tab_2)
        self.pushButton_LihatDetail.setObjectName(u"pushButton_LihatDetail")
        self.pushButton_LihatDetail.setStyleSheet(u"\n"
"QPushButton { \n"
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

        self.verticalLayout.addWidget(self.pushButton_LihatDetail)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 70))
        self.textBrowser.setStyleSheet(u"background-color: rgb(125, 192, 211);\n"
"BORDER-RADIUS:5PX;")

        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Data -", None))
        self.pushButton_tambah.setText(QCoreApplication.translate("MainWindow", u"Tambah Data +", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Obat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Jenis", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tgl Produksi", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kadaluarsa", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Nama atau ID obat", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Kelola Data Obat", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" Tanggal :", None))
        self.label_jam.setText(QCoreApplication.translate("MainWindow", u" Jam :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID Transaksi", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Kasir", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Total Harga(Rp)", None));
        self.pushButton_LihatDetail.setText(QCoreApplication.translate("MainWindow", u"Lihat Detail", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Riwayat Transaksi", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">DASHBOARD</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">ADMIN</span></p></body></html>", None))
    # retranslateUi


from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from backend.admin import (
    lihatSemuaDataObat, tambahObat, updateObat, hapusObat,
    lihatSemuaTransaksi, lihatDetailTransaksi, cariObat
)
from backend.login import session

class DashboardAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect button keluar/logout
        if hasattr(self.ui, "pushButton_keluar"):
            self.ui.pushButton_keluar.clicked.connect(self.logout_to_login)
        
        # Connect button di tab Kelola Obat
        if hasattr(self.ui, "pushButton_tambah"):
            self.ui.pushButton_tambah.clicked.connect(self.open_tambah_obat)
        if hasattr(self.ui, "pushButton_edit"):
            self.ui.pushButton_edit.clicked.connect(self.open_edit_obat)
        if hasattr(self.ui, "pushButton_delete"):
            self.ui.pushButton_delete.clicked.connect(self.hapus_obat)
        if hasattr(self.ui, "pushButton_search"):
            self.ui.pushButton_search.clicked.connect(self.cari_obat_action)
        if hasattr(self.ui, "pushButton_refresh"):
            self.ui.pushButton_refresh.clicked.connect(self.refresh_data_obat)
        
        # Connect button di tab Riwayat Transaksi
        if hasattr(self.ui, "pushButton"):  # Button Cari transaksi
            self.ui.pushButton.clicked.connect(self.cari_transaksi_by_date)
        if hasattr(self.ui, "pushButton_2"):  # Button Refresh transaksi
            self.ui.pushButton_2.clicked.connect(self.refresh_data_transaksi)
        if hasattr(self.ui, "pushButton_LihatDetail"):  # Button Lihat Detail
            self.ui.pushButton_LihatDetail.clicked.connect(self.open_detail_transaksi)
        
        try:
            username = session.get('dataUser', {}).get('username', 'Admin')
            self.ui.textBrowser.setHtml(f"<h2 style='text-align:center'>DASHBOARD ADMIN</h2><p style='text-align:center'>Selamat Datang, {username}</p>")
        except Exception:
            pass
        
        # Load data
        self.refresh_data_obat()
        self.refresh_data_transaksi()

    def refresh_data_obat(self):
        try:
            if hasattr(self.ui, 'tableWidget'):
                self.ui.tableWidget.setRowCount(0)
                data = lihatSemuaDataObat()
                if isinstance(data, str):
                    QMessageBox.information(self, "Info", data)
                    return
                for d in data:
                    row = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row)
                    
                    # Format harga as integer if it's a whole number
                    harga_val = d.get('harga', '')
                    if isinstance(harga_val, (int, float)):
                        harga_str = str(int(harga_val)) if float(harga_val) == int(harga_val) else str(harga_val)
                    else:
                        harga_str = str(harga_val)
                    
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d.get('obatId', ''))))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d.get('namaObat', '')).title()))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(d.get('jenis', '')).title()))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d.get('namaKategori', ''))))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(harga_str))
                    self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(d.get('stok', ''))))
                    self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(d.get('tgl_produksi', ''))))
                    self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(d.get('kadaluarsa', ''))))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load data: {e}")

    def open_tambah_obat(self):
        """Buka window tambah obat"""
        try:
            from tambah_Obat import TambahObatWindow
            self.tambah_window = TambahObatWindow(parent=self)
            self.tambah_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal membuka form tambah obat: {e}")
    
    def open_edit_obat(self):
        """Buka window edit obat"""
        try:
            # Ambil baris yang dipilih
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat yang akan diedit!")
                return
            
            # Ambil obatId dari kolom pertama
            obat_id = self.ui.tableWidget.item(selected, 0).text()
            
            from updateObat import UpdateObatWindow
            self.edit_window = UpdateObatWindow(obat_id, parent=self)
            self.edit_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal membuka form edit obat: {e}")
    
    def hapus_obat(self):
        """Hapus obat yang dipilih"""
        try:
            # Ambil baris yang dipilih
            selected = self.ui.tableWidget.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih obat yang akan dihapus!")
                return
            
            # Ambil obatId dari kolom pertama
            obat_id = self.ui.tableWidget.item(selected, 0).text()
            nama_obat = self.ui.tableWidget.item(selected, 1).text()
            
            # Konfirmasi hapus
            reply = QMessageBox.question(
                self, 
                "Konfirmasi Hapus", 
                f"Yakin ingin menghapus obat '{nama_obat}'?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                pesan = hapusObat(obat_id)
                QMessageBox.information(self, "Info", pesan)
                self.refresh_data_obat()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menghapus obat: {e}")
    
    def cari_obat_action(self):
        """Cari obat berdasarkan keyword"""
        try:
            keyword = self.ui.lineEdit.text().strip()
            
            if not keyword:
                self.refresh_data_obat()
                return
            
            data = cariObat(keyword)
            
            if isinstance(data, str):
                QMessageBox.information(self, "Info", data)
                return
            
            # Tampilkan hasil pencarian
            self.ui.tableWidget.setRowCount(0)
            for d in data:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                
                if isinstance(d, dict):
                    # Format harga as integer if it's a whole number
                    harga_val = d.get('harga', '')
                    if isinstance(harga_val, (int, float)):
                        harga_str = str(int(harga_val)) if float(harga_val) == int(harga_val) else str(harga_val)
                    else:
                        harga_str = str(harga_val)
                    
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d.get('obatId', ''))))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d.get('namaObat', ''))))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(d.get('jenis', ''))))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d.get('namaKategori', ''))))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(harga_str))
                    self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(d.get('stok', ''))))
                    self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(d.get('tgl_produksi', ''))))
                    self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(d.get('kadaluarsa', ''))))
                else:
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(d[0])))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(d[1])))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(d[2])))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(d[7]) if len(d) > 7 else ''))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(d[3])))
                    self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(d[4])))
                    self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(d[5])))
                    self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(d[6])))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal mencari obat: {e}")
    
    def refresh_data_transaksi(self):
        """Load data riwayat transaksi ke tableWidget_2"""
        try:
            if hasattr(self.ui, 'tableWidget_2'):
                self.ui.tableWidget_2.setRowCount(0)
                data = lihatSemuaTransaksi()
                
                if isinstance(data, str):
                    return
                
                for d in data:
                    row = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row)
                    
                    if isinstance(d, dict):
                        transaksi_id = str(d.get('transaksiId', ''))
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(transaksi_id))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d.get('tanggalTransaksi', ''))))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d.get('Kasir', ''))))
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(f"Rp {d.get('totalHarga', 0):,}"))
                    else:
                        transaksi_id = str(d[0])
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(transaksi_id))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d[1])))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d[2])))
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(f"Rp {d[3]:,}"))
                
                # Connect double click untuk lihat detail
                self.ui.tableWidget_2.doubleClicked.connect(self.open_detail_transaksi)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load transaksi: {e}")
    
    def cari_transaksi_by_date(self):
        """Cari transaksi berdasarkan tanggal dan jam"""
        try:
            # Ambil tanggal dan jam yang dipilih
            selected_date = self.ui.lineEdit_2.date()
            tanggal_str = selected_date.toString("yyyy-MM-dd")
            jam_pilihan = int(self.ui.spinBox_jam.value())
            
            tanggalDanJam = f"{tanggal_str} {jam_pilihan:02d}:00:00"
            
            # Load semua data transaksi
            data = lihatSemuaTransaksi()
            
            if isinstance(data, str):
                QMessageBox.information(self, "Info", data)
                return
            
            # Filter berdasarkan tanggal dan jam
            self.ui.tableWidget_2.setRowCount(0)
            found = False
            
            for d in data:
                if isinstance(d, dict):
                    tgl_transaksi = str(d.get('tanggalTransaksi', ''))
                else:
                    tgl_transaksi = str(d[1])
                
                # Cek apakah tanggal cocok
                if tanggal_str in tgl_transaksi:
                    # Jika jam dipilih (bukan -1/Semua), filter berdasarkan jam
                    if jam_pilihan >= 0:
                        # Extract jam dari datetime string
                        # Format biasanya: 2025-12-15 13:45:30
                        try:
                            waktu_parts = tgl_transaksi.split()
                            if len(waktu_parts) >= 2:
                                jam_parts = waktu_parts[1].split(':')
                                jam_transaksi = int(jam_parts[0])
                                
                                # Hanya tampilkan jika jam cocok
                                if jam_transaksi != jam_pilihan:
                                    continue
                        except:
                            # Jika gagal parse, skip filter jam
                            pass
                    
                    # Tambahkan ke tabel
                    found = True
                    row = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row)
                    
                    if isinstance(d, dict):
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(d.get('transaksiId', ''))))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d.get('tanggalTransaksi', ''))))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d.get('Kasir', ''))))
                        total_harga = d.get('totalHarga', 0)
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(f"Rp {total_harga:,}"))
                    else:
                        self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(d[0])))
                        self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(d[1])))
                        self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(d[2])))
                        self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(f"Rp {d[3]:,}"))
            
            if not found:
                jam_info = f" jam {jam_pilihan}" if jam_pilihan >= 0 else ""
                QMessageBox.information(self, "Info", f"Tidak ada transaksi pada tanggal '{tanggal_str}'{jam_info}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal mencari transaksi: {e}")
    
    def open_detail_transaksi(self):
        """Buka window detail transaksi"""
        try:
            selected = self.ui.tableWidget_2.currentRow()
            if selected < 0:
                QMessageBox.warning(self, "Peringatan", "Pilih transaksi yang akan dilihat detailnya!")
                return
            
            # Ambil transaksiId dari kolom pertama
            transaksi_id = self.ui.tableWidget_2.item(selected, 0).text()
            
            from detailRiwayatTransaksi import DetailRiwayatWindow
            self.detail_window = DetailRiwayatWindow(transaksi_id, parent=self)
            self.detail_window.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal membuka detail transaksi: {e}")

    def logout_to_login(self):
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
