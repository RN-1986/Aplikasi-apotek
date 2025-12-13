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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QMessageBox)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))
import logo_apotek_rc
from backend.login import login, session
from backend.logout import logout as backend_logout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(665, 535)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, -120, 481, 671))
        self.label.setStyleSheet(u"image: url(:/logo-apotek/asset/apotek.jpeg);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 180, 271, 41))
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: black;\n"
"font-size: 18px;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 90, 111, 31))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.pushButton_register = QPushButton(self.centralwidget)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setGeometry(QRect(420, 410, 151, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_register.setFont(font2)
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
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 370, 211, 16))
        font3 = QFont()
        font3.setPointSize(7)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: black;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 190, 241, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 20px;")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 20px;")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(226, 226, 226);\n"
"padding: 6px 8px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 410, 241, 51))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_logout = QPushButton(self.layoutWidget1)
        self.pushButton_logout.setObjectName(u"pushButton_logout")
        self.pushButton_logout.setFont(font2)
        self.pushButton_logout.setStyleSheet(u"QPushButton { \n"
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

        self.gridLayout.addWidget(self.pushButton_logout, 0, 0, 1, 1)

        self.pushButton_login = QPushButton(self.layoutWidget1)
        self.pushButton_login.setObjectName(u"pushButton_login")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.pushButton_login.setFont(font5)
        self.pushButton_login.setStyleSheet(u"QPushButton { \n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;\n"
"padding: 6px 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Saat kursor hover */\n"
"QPushButton:hover {\n"
"     /* warna saat hover */\n"
"	background-color: rgb(36, 79, 124);\n"
"	color: white;\n"
"}\n"
"\n"
"/* Saat tombol ditekan */\n"
"QPushButton:pressed {\n"
"     /* warna saat ditekan */	background-color: rgb(36, 79, 124);\n"
"	color: white;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_login, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 665, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Simpan referensi window untuk kontrol show/hide
        self.login_window = MainWindow
        
        # Koneksi tombol Login
        self.pushButton_login.clicked.connect(lambda: self.proses_login(MainWindow))
        
        # Koneksi tombol Register
        self.pushButton_register.clicked.connect(lambda: self.open_register(MainWindow))
        
        # Koneksi tombol Logout
        self.pushButton_logout.clicked.connect(lambda: self.action_logout(MainWindow))
        
        # Enter key di username/password juga trigger login
        self.lineEdit.returnPressed.connect(lambda: self.proses_login(MainWindow))
        self.lineEdit_2.returnPressed.connect(lambda: self.proses_login(MainWindow))
        
        # Update state tombol berdasarkan session
        self.update_button_states()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Halo, selamat datang kembali", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Belum punya akun? silahkan daftar terlebih dahulu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.lineEdit_2.setText("")
        self.pushButton_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

    def update_button_states(self):
        """Update enabled/disabled state untuk tombol berdasarkan session"""
        logged = bool(session.get('is_login'))
        self.pushButton_login.setEnabled(not logged)
        self.pushButton_register.setEnabled(not logged)
        # Logout button selalu aktif sebagai tombol exit
        self.pushButton_logout.setEnabled(True)

    def proses_login(self, MainWindow):
        """Proses login user"""
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()

        if not username or not password:
            QMessageBox.warning(MainWindow, "Peringatan", "Username dan password harus diisi!")
            return

        pesan = login(username, password)

        if session.get('is_login'):
            QMessageBox.information(MainWindow, "Login Berhasil", pesan)
            role = session.get('role')

            if role == "admin":
                # Import runtime untuk menghindari circular import
                import sys
                sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))
                from dashboardAdmin import DashboardAdmin
                self.window = DashboardAdmin()
                self.window.show()
                # Tutup window login
                self.login_window.close()
            elif role == "apoteker":
                import sys
                sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))
                from dashboardApoteker import DashboardApoteker
                self.window = DashboardApoteker()
                self.window.show()
                self.login_window.close()
            elif role == "kasir":
                import sys
                sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))
                from dashboardKasir import DashboardKasir
                self.window = DashboardKasir()
                self.window.show()
                self.login_window.close()
            else:
                QMessageBox.warning(MainWindow, "Role belum tersedia", f"Role '{role}' belum didukung.")
        else:
            QMessageBox.critical(MainWindow, "Login Gagal", pesan)

    def open_register(self, MainWindow):
        """Buka window register"""
        try:
            from frontend.Register import Ui_MainWindow as Ui_Register
            self.register_win = QMainWindow()
            self.register_ui = Ui_Register()
            self.register_ui.setupUi(self.register_win)
            
            # Koneksi tombol kembali di register
            if hasattr(self.register_ui, 'pushButton_kembali'):
                self.register_ui.pushButton_kembali.clicked.connect(self.register_win.close)
            
            # Koneksi tombol register
            if hasattr(self.register_ui, 'pushButton_register'):
                self.register_ui.pushButton_register.clicked.connect(
                    lambda: self.proses_register(self.register_ui, self.register_win)
                )
            
            self.register_win.show()
        except Exception as e:
            QMessageBox.warning(MainWindow, "Error", f"Gagal membuka form register: {e}")

    def proses_register(self, ui, window):
        """Proses registrasi user baru"""
        try:
            from backend.register import register as backend_register
            
            nama = ui.lineEdit_nama.text().strip()
            username = ui.lineEdit_username.text().strip()
            password = ui.lineEdit_password.text().strip()
            konfirmasi = ui.lineEdit_konfirmasipass.text().strip()
            role = ui.comboBox_pilihRole.currentText().lower()

            if not all([nama, username, password, konfirmasi]):
                QMessageBox.warning(window, "Peringatan", "Semua field harus diisi!")
                return

            if password != konfirmasi:
                QMessageBox.warning(window, "Peringatan", "Password dan konfirmasi tidak cocok!")
                return

            pesan = backend_register(nama, username, password, role)
            QMessageBox.information(window, "Info", pesan)
            window.close()
        except Exception as e:
            QMessageBox.warning(window, "Error", f"Gagal register: {e}")

    def action_logout(self, MainWindow):
        """Logout user dan tutup aplikasi"""
        try:
            # Logout dari session jika sedang login
            if session.get('is_login'):
                pesan = backend_logout()
            else:
                pesan = "Terimakasih"
            
            # Buat message box secara eksplisit agar pasti muncul
            msg = QMessageBox(MainWindow)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Logout")
            msg.setText(pesan)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        except Exception:
            pass
        
        # Tutup aplikasi setelah dialog ditutup
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
