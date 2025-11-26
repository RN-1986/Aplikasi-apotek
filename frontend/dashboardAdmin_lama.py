from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QWidget, QMessageBox)
from backend.admin import (
    lihatSemuaDataObat, tambahObat, updateObat, hapusObat,
    lihatSemuaTransaksi, lihatDetailTransaksi, cariObat,
    ambilDataObatYangAkanDiUpdate
)
# tambahkan import UI windows lain + wrapper window classes
from frontend.tambahObat_lama import Ui_MainWindow as Ui_TambahObat, TambahObatWindow
from frontend.editObat_lama import Ui_MainWindow as Ui_EditObat, EditObatWindow
from frontend.hapusObat_lama import Ui_MainWindow as Ui_HapusObat, HapusObatWindow
from frontend.adminRiwayatTransaksi import Ui_MainWindow as Ui_Riwayat
from frontend.adminRiwayatTransaksi import RiwayatWindow
from frontend.detailRiwayatTransaksi_lama import Ui_MainWindow as Ui_Detail
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 608)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 40, 41, 31))
        self.label_4.setStyleSheet(u"image: url(:/Icons/medication.png);\n"
"border-radius: 15px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 530, 31, 31))
        self.label_6.setStyleSheet(u"image: url(:/logoKasir/circle-user.png);\n"
"border-radius: 15px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 230, 41, 41))
        self.label.setStyleSheet(u"image: url(:/logo-admin/money-check-edit.png);\n"
"\n"
"background-color: rgb(125, 202, 211);\n"
"border-radius: 5px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 10, 661, 501))
        self.frame.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(187, 255, 253);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 561, 81))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border radius: 30px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 71, 20))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(125, 202, 211);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 40, 261, 41))
        self.lineEdit.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(125, 202, 211);")
        self.pushButton_search = QPushButton(self.frame)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(420, 45, 70, 30))
        self.pushButton_search.setStyleSheet("""
    QPushButton {
        border-radius: 8px;
        background-color: rgb(230, 255, 255);
        font-size: 12px; 
        font-weight: bold;
        padding: 4px 8px;
    }
""")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(480, 40, 71, 41))
        self.pushButton_4.setStyleSheet("""
    QPushButton {
        border-radius: 8px;
        background-color: rgb(125, 202, 211);
        font-size: 14px;       /* perbesar tulisan */
        font-weight: bold;     /* biar rapi */
        padding: 6px 12px;     /* biar proporsional */
    }
""")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 150, 561, 331))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(112)
        self.pushButton_tambah = QPushButton(self.frame)
        self.pushButton_tambah.setObjectName(u"pushButton_tambah")
        self.pushButton_tambah.setGeometry(QRect(40, 110, 91, 31))
        self.pushButton_tambah.setStyleSheet("""
    QPushButton {
        border-radius: 10px;
        background-color: rgb(49, 245, 46);
        font-size: 14px;  
        font-weight: bold;
        padding: 6px 12px;
    }
""")
        self.pushButton_edit = QPushButton(self.frame)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(140, 110, 91, 31))
        self.pushButton_edit.setStyleSheet("""
    QPushButton {
        border-radius: 10px;
        background-color: rgb(255, 216, 23);
        font-size: 14px;
        font-weight: bold;
        padding: 6px 12px;
    }
""")
        self.pushButton_delete = QPushButton(self.frame)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(240, 110, 91, 31))
        self.pushButton_delete.setStyleSheet("""
    QPushButton {
        border-radius: 10px;
        background-color: rgb(255, 0, 0);
        color: white;
        font-size: 14px;
        font-weight: bold;
        padding: 6px 12px;
    }
""")
        self.pushButton_kelolaObat = QPushButton(self.centralwidget)
        self.pushButton_kelolaObat.setObjectName(u"pushButton_kelolaObat")
        self.pushButton_kelolaObat.setGeometry(QRect(70, 170, 161, 41))
        self.pushButton_kelolaObat.setFont(font)
        self.pushButton_kelolaObat.setStyleSheet(u"""
            QPushButton {
                background-color: rgb(187, 255, 253);
                border-radius: 10px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: rgb(160, 230, 228);
            }
            QPushButton:pressed {
                background-color: rgb(120, 200, 198);
            }
        """)
        self.pushButton_riwayatTransaksi = QPushButton(self.centralwidget)
        self.pushButton_riwayatTransaksi.setObjectName(u"pushButton_riwayatTransaksi")
        self.pushButton_riwayatTransaksi.setGeometry(QRect(70, 230, 161, 41))
        self.pushButton_riwayatTransaksi.setFont(font)
        self.pushButton_riwayatTransaksi.setStyleSheet(u"""
            QPushButton {
                background-color: rgb(187, 255, 253);
                border-radius: 10px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: rgb(160, 230, 228);
            }
            QPushButton:pressed {
                background-color: rgb(120, 200, 198);
            }
        """)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 520, 131, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 41, 41))
        font3 = QFont()
        font3.setPointSize(6)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(125, 202, 211);\n"
"image: url(:/logo-admin/admin-alt.png);\n"
"border-radius: 5px;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 20, 191, 61))
        self.textBrowser.setStyleSheet(u"background-color: rgb(187, 255, 253);\n"
"border-radius: 30px;")
        self.pushButton_keluar = QPushButton(self.centralwidget)
        self.pushButton_keluar.setObjectName(u"pushButton_keluar")
        self.pushButton_keluar.setGeometry(QRect(770, 530, 151, 31))
        self.pushButton_keluar.setFont(font2)
        self.pushButton_keluar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-color: 1px rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 520, 41, 41))
        self.label_7.setStyleSheet(u"image: url(:/logo-admin/circle-user.png);\n"
"border-radius: 15px;")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        MainWindow.setFixedSize(MainWindow.size())
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        # buat stub sederhana supaya setupUi tidak error bila file UI terpotong.
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard Admin", None))
        try:
            self.label_2.setText(QCoreApplication.translate("MainWindow", u"Daftar Obat", None))
        except Exception:
            pass
        try:
            self.label.setText(QCoreApplication.translate("MainWindow", u"📊", None))
            font_emoji2 = QFont()
            font_emoji2.setPointSize(25)  # perbesar emoji
            self.label.setFont(font_emoji2)
        except Exception:
            pass
        try:
            self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cari Obat", None))
        except Exception:
            pass
        try:
            self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        except Exception:
            pass
        try:
            self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        except Exception:
            pass
        try:
            self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        except Exception:
            pass
        try:
            self.pushButton_tambah.setText(QCoreApplication.translate("MainWindow", u"Tambah", None))
        except Exception:
            pass
        try:
            self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        except Exception:
            pass
        try:
            self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        except Exception:
            pass
        try:
            self.pushButton_kelolaObat.setText(QCoreApplication.translate("MainWindow", u"Kelola Obat", None))
        except Exception:
            pass
        try:
            self.pushButton_riwayatTransaksi.setText(QCoreApplication.translate("MainWindow", u"Riwayat Transaksi", None))
        except Exception:
            pass
        try:
            self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        except Exception:
            pass
        try:
            self.pushButton_keluar.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        except Exception:
            pass
        try:
            self.label_5.setText(QCoreApplication.translate("MainWindow", u"💊", None))
            font_emoji3 = QFont()
            font_emoji3.setPointSize(25)  # perbesar emoji
            self.label_5.setFont(font_emoji3)
        except Exception:
            pass
        try:
            self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<div style='text-align:center; font-size:18px; font-weight:bold;'>Dashboard Admin</div>", None))
        except Exception:
            pass
        try:
            self.label_7.setText(QCoreApplication.translate("MainWindow", u"👤", None))
            font_emoji1 = QFont()
            font_emoji1.setPointSize(25)  # perbesar emoji
            self.label_7.setFont(font_emoji1)
        except Exception:
            pass
        try:
            self.label_8.setText(QCoreApplication.translate("MainWindow", u"", None))
        except Exception:
            pass
    # retranslateUi

class DashboardAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ===== fix: tombol warna sesuai fungsi + search emoji posision =====
        try:
            # mapping warna per tombol (sesuaikan nama widget jika berbeda)
            button_map = {
                "pushButton_tambah":  {"bg":"#36D14A","hover":"#2FBF3F","pressed":"#219224","color":"#000"},
                "pushButton_edit":    {"bg":"#FFD54D","hover":"#FFCC33","pressed":"#E6B800","color":"#000"},
                "pushButton_delete":  {"bg":"#FF4D4D","hover":"#E04343","pressed":"#C73A3A","color":"#fff"},
                "pushButton_4":       {"bg":"#7FE6E6","hover":"#66DADA","pressed":"#4BCBCB","color":"#000"}, # refresh
                "pushButton_search":  {"bg":"#E6FFFF","hover":"#D6FFFF","pressed":"#C6FFFF","color":"#000"},
                "pushButton_keluar":  {"bg":"#FF2B2B","hover":"#E02424","pressed":"#C71D1D","color":"#fff"}
            }

            for name, colors in button_map.items():
                if hasattr(self.ui, name):
                    btn = getattr(self.ui, name)
                    # set teks/emoji khusus untuk search (emoji di kanan)
                    if name == "pushButton_search":
                        # letakkan emoji di kanan sedikit: "Cari"
                        try:
                            btn.setText("Cari")
                        except Exception:
                            pass
                    # apply per-button stylesheet (preserve color)
                    style = f"""
                        QPushButton {{
                            background-color: {colors['bg']};
                            color: {colors['color']};
                            border: none;
                            border-radius: 8px;
                            padding: 8px 16px;
                            font-size: 10px;
                            margin-left: 20px;
                        }}
                        QPushButton:hover {{
                            background-color: {colors['hover']};
                        }}
                        QPushButton:pressed {{
                            background-color: {colors['pressed']};
                        }}
                    """
                    btn.setStyleSheet(style)
        except Exception:
            pass

        # ===== fix: hapus background putih pada label-welcome jika ada =====
        try:
            # cari semua QLabel di ui dan bersihkan background bila ada putih
            from PySide6.QtWidgets import QLabel
            for attr in vars(self.ui).values():
                if isinstance(attr, QLabel):
                    ss = attr.styleSheet() or ""
                    # jika di stylesheet ada background-color putih atau fill putih, set jadi transparent
                    if "background-color: rgb(255, 255, 255)" in ss or "background-color: #ffffff" in ss.lower():
                        attr.setStyleSheet("background: transparent; color: #000;")
                    # jika label menampilkan teks "Selamat" dan masih ada kotak, buat transparan juga
                    try:
                        if "selamat" in (attr.text() or "").lower():
                            attr.setStyleSheet("background: transparent; color: #000;")
                    except Exception:
                        pass
        except Exception:
            pass

        # pastikan tableWidget ada dan konfigurasi header terlihat
        try:
            # pastikan jumlah kolom sesuai (sesuaikan jumlah kolom UI)
            self.ui.tableWidget.setColumnCount(5)
            # set label header (sesuaikan teks sesuai UI)
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID Obat", "Jenis", "Harga", "Nama Obat", "Kadaluarsa"])

            # pastikan header terlihat dan memiliki tinggi minimum
            header = self.ui.tableWidget.horizontalHeader()
            header.setVisible(True)
            header.setMinimumHeight(28)              # atur tinggi header jika terlalu kecil
            header.setStretchLastSection(False)
            header.setSectionResizeMode(0, header.Stretch)   # contoh: kolom 0 stretch
            header.setSectionResizeMode(1, header.ResizeToContents)
            header.setSectionResizeMode(2, header.ResizeToContents)
            header.setSectionResizeMode(3, header.ResizeToContents)
            header.setSectionResizeMode(4, header.ResizeToContents)

            # override stylesheet header kalau ada style yang menyembunyikan teks/bg
            self.ui.tableWidget.setStyleSheet("""
                QHeaderView::section {
                    background-color: #E6FFFF;
                    color: #000000;
                    padding: 4px;
                    border: 1px solid #d9d9d9;
                }
            """)
        except Exception:
            pass

        # contoh koneksi tombol jika ada (gunakan nama widget yang valid)
        try:
            if hasattr(self.ui, "pushButton_keluar"):
                self.ui.pushButton_keluar.clicked.connect(self.logout_to_login)
        except Exception:
            pass

        # Tombol Tambah / Edit / Delete / Refresh / Search / Riwayat
        self.ui.pushButton_tambah.clicked.connect(self.open_tambah)
        self.ui.pushButton_edit.clicked.connect(self.open_edit)
        self.ui.pushButton_delete.clicked.connect(self.open_hapus)
        self.ui.pushButton_4.clicked.connect(self.refresh_data_obat)
        self.ui.pushButton_keluar.clicked.connect(self.logout_to_login)

        # search
        try:
            self.ui.pushButton_search.clicked.connect(self.action_search)
        except Exception:
            pass
        # riwayat page
        try:
            self.ui.pushButton_riwayatTransaksi.clicked.connect(self.open_riwayat)
        except Exception:
            pass

        # double click item => edit
        try:
            self.ui.tableWidget.itemDoubleClicked.connect(self.open_edit_from_item)
        except Exception:
            pass

        # tambahkan emoji 🔍 di samping tombol search (jika ada)
        try:
            if hasattr(self.ui, "pushButton_search"):
                # pilih salah satu: hanya emoji, atau emoji + teks
                self.ui.pushButton_search.setText("Cari")
                # atau: self.ui.pushButton_search.setText("🔍 Cari")
        except Exception:
            pass

        # Load awal
        self.refresh_data_obat()

    def keluar(self):
        self.close()

    def refresh_data_obat(self):
        self.ui.tableWidget.setRowCount(0)
        data = lihatSemuaDataObat()
        if isinstance(data, str):
            QMessageBox.information(self, "Info", data)
            return

        for row_data in data:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            # dukung hasil dict atau tuple/list
            if isinstance(row_data, dict):
                obatId = row_data.get("obatId") or row_data.get("id") or ""
                jenis = row_data.get("jenis") or ""
                harga = row_data.get("harga") or ""
                hargaObat = row_data.get("hargaObat") or row_data.get("namaObat") or ""
                kadaluarsa = row_data.get("kadaluarsa") or ""
            else:
                # asumsi tuple: (obatId, namaObat, jenis, harga, stok, kadaluarsa)
                obatId = row_data[0] if len(row_data) > 0 else ""
                hargaObat = row_data[1] if len(row_data) > 1 else ""
                jenis = row_data[2] if len(row_data) > 2 else ""
                harga = row_data[3] if len(row_data) > 3 else ""
                kadaluarsa = row_data[5] if len(row_data) > 5 else ""

            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(obatId)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(jenis)))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(harga)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(hargaObat)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(kadaluarsa)))

    def tambah_data(self):
        QMessageBox.information(self, "Info", "Tambah data diklik")

    def edit_data(self):
        selected = self.ui.tableWidget.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return
        QMessageBox.information(self, "Info", f"Edit data {selected[0].text()}")

    def hapus_data(self):
        selected = self.ui.tableWidget.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return
        obatId = selected[0].text()
        pesan = hapusObat(obatId)
        QMessageBox.information(self, "Info", pesan)
        self.refresh_data_obat()

    # --------------------
    # Window: Tambah Obat
    # --------------------
    def open_tambah(self):
        self._tambah_win = TambahObatWindow(parent=self)
        self._tambah_win.show()

    def save_tambah(self):
        ui = self._tambah_ui
        nama = ui.lineEdit.text().strip()
        jenis = ui.lineEdit_2.text().strip()
        harga = ui.lineEdit_3.text().strip()
        stok = ui.lineEdit_4.text().strip()
        kadaluarsa = ui.lineEdit_6.text().strip()
        if not nama:
            QMessageBox.warning(self, "Peringatan", "Nama obat harus diisi")
            return
        pesan = tambahObat(nama, jenis, harga, stok, kadaluarsa)
        QMessageBox.information(self, "Info", pesan)
        self._tambah_win.close()
        self.refresh_data_obat()

    # --------------------
    # Window: Edit Obat
    # --------------------
    def open_edit(self):
        selected = self.ui.tableWidget.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih baris terlebih dulu")
            return
        obatId = selected[0].text()
        self._edit_win = EditObatWindow(obatId, parent=self)
        self._edit_win.show()

    def open_edit_from_item(self, item):
        # double-click handler opens EditObatWindow
        row = item.row()
        id_item = self.ui.tableWidget.item(row, 0).text()
        self._edit_win = EditObatWindow(id_item, parent=self)
        self._edit_win.show()

    def save_edit(self, obatId):
        # tetap ada untuk kompatibilitas jika ada code lain yg memanggilnya
        pass

    # --------------------
    # Window: Hapus Obat
    # --------------------
    def open_hapus(self):
        selected = self.ui.tableWidget.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Peringatan", "Pilih baris terlebih dulu")
            return
        obatId = selected[0].text()
        self._hapus_win = HapusObatWindow(obatId, parent=self)
        # jika UI hapus memiliki field nama, coba isi
        try:
            if hasattr(self._hapus_win.ui, "lineEdit"):
                try:
                    self._hapus_win.ui.lineEdit.setText(selected[1].text())
                except Exception:
                    pass
        except Exception:
            pass
        self._hapus_win.show()

    def confirm_hapus(self, obatId):
        pesan = hapusObat(obatId)
        QMessageBox.information(self, "Info", pesan)
        self._hapus_win.close()
        self.refresh_data_obat()

    # --------------------
    # Search / Refresh
    # --------------------
    def action_search(self):
        keyword = self.ui.lineEdit.text().strip()
        if not keyword:
            self.refresh_data_obat()
            return
        hasil = cariObat(keyword)
        if isinstance(hasil, str):
            QMessageBox.information(self, "Info", hasil)
            return
        # tampilkan hasil
        self.ui.tableWidget.setRowCount(0)
        for row_data in hasil:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            if isinstance(row_data, dict):
                obatId = row_data.get("obatId", "")
                nama = row_data.get("namaObat", "")
                jenis = row_data.get("jenis", "")
                harga = row_data.get("harga", "")
                kadaluarsa = row_data.get("kadaluarsa", "")
            else:
                obatId = row_data[0]
                nama = row_data[1]
                jenis = row_data[2]
                harga = row_data[3]
                kadaluarsa = row_data[5] if len(row_data) > 5 else ""
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(obatId)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(jenis)))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(harga)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(nama)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(kadaluarsa)))

    # --------------------
    # Riwayat Transaksi
    # --------------------
    def open_riwayat(self):
        # sembunyikan dashboard, buka window riwayat sebagai window terpisah
        try:
            self.hide()
        except Exception:
            pass

        self._riwayat_win = QMainWindow()
        self._riwayat_ui = Ui_Riwayat()
        self._riwayat_ui.setupUi(self._riwayat_win)

        # koneksikan tombol riwayat -> panggil fungsi yang sesuai
        try:
            if hasattr(self._riwayat_ui, "pushButton_semuTransaksi"):
                self._riwayat_ui.pushButton_semuTransaksi.clicked.connect(lambda: self.load_semua_transaksi(self._riwayat_ui))
            if hasattr(self._riwayat_ui, "pushButton_detailriwayatTransaksi"):
                self._riwayat_ui.pushButton_detailriwayatTransaksi.clicked.connect(lambda: self.open_detail_riwayat_from_selection(self._riwayat_ui))
            if hasattr(self._riwayat_ui, "tableWidget_2"):
                self._riwayat_ui.tableWidget_2.itemDoubleClicked.connect(lambda item: self.open_detail_riwayat_from_item(self._riwayat_ui, item))

            # tombol "Kelola Data" di riwayat -> kembali ke dashboard (tutup riwayat, show dashboard)
            if hasattr(self._riwayat_ui, "pushButton_kelolaData"):
                def back_to_dashboard():
                    try:
                        self._riwayat_win.close()
                    except Exception:
                        pass
                    try:
                        self.show()
                    except Exception:
                        pass
                self._riwayat_ui.pushButton_kelolaData.clicked.connect(back_to_dashboard)

            # tombol "Kembali" di riwayat -> kembali ke dashboard admin
            if hasattr(self._riwayat_ui, "pushButton_keluar"):
                
                # ubah teks tombol: Keluar -> Kembali
                self._riwayat_ui.pushButton_keluar.setText("Kembali")

                def kembali_ke_dashboard_riwayat():
                    try:
                        self._riwayat_win.close()   # tutup jendela riwayat
                    except Exception:
                        pass
                    try:
                        self.show()                # tampilkan dashboard admin
                    except Exception:
                        pass

                self._riwayat_ui.pushButton_keluar.clicked.connect(kembali_ke_dashboard_riwayat)
        except Exception:
            pass
        
        # tampilkan dan load data awal
        self._riwayat_win.show()
        try:
            self.load_semua_transaksi(self._riwayat_ui)
        except Exception:
            pass

    def load_semua_transaksi(self, ui):
        data = lihatSemuaTransaksi()
        if isinstance(data, str):
            QMessageBox.information(self, "Info", data)
            return
        ui.tableWidget_2.setRowCount(0)
        for row_data in data:
            row = ui.tableWidget_2.rowCount()
            ui.tableWidget_2.insertRow(row)
            # dukung dict atau tuple/list
            if isinstance(row_data, dict):
                tid = row_data.get('transaksiId') or row_data.get('transaksi_id') or ''
                tanggal = row_data.get('tanggalTransaksi') or row_data.get('tanggal_transaksi') or row_data.get('tanggal') or ''
                kasir = row_data.get('Kasir') or row_data.get('kasir') or row_data.get('username') or ''
                total = row_data.get('totalHarga') or row_data.get('total_harga') or row_data.get('total') or ''
            else:
                # asumsi tuple: (transaksiId, tanggalTransaksi, Kasir, totalHarga)
                try:
                    tid = row_data[0]
                    tanggal = row_data[1]
                    kasir = row_data[2]
                    total = row_data[3]
                except Exception:
                    tid = tanggal = kasir = total = ''
            ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(tid)))
            ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(tanggal)))
            ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(kasir)))
            ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(total)))

    def open_detail_riwayat_from_selection(self, ui):
        sel = ui.tableWidget_2.selectedItems()
        if not sel:
            QMessageBox.warning(self, "Peringatan", "Pilih transaksi dulu")
            return
        transaksiId = sel[0].text()
        self.open_detail_riwayat(transaksiId)

    def open_detail_riwayat_from_item(self, ui, item):
        row = item.row()
        transaksiId = ui.tableWidget_2.item(row, 0).text()
        self.open_detail_riwayat(transaksiId)

    def open_detail_riwayat(self, transaksiId):
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout

        data = lihatDetailTransaksi(transaksiId)
        if isinstance(data, str):
            QMessageBox.information(self, "Info", data)
            return

        # modal dialog mirip Toplevel di tkinter
        dlg = QDialog(self)
        dlg.setWindowTitle(f"Detail Transaksi {transaksiId}")
        dlg.resize(520, 360)
        layout = QVBoxLayout(dlg)

        # table detail
        tbl = QTableWidget(dlg)
        tbl.setColumnCount(4)
        tbl.setHorizontalHeaderLabels(["detailId", "Nama Obat", "Jumlah", "Subtotal"])
        tbl.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        tbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        tbl.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        tbl.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

        # isi baris
        tbl.setRowCount(0)
        for d in data:
            r = tbl.rowCount()
            tbl.insertRow(r)
            if isinstance(d, dict):
                tbl.setItem(r, 0, QTableWidgetItem(str(d.get("detailId") or d.get("detail_id") or "")))
                tbl.setItem(r, 1, QTableWidgetItem(str(d.get("namaObat") or d.get("nama") or "")))
                tbl.setItem(r, 2, QTableWidgetItem(str(d.get("jumlah") or d.get("qty") or "")))
                tbl.setItem(r, 3, QTableWidgetItem(str(d.get("subtotal") or "")))
            else:
                try:
                    tbl.setItem(r, 0, QTableWidgetItem(str(d[0])))
                    tbl.setItem(r, 1, QTableWidgetItem(str(d[1])))
                    tbl.setItem(r, 2, QTableWidgetItem(str(d[2])))
                    tbl.setItem(r, 3, QTableWidgetItem(str(d[3])))
                except Exception:
                    tbl.setItem(r, 0, QTableWidgetItem(str(d)))

        layout.addWidget(tbl)

        # tombol tutup
        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)
        close_btn = QPushButton("Tutup", dlg)
        close_btn.clicked.connect(dlg.accept)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)

        # jika ingin menyembunyikan dashboard saat dialog terbuka:
        try:
            self.hide()
            dlg.exec()
        finally:
            # pastikan dashboard muncul kembali
            try:
                self.show()
            except Exception:
                pass
    def logout_to_login(self):
        from backend.logout import logout
        logout()  # reset session

        from Login_lama import LoginWindow
        self.login_win = LoginWindow()
        self.login_win.show()

        self.close()
                    # tutup dashboard admin


def open_riwayat(self):
    self._riwayat_win = RiwayatWindow(parent=self)
    self.hide()
    self._riwayat_win.show()


