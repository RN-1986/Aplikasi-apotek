# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hapusObat.ui'
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
        MainWindow.resize(471, 526)
        MainWindow.setStyleSheet(u"background-color: rgb(187, 255, 253);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 151, 51))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QRect(200, 180, 201, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 330, 121, 22))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_6.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 280, 121, 22))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_5.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(71, 181, 117, 22))
        self.label_3.setFont(font2)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QRect(200, 330, 201, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 420, 91, 31))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 230, 117, 22))
        self.label_4.setFont(font2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 420, 91, 31))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(49, 245, 46);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QRect(200, 230, 201, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 130, 116, 22))
        self.label_2.setFont(font2)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(200, 130, 201, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QRect(200, 280, 201, 31))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 471, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setFixedSize(MainWindow.size())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"         Hapus Obat ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tgl Kadaluarsa     :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stok                   :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jenis Obat         :", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Harga                :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Obat       :", None))
    # retranslateUi

class HapusObatWindow(QMainWindow):
    def __init__(self, obatId, parent=None):
        super().__init__(parent)
        self._obatId = obatId
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            if hasattr(self.ui, "pushButton"):
                self.ui.pushButton.clicked.connect(self.confirm_hapus)
            if hasattr(self.ui, "pushButton_2"):
                self.ui.pushButton_2.clicked.connect(self.close)
        except Exception:
            pass

    def confirm_hapus(self):
        from backend.admin import hapusObat
        from PySide6.QtWidgets import QMessageBox
        pesan = hapusObat(self._obatId)
        QMessageBox.information(self, "Info", pesan)
        self.close()
        try:
            if hasattr(self.parent(), "refresh_data_obat"):
                self.parent().refresh_data_obat()
        except Exception:
            pass

