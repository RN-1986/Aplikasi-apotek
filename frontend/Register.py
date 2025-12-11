# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "qrc"))
import logo_apotek_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(734, 482)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 161, 21))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, -100, 431, 601))
        self.label_7.setStyleSheet(u"image: url(:/logo-apotek/asset/apotek.jpeg);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(500, 160, 141, 61))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(400, 200, 341, 41))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0, 0);")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 80, 231, 286))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.lineEdit_nama = QLineEdit(self.layoutWidget)
        self.lineEdit_nama.setObjectName(u"lineEdit_nama")
        self.lineEdit_nama.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.lineEdit_nama)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.lineEdit_username = QLineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.lineEdit_username)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.lineEdit_password = QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.lineEdit_konfirmasipass = QLineEdit(self.layoutWidget)
        self.lineEdit_konfirmasipass.setObjectName(u"lineEdit_konfirmasipass")
        self.lineEdit_konfirmasipass.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.lineEdit_konfirmasipass)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.comboBox_pilihRole = QComboBox(self.layoutWidget)
        self.comboBox_pilihRole.addItem("")
        self.comboBox_pilihRole.addItem("")
        self.comboBox_pilihRole.addItem("")
        self.comboBox_pilihRole.setObjectName(u"comboBox_pilihRole")
        self.comboBox_pilihRole.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.comboBox_pilihRole)

        self.pushButton_register = QPushButton(self.centralwidget)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setGeometry(QRect(60, 390, 101, 30))
        self.pushButton_register.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* transparan */\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: black; /* default text color */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60); /* abu-abu gelap */\n"
"    color: white;\n"
"}\n"
"\n"
"/* Selected (checked) state */\n"
"QPushButton:checked {\n"
"    background-color: rgb(60, 60, 60); /* abu-abu gelap */\n"
"    color: white;\n"
"    border-color: rgb(80, 80, 80); /* sedikit lebih gelap */\n"
"}\n"
"")
        self.pushButton_kembali = QPushButton(self.centralwidget)
        self.pushButton_kembali.setObjectName(u"pushButton_kembali")
        self.pushButton_kembali.setGeometry(QRect(230, 390, 101, 31))
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        self.pushButton_kembali.setFont(font3)
        self.pushButton_kembali.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0); /* transparan */\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: black; /* default text color */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60); /* abu-abu gelap */\n"
"    color: white;\n"
"}\n"
"\n"
"/* Selected (checked) state */\n"
"QPushButton:checked {\n"
"    background-color: rgb(60, 60, 60); /* abu-abu gelap */\n"
"    color: white;\n"
"    border-color: rgb(80, 80, 80); /* sedikit lebih gelap */\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget.raise_()
        self.pushButton_register.raise_()
        self.pushButton_kembali.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FORM REGISTER", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Halo, Teman", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Daftarkan diri anda dan mulai gunakan layanan kami segera", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Konfirmasi Password:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pilih Role:", None))
        self.comboBox_pilihRole.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.comboBox_pilihRole.setItemText(1, QCoreApplication.translate("MainWindow", u"Apoteker", None))
        self.comboBox_pilihRole.setItemText(2, QCoreApplication.translate("MainWindow", u"Kasir", None))

        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_kembali.setText(QCoreApplication.translate("MainWindow", u"\u21a9", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
