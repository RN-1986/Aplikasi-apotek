from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget, QMessageBox)
from backend.login import login, session
from backend.logout import logout as backend_logout
from frontend.dashboardAdmin import DashboardAdmin
from PySide6.QtWidgets import QMainWindow, QPushButton
from frontend.tampilanRegister_lama import tampil_register


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
"height: 5px;\n"
"text-align: center;      \n"
"line-height: 20px;  \n"
"border: 2px solid white;   ")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(14)
        self.label.setIndent(13)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 140, 411, 221))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
" border: 2px solid white;   \n"
"border-radius: 10px;   ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(224, 390, 141, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;\n"
"border-width: 1px;            \n"
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
"border-radius: 5px;\n"
"border-width: 1px;            \n"
"border-style: solid;       \n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 390, 75, 41))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-width: 1px;            \n"
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
        self.lineEdit.setStyleSheet(u"border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 280, 211, 51))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"border-radius: 8px;\n"
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
        MainWindow.setFixedSize(MainWindow.size())


        # simpan referensi window supaya bisa ditutup oleh proses_login
        self.login_window = MainWindow

        # koneksikan tombol Login / Register / Logout tanpa try/except
        if hasattr(self, "pushButton"):
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(lambda: self.proses_login(MainWindow))

        if hasattr(self, "lineEdit"):
            self.lineEdit.returnPressed.connect(lambda: self.proses_login(MainWindow))

        if hasattr(self, "lineEdit_2"):
            self.lineEdit_2.returnPressed.connect(lambda: self.proses_login(MainWindow))

        if hasattr(self, "pushButton_2"):
            # tombol Register
            self.pushButton_2.clicked.connect(lambda: self.action_register(MainWindow))

        if hasattr(self, "pushButton_3"):
            # tombol Logout
            self.pushButton_3.clicked.connect(lambda: self.action_logout(MainWindow))

        # set state awal tombol berdasarkan session
        self.update_button_states()
        self.lineEdit.setStyleSheet("""background-color: white; border-radius: 20px; padding-left: 15px;""")
        self.lineEdit_2.setStyleSheet("""background-color: white; border-radius: 20px; padding-left: 15px;""")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label.setText("⚕️ Selamat Datang di Aplikasi Apotek ⚕️")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
    # retranslateUi
    # ======================================================
    #  FUNGSI LOGIN - harus jadi method class
    # ======================================================
    def proses_login(self, MainWindow):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username or not password:
            QMessageBox.warning(MainWindow, "Peringatan", "Username dan password harus diisi!")
            return

        pesan = login(username, password)

        if session.get('is_login'):
            QMessageBox.information(MainWindow, "Login Berhasil", pesan)
            role = session.get('role')

            if role == "admin":
                # buka dashboard admin (kelas DashboardAdmin)
                self.window = DashboardAdmin()
                self.window.show()
                # tutup window login
                if hasattr(self, "login_window") and self.login_window:
                    self.login_window.close()
            else:
                QMessageBox.warning(MainWindow, "Role belum tersedia", f"Role '{role}' belum didukung.")
        else:
            QMessageBox.critical(MainWindow, "Login Gagal", pesan)

    def update_button_states(self):
        """
        Atur enabled/disabled untuk tiga tombol:
        - sebelum login: Login & Register aktif, Logout non-aktif
        - sesudah login : Login & Register non-aktif, Logout aktif
        """
        logged = bool(session.get('is_login'))
        if hasattr(self, "pushButton"):
            self.pushButton.setEnabled(not logged)
        if hasattr(self, "pushButton_2"):
            self.pushButton_2.setEnabled(not logged)
        if hasattr(self, "pushButton_3"):
            self.pushButton_3.setEnabled(not logged)

    def action_register(self, MainWindow):
        self.reg_window = tampil_register(MainWindow)   # <<< kirim referensi window login
        MainWindow.close()


    def action_logout(self, MainWindow):
        # panggil backend untuk membersihkan session
        pesan = backend_logout()
        QMessageBox.information(MainWindow, "Logout", pesan)

        # tutup window yang dipassing (mis. window login atau dashboard)
        MainWindow.close()

        # pastikan aplikasi berhenti jika tidak ada window tersisa
        QApplication.quit()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        session['is_login'] = False  # pastikan reset
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())