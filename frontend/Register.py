from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QVBoxLayout, QFormLayout,QHBoxLayout)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from backend.register import register
from frontend.tampilanLogin import tampil_login


class FormRegister(QMainWindow):
    def __init__(self, menu_awal_window=None):
        super().__init__()
        self.menu_awal_window = menu_awal_window
        self.setWindowTitle("Form Register - Aplikasi Apotek")
        self.resize(500, 430)
        self.center_window()

        # 🌿 Background gradasi hijau lembut
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor("#d4f8e8"))
        gradient.setColorAt(1.0, QColor("#ffffff"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # Layout utama
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(100, 40, 100, 40)
        main_layout.setSpacing(20)

        # Judul
        title = QLabel("💊  FORM REGISTER  💊")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Form layout
        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignCenter)
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setHorizontalSpacing(20)
        form_layout.setVerticalSpacing(15)

        font_label = QFont("Segoe UI", 10)
        font_input = QFont("Segoe UI", 10)

        # Input field
        self.input_nama = QLineEdit()
        self.input_username = QLineEdit()
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_konfirmasi = QLineEdit()
        self.input_konfirmasi.setEchoMode(QLineEdit.Password)
        self.combo_role = QComboBox()
        self.combo_role.addItems(["Pilih role", "Admin", "Apoteker", "Kasir"])

        for inp in [
            self.input_nama, self.input_username,
            self.input_password, self.input_konfirmasi
        ]:
            inp.setFixedHeight(30)
            inp.setFont(font_input)
            inp.setStyleSheet("""
                QLineEdit {
                    background-color: white;
                    border: 2px solid #81c784;
                    border-radius: 6px;
                    padding: 4px 6px;
                }
                QLineEdit:focus {
                    border: 2px solid #43a047;
                }
            """)

        self.combo_role.setFixedHeight(30)
        self.combo_role.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #81c784;
                border-radius: 6px;
                padding: 4px;
            }
            QComboBox:focus {
                border: 2px solid #43a047;
            }
        """)

        # Tambahkan field ke layout form
        form_layout.addRow(QLabel("Nama Lengkap:", font=font_label), self.input_nama)
        form_layout.addRow(QLabel("Username:", font=font_label), self.input_username)
        form_layout.addRow(QLabel("Password:", font=font_label), self.input_password)
        form_layout.addRow(QLabel("Konfirmasi Password:", font=font_label), self.input_konfirmasi)
        form_layout.addRow(QLabel("Role:", font=font_label), self.combo_role)

        main_layout.addLayout(form_layout)

        # Tombol Register dan Kembali sejajar
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)
        btn_layout.setSpacing(20)

        btn_register = QPushButton("Register")
        btn_register.setFixedSize(120, 35)
        btn_register.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11pt;
            }
            QPushButton:hover { background-color: #43a047; }
            QPushButton:pressed { background-color: #2e7d32; }
        """)

        btn_back = QPushButton("↩ Kembali")
        btn_back.setFixedSize(120, 35)
        btn_back.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11pt;
            }
            QPushButton:hover { background-color: #e0e0e0; }
        """)

        btn_register.clicked.connect(self.aksi_register)
        btn_back.clicked.connect(self.kembali_ke_menu)

        btn_layout.addWidget(btn_register)
        btn_layout.addWidget(btn_back)
        main_layout.addLayout(btn_layout)

        # Set layout ke central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def aksi_register(self):
        nama = self.input_nama.text().strip()
        username = self.input_username.text().strip()
        password = self.input_password.text()
        konfirmasi = self.input_konfirmasi.text()
        role = self.combo_role.currentText()

        if not nama or not username or not password or not konfirmasi or role == "Pilih role":
            QMessageBox.warning(self, "Peringatan", "Semua kolom wajib diisi!")
            return
        if password != konfirmasi:
            QMessageBox.critical(self, "Error", "Password dan konfirmasi tidak cocok!")
            return

        hasil = register(nama, username, password, role)
        QMessageBox.information(self, "Informasi", hasil)

        if "berhasil" in hasil.lower():
            self.close()
            tampil_login() 

    def kembali_ke_menu(self):
        """Kembali ke menu awal"""
        self.close()
        if self.menu_awal_window:
            self.menu_awal_window.show()


    def center_window(self):
        """Agar jendela muncul di tengah layar"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

def tampil_register(menu_awal_window=None):
    window = FormRegister(menu_awal_window)
    window.show()
    return window  # penting supaya tidak hilang dari memori

# Jalankan langsung (untuk testing mandiri)
if __name__ == "__main__":
    app = QApplication([])
    win = FormRegister()
    win.show()
    app.exec()