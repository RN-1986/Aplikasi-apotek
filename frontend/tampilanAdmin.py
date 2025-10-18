# frontend/tampilanAdmin.py
import tkinter as tk
from tkinter import ttk, messagebox
from backend.admin import (
    lihatSemuaDataObat,
    tambahObat,
    updateObat,
    hapusObat,
    lihatSemuaTransaksi,
    lihatDetailTransaksi
)

def tampil_admin():
    root = tk.Tk()
    root.title("Dashboard Admin - Aplikasi Apotek")
    root.geometry("950x600")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # =========================
    # TAB 1: KELOLA DATA OBAT
    # =========================
    frame_obat = tk.Frame(notebook)
    notebook.add(frame_obat, text="Kelola Data Obat")

    tk.Label(frame_obat, text="Kelola Data Obat", font=("Arial", 16, "bold")).pack(pady=10)

    # --- Frame Data ---
    frame_data = tk.Frame(frame_obat)
    frame_data.pack(pady=10)

    columns = ("obatId", "namaObat", "jenis", "harga", "stok", "kadaluarsa")
    tabel_obat = ttk.Treeview(frame_data, columns=columns, show="headings", height=10)

    for col in columns:
        tabel_obat.heading(col, text=col)
        tabel_obat.column(col, width=120)

    tabel_obat.pack(side="left")
    scrollbar = ttk.Scrollbar(frame_data, orient="vertical", command=tabel_obat.yview)
    scrollbar.pack(side="right", fill="y")
    tabel_obat.configure(yscrollcommand=scrollbar.set)

    # --- Frame Input ---
    frame_input = tk.LabelFrame(frame_obat, text="Form Obat", padx=10, pady=10)
    frame_input.pack(fill="x", padx=20, pady=10)

    tk.Label(frame_input, text="Nama Obat").grid(row=0, column=0, sticky="w")
    entry_nama = tk.Entry(frame_input, width=30)
    entry_nama.grid(row=0, column=1)

    tk.Label(frame_input, text="Jenis").grid(row=1, column=0, sticky="w")
    entry_jenis = tk.Entry(frame_input, width=30)
    entry_jenis.grid(row=1, column=1)

    tk.Label(frame_input, text="Harga").grid(row=2, column=0, sticky="w")
    entry_harga = tk.Entry(frame_input, width=30)
    entry_harga.grid(row=2, column=1)

    tk.Label(frame_input, text="Stok").grid(row=3, column=0, sticky="w")
    entry_stok = tk.Entry(frame_input, width=30)
    entry_stok.grid(row=3, column=1)

    tk.Label(frame_input, text="Kadaluarsa").grid(row=4, column=0, sticky="w")
    entry_kadaluarsa = tk.Entry(frame_input, width=30)
    entry_kadaluarsa.grid(row=4, column=1)

    # --- Fungsi bantu ---
    def refresh_data_obat():
        tabel_obat.delete(*tabel_obat.get_children())
        data = lihatSemuaDataObat()
        if isinstance(data, str):
            messagebox.showinfo("Info", data)
            return
        for d in data:
            tabel_obat.insert("", "end", values=(
                d["obatId"], d["namaObat"], d["jenis"], d["harga"], d["stok"], d["kadaluarsa"]
            ))

    def tambah_data():
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        harga = entry_harga.get()
        stok = entry_stok.get()
        kadaluarsa = entry_kadaluarsa.get()

        if not all([nama, jenis, harga, stok, kadaluarsa]):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        pesan = tambahObat(nama, jenis, harga, stok, kadaluarsa)
        messagebox.showinfo("Info", pesan)
        refresh_data_obat()

    def hapus_data():
        selected = tabel_obat.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return
        obatId = tabel_obat.item(selected[0])["values"][0]
        pesan = hapusObat(obatId)
        messagebox.showinfo("Info", pesan)
        refresh_data_obat()

    def update_data():
        selected = tabel_obat.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin diupdate!")
            return
        obatId = tabel_obat.item(selected[0])["values"][0]
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        harga = entry_harga.get()
        stok = entry_stok.get()
        kadaluarsa = entry_kadaluarsa.get()

        if not all([nama, jenis, harga, stok, kadaluarsa]):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        pesan = updateObat(obatId, nama, jenis, harga, stok, kadaluarsa)
        messagebox.showinfo("Info", pesan)
        refresh_data_obat()

    def isi_form_dari_tabel(event):
        selected = tabel_obat.selection()
        if selected:
            data = tabel_obat.item(selected[0])["values"]
            entry_nama.delete(0, tk.END)
            entry_nama.insert(0, data[1])
            entry_jenis.delete(0, tk.END)
            entry_jenis.insert(0, data[2])
            entry_harga.delete(0, tk.END)
            entry_harga.insert(0, data[3])
            entry_stok.delete(0, tk.END)
            entry_stok.insert(0, data[4])
            entry_kadaluarsa.delete(0, tk.END)
            entry_kadaluarsa.insert(0, data[5])

    tabel_obat.bind("<<TreeviewSelect>>", isi_form_dari_tabel)

    # --- Tombol Aksi ---
    frame_button = tk.Frame(frame_obat)
    frame_button.pack(pady=10)

    tk.Button(frame_button, text="Tambah", command=tambah_data, bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
    tk.Button(frame_button, text="Update", command=update_data, bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)
    tk.Button(frame_button, text="Hapus", command=hapus_data, bg="#f44336", fg="white", width=12).grid(row=0, column=2, padx=5)
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
            tabel_transaksi.insert("", "end", values=(
                d["transaksiId"], d["tanggalTransaksi"], d["Kasir"], d["totalHarga"]
            ))

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

    # Load data awal
    refresh_data_obat()
    refresh_transaksi()

    tk.Button(root, text="Keluar", command=root.destroy, width=15).pack(pady=10)

    root.mainloop()
