# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tambah_Obat.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(453, 415)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(9000, 60))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 6px 8px;")

        self.gridLayout_2.addWidget(self.comboBox, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
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

        self.gridLayout.addWidget(self.pushButton_batal, 0, 0, 1, 1)

        self.pushButton_simpan = QPushButton(self.centralwidget)
        self.pushButton_simpan.setObjectName(u"pushButton_simpan")
        self.pushButton_simpan.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(49, 245, 46);\n"
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

        self.gridLayout.addWidget(self.pushButton_simpan, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 453, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tambah Obat + ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tgl Produksi        :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stok                   :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Harga                :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Obat       :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tgl Kadaluarsa     :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kategori Obat     :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jenis Obat         :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Obat Bebas", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Obat Bebas Terbatas", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Obat Keras", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Obat Narkotika & Psikotropika", None))

        self.pushButton_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.pushButton_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
    # retranslateUi

