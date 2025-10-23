import tkinter as tk
from tkinter import ttk, messagebox
from backend.admin import (
    lihatSemuaDataObat,
    tambahObat,
    updateObat,
    hapusObat,
    lihatSemuaTransaksi,
    lihatDetailTransaksi,
    cariObat
)
import re
from datetime import datetime


def tampil_admin():
    root = tk.Tk()
    root.title("Dashboard Admin - Aplikasi Apotek")
    root.geometry("1000x620")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # =========================
    # TAB 1: KELOLA DATA OBAT
    # =========================
    frame_obat = tk.Frame(notebook)
    notebook.add(frame_obat, text="Kelola Data Obat")

    tk.Label(frame_obat, text="Kelola Data Obat", font=("Arial", 16, "bold")).pack(pady=10)

    # --- Search Bar ---
    search_frame = tk.LabelFrame(frame_obat, text="Cari Obat", padx=10, pady=5)
    search_frame.pack(pady=6, padx=20, fill="x")

    tk.Label(search_frame, text="Nama atau ID Obat:").grid(row=0, column=0, sticky="w")
    entry_search = tk.Entry(search_frame, width=40)
    entry_search.grid(row=0, column=1, padx=5)

    def refresh_data_obat():
        entry_search.delete(0, tk.END)
        tabel_obat.delete(*tabel_obat.get_children())
        data = lihatSemuaDataObat()
        if isinstance(data, str):
            messagebox.showinfo("Info", data)
            return
        for d in data:
            tabel_obat.insert("", "end", values=(
                d["obatId"], d["namaObat"], d["jenis"], d["harga"], d["stok"], d["kadaluarsa"]
            ))

    def perform_search_admin():
        keyword = entry_search.get().strip()
        tabel_obat.delete(*tabel_obat.get_children())

        if not keyword:
            data = lihatSemuaDataObat()
            if isinstance(data, str):
                messagebox.showinfo("Info", data)
                return
            for d in data:
                tabel_obat.insert("", "end", values=(
                    d["obatId"], d["namaObat"], d["jenis"], d["harga"], d["stok"], d["kadaluarsa"]
                ))
            return

        hasil = cariObat(keyword)
        if isinstance(hasil, str):
            messagebox.showinfo("Info", hasil)
            return

        for d in hasil:
            tabel_obat.insert("", "end", values=(
                d["obatId"], d["namaObat"], d["jenis"], d["harga"], d["stok"], d["kadaluarsa"]
            ))

    tk.Button(search_frame, text="Cari", width=10, command=perform_search_admin).grid(row=0, column=2, padx=5)
    tk.Button(search_frame, text="Reset", width=10, command=refresh_data_obat).grid(row=0, column=3, padx=5)

    # --- Frame Data ---
    frame_data = tk.Frame(frame_obat)
    frame_data.pack(pady=10, padx=20, fill="both", expand=True)

    columns = ("obatId", "namaObat", "jenis", "harga", "stok", "kadaluarsa")
    tabel_obat = ttk.Treeview(frame_data, columns=columns, show="headings", height=12)

    for col in columns:
        tabel_obat.heading(col, text=col)
        tabel_obat.column(col, width=140)

    tabel_obat.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(frame_data, orient="vertical", command=tabel_obat.yview)
    scrollbar.pack(side="right", fill="y")
    tabel_obat.configure(yscrollcommand=scrollbar.set)

    # --- Fokus otomatis ke search bar setiap kali tab Kelola Obat dipilih ---
    def fokus_search_bar(event=None):
        entry_search.focus_set()

    notebook.bind("<<NotebookTabChanged>>", lambda e: fokus_search_bar() if notebook.index("current") == 0 else None)

    # =========================
    # FORM POPUP TAMBAH / UPDATE
    # =========================
    def form_popup(mode="tambah", data=None):
        popup = tk.Toplevel(root)
        popup.title("Tambah Data Obat" if mode == "tambah" else "Update Data Obat")
        popup.geometry("400x350")
        popup.grab_set()

        tk.Label(
            popup,
            text=("Tambah Obat Baru" if mode == "tambah" else "Update Data Obat"),
            font=("Arial", 12, "bold"),
        ).pack(pady=10)

        form_frame = tk.Frame(popup)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nama Obat").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        nama = tk.Entry(form_frame, width=30)
        nama.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(form_frame, text="Jenis").grid(row=1, column=0, sticky="w", padx=5, pady=3)
        jenis = tk.Entry(form_frame, width=30)
        jenis.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(form_frame, text="Harga").grid(row=2, column=0, sticky="w", padx=5, pady=3)
        harga = tk.Entry(form_frame, width=30)
        harga.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(form_frame, text="Stok").grid(row=3, column=0, sticky="w", padx=5, pady=3)
        stok = tk.Entry(form_frame, width=30)
        stok.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(form_frame, text="Kadaluarsa (dd/mm/yyyy)").grid(row=4, column=0, sticky="w", padx=5, pady=3)
        kadaluarsa = tk.Entry(form_frame, width=30)
        kadaluarsa.grid(row=4, column=1, padx=5, pady=3)

        # Isi data otomatis kalau mode update
        if mode == "update" and data:
            nama.insert(0, data[1])
            jenis.insert(0, data[2])
            harga.insert(0, data[3])
            stok.insert(0, data[4])
            try:
                if "-" in str(data[5]):
                    tanggal = datetime.strptime(str(data[5]), "%Y-%m-%d").strftime("%d/%m/%Y")
                else:
                    tanggal = data[5]
                kadaluarsa.insert(0, tanggal)
            except Exception:
                kadaluarsa.insert(0, data[5])

        def validasi_tanggal(input_str):
            pola = r"^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$"
            if not re.match(pola, input_str):
                return False
            try:
                input_str = input_str.replace("-", "/")
                d, m, y = input_str.split("/")
                d, m, y = int(d), int(m), int(y)
                if not (1 <= m <= 12):
                    return False
                datetime.strptime(input_str, "%d/%m/%Y" if len(str(y)) == 4 else "%d/%m/%y")
                return True
            except ValueError:
                return False

        def simpan():
            n, j, h, s, k = (
                nama.get().strip(),
                jenis.get().strip(),
                harga.get().strip(),
                stok.get().strip(),
                kadaluarsa.get().strip(),
            )

            if not all([n, j, h, s, k]):
                messagebox.showwarning("Peringatan", "Harap isi semua field!", parent=popup)
                return

            if not validasi_tanggal(k):
                messagebox.showwarning(
                    "Peringatan",
                    "Inputkan tanggal kadaluarsa dengan benar (dd/mm/yyyy atau dd-mm-yyyy)!",
                    parent=popup,
                )
                return

            # Ubah ke format MySQL
            k = k.replace("-", "/")
            d, m, y = k.split("/")
            if len(y) == 2:
                y = "20" + y
            try:
                k_mysql = datetime.strptime(f"{d}/{m}/{y}", "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Peringatan", "Tanggal kadaluarsa tidak valid!", parent=popup)
                return

            if mode == "tambah":
                pesan = tambahObat(n, j, h, s, k_mysql)
            else:
                obatId = data[0]
                pesan = updateObat(obatId, n, j, h, s, k_mysql)

            messagebox.showinfo("Info", pesan, parent=popup)
            popup.destroy()
            refresh_data_obat()

        tk.Button(
            popup,
            text=("Tambah" if mode == "tambah" else "Update"),
            width=12,
            bg="#4CAF50",
            fg="white",
            command=simpan,
        ).pack(pady=5)
        tk.Button(popup, text="Batal", width=12, command=popup.destroy).pack()

    # =========================
    # TOMBOL AKSI
    # =========================
    frame_button = tk.Frame(frame_obat)
    frame_button.pack(pady=10)

    tk.Button(frame_button, text="Tambah", command=lambda: form_popup("tambah"), bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
    tk.Button(frame_button, text="Update", command=lambda: [form_popup("update", tabel_obat.item(tabel_obat.selection()[0])["values"]) if tabel_obat.selection() else messagebox.showwarning("Peringatan", "Pilih data obat yang ingin diupdate!")], bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)
    tk.Button(frame_button, text="Hapus", command=lambda: [hapusObat(tabel_obat.item(tabel_obat.selection()[0])["values"][0]) if tabel_obat.selection() else messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")], bg="#f44336", fg="white", width=12).grid(row=0, column=2, padx=5)
    tk.Button(frame_button, text="Refresh", command=refresh_data_obat, width=12).grid(row=0, column=3, padx=5)

    # =========================
    # TAB 2: RIWAYAT TRANSAKSI
    # =========================
    frame_transaksi = tk.Frame(notebook)
    notebook.add(frame_transaksi, text="Riwayat Transaksi")

    tk.Label(frame_transaksi, text="Riwayat Transaksi", font=("Arial", 16, "bold")).pack(pady=10)

    frame_data_trans = tk.Frame(frame_transaksi)
    frame_data_trans.pack(pady=10)

    columns_trans = ("transaksiId", "tanggalTransaksi", "Kasir", "totalHarga")
    tabel_transaksi = ttk.Treeview(frame_data_trans, columns=columns_trans, show="headings", height=10)

    for col in columns_trans:
        tabel_transaksi.heading(col, text=col)
        tabel_transaksi.column(col, width=150)

    tabel_transaksi.pack(side="left")
    scrollbar2 = ttk.Scrollbar(frame_data_trans, orient="vertical", command=tabel_transaksi.yview)
    scrollbar2.pack(side="right", fill="y")
    tabel_transaksi.configure(yscrollcommand=scrollbar2.set)

    def refresh_transaksi():
        tabel_transaksi.delete(*tabel_transaksi.get_children())
        data = lihatSemuaTransaksi()
        if isinstance(data, str):
            messagebox.showinfo("Info", data)
            return
        for d in data:
            tabel_transaksi.insert("", "end", values=(d["transaksiId"], d["tanggalTransaksi"], d["Kasir"], d["totalHarga"]))

    def lihat_detail_transaksi():
        selected = tabel_transaksi.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih transaksi untuk melihat detail!")
            return
        transaksiId = tabel_transaksi.item(selected[0])["values"][0]
        dataDetail = lihatDetailTransaksi(transaksiId)
        if isinstance(dataDetail, str):
            messagebox.showinfo("Info", dataDetail)
            return

        detail_window = tk.Toplevel(root)
        detail_window.title(f"Detail Transaksi {transaksiId}")
        detail_window.geometry("500x300")

        columns_detail = ("detailId", "namaObat", "jumlah", "subtotal")
        tabel_detail = ttk.Treeview(detail_window, columns=columns_detail, show="headings")
        for col in columns_detail:
            tabel_detail.heading(col, text=col)
            tabel_detail.column(col, width=100)
        tabel_detail.pack(fill="both", expand=True, padx=10, pady=10)

        for d in dataDetail:
            tabel_detail.insert("", "end", values=(d["detailId"], d["namaObat"], d["jumlah"], d["subtotal"]))

    frame_btn_trans = tk.Frame(frame_transaksi)
    frame_btn_trans.pack(pady=10)
    tk.Button(frame_btn_trans, text="Refresh Data", command=refresh_transaksi, width=15).grid(row=0, column=0, padx=5)
    tk.Button(frame_btn_trans, text="Lihat Detail", command=lihat_detail_transaksi, width=15).grid(row=0, column=1, padx=5)

    def kembali_ke_menu():
        root.destroy()
        from main import menu_awal
        menu_awal()

    tk.Button(root, text="Keluar", command=kembali_ke_menu, width=15).pack(pady=10)

      # Load data awal
    refresh_data_obat()
    refresh_transaksi()

    # --- Fokus otomatis ke search bar ---
    def fokus_awal(*args):
        entry_search.focus_force()

    # Panggil saat frame kelihatan di layar
    frame_obat.bind("<Visibility>", fokus_awal)

    root.mainloop()

if __name__ == "__main__":
    tampil_admin()