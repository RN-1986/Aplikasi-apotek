# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(594, 515)
        MainWindow.setStyleSheet(u"background-color: rgb(187, 255, 253);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 411, 101))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-radius: 30px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"width: 200px;\n"
"height: 50px;\n"
"text-align: center;      \n"
"line-height: 50px;  \n"
"border: 3px solid white;   ")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setMargin(14)
        self.label.setIndent(13)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 140, 411, 221))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
" border: 3px solid white;   \n"
"border-radius: 20px;   ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(224, 390, 141, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 20px;\n"
"border-width: 2px;            \n"
"border-style: solid;       \n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 390, 75, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 2px;            \n"
"border-style: solid;       \n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 390, 75, 41))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 2px;            \n"
"border-style: solid;       \n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 190, 211, 51))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 280, 211, 51))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 160, 71, 20))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 20px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 250, 71, 20))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 594, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  \ud83d\udc8aSelamat Datang di Aplikasi Apotek\ud83d\udc8a", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
    # retranslateUi

