# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget, QVBoxLayout)
from PySide6.QtWidgets import QApplication, QMessageBox
import sys
from frontend.tampilanLogin import tampil_login
from frontend.tampilanRegister import tampil_register
from frontend.tampilanAdmin import tampil_admin
from frontend.tampilanApoteker import tampil_apoteker
from frontend.tampilanKasir import tampil_kasir
from backend.login import session


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Menu Awal")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
            x1:0, y1:0, x2:1, y2:1,
            stop:0 #a8e6cf,
            stop:0.5 #dcedc1,
            stop:1 #f0f4c3
        );
            }
            QLabel {
                color: #1b5e20; /* hijau tua */
                font-weight: bold;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-weight: bold;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #43a047; /* lebih gelap sedikit */
            }
            QPushButton:pressed {
                background-color: #2e7d32;
            }
        """)

        # Widget utama
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Layout utama (vertikal, tengah)
        layout = QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(0, 80, 0, 50)
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignHCenter)

        # Label judul
        self.label = QLabel("💊 Selamat Datang di Aplikasi Apotek 💊")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Tombol Register
        self.pushButton_register = QPushButton("REGISTER")
        self.pushButton_register.setFixedSize(200, 45)
        layout.addWidget(self.pushButton_register, alignment=Qt.AlignCenter)

        # Tombol Login
        self.pushButton_login = QPushButton("LOGIN")
        self.pushButton_login.setFixedSize(200, 45)
        layout.addWidget(self.pushButton_login, alignment=Qt.AlignCenter)

        # Tombol Logout (Keluar)
        self.pushButton_logout = QPushButton("KELUAR")
        self.pushButton_logout.setFixedSize(200, 45)
        self.pushButton_logout.setStyleSheet("""
            QPushButton {
                background-color: #c62828; /* merah untuk keluar */
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        layout.addWidget(self.pushButton_logout, alignment=Qt.AlignCenter)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Aplikasi Apotek", None))


def menu_awal():
    """Tampilan awal aplikasi menggunakan PyQt"""
    app = QApplication(sys.argv)
    session.clear()

    # Buat window utama
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    # Hubungkan tombol ke fungsi lain
    ui.pushButton_register.clicked.connect(lambda: buka_register(main_window))
    ui.pushButton_login.clicked.connect(lambda: [main_window.hide(), tampil_login()])
    ui.pushButton_logout.clicked.connect(app.quit)

    # Jalankan aplikasi
    app.exec()

    # Setelah ditutup, cek login session
    if session.get("is_login"):
        role = session["dataUser"].get("role", "").lower()

        if role == "admin":
            tampil_admin()
        elif role == "apoteker":
            tampil_apoteker()
        elif role == "kasir":
            tampil_kasir()
        else:
            QMessageBox.information(None, "Info", f"Role '{role}' belum memiliki tampilan GUI.")
    else:
        print("Program ditutup oleh pengguna.")

form_register_window = None  # tambahkan global di luar fungsi

def buka_register(main_window):
    """Buka form register dan sembunyikan menu utama"""
    from frontend.tampilanRegister import FormRegister
    global form_register_window
    main_window.hide()
    form_register_window = FormRegister(menu_awal_window=main_window)
    form_register_window.show()

def main():
    """Fungsi utama menjalankan aplikasi"""
    menu_awal()


if __name__ == "__main__":
    main()
