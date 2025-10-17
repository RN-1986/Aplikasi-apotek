# frontend/tampilanAdmin.py
import tkinter as tk
from tkinter import ttk, messagebox
from backend.admin import lihatSemuaDataObat, tambahObat, updateObat, hapusObat

def tampil_admin():
    root = tk.Tk()
    root.title("Dashboard Admin - Aplikasi Apotek")
    root.geometry("800x500")

    # Judul
    tk.Label(root, text="Dashboard Admin - Kelola Obat", font=("Arial", 16, "bold")).pack(pady=10)

    # --- Frame Data ---
    frame_data = tk.Frame(root)
    frame_data.pack(pady=10)

    columns = ("obatId", "namaObat", "jenis", "harga", "stok", "kadaluarsa")
    tabel = ttk.Treeview(frame_data, columns=columns, show="headings", height=10)

    for col in columns:
        tabel.heading(col, text=col)
        tabel.column(col, width=120)

    tabel.pack(side="left")
    scrollbar = ttk.Scrollbar(frame_data, orient="vertical", command=tabel.yview)
    scrollbar.pack(side="right", fill="y")
    tabel.configure(yscrollcommand=scrollbar.set)

    # --- Frame Input ---
    frame_input = tk.LabelFrame(root, text="Form Obat", padx=10, pady=10)
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
    def refresh_data():
        tabel.delete(*tabel.get_children())
        data = lihatSemuaDataObat()
        if isinstance(data, str):
            messagebox.showinfo("Info", data)
            return
        for d in data:
            tabel.insert("", "end", values=(
                d["obatId"], d["namaObat"], d["jenis"], d["harga"], d["stok"], d["kadaluarsa"]
            ))

    def tambah_data():
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        harga = entry_harga.get()
        stok = entry_stok.get()
        kadaluarsa = entry_kadaluarsa.get()

        if not nama or not jenis or not harga or not stok or not kadaluarsa:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        pesan = tambahObat(nama, jenis, harga, stok, kadaluarsa)
        messagebox.showinfo("Info", pesan)
        refresh_data()

    def hapus_data():
        selected = tabel.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return
        obatId = tabel.item(selected[0])["values"][0]
        pesan = hapusObat(obatId)
        messagebox.showinfo("Info", pesan)
        refresh_data()

    # --- Tombol Aksi ---
    frame_button = tk.Frame(root)
    frame_button.pack(pady=10)

    tk.Button(frame_button, text="Tambah Obat", command=tambah_data, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
    tk.Button(frame_button, text="Hapus Obat", command=hapus_data, bg="#f44336", fg="white", width=15).grid(row=0, column=1, padx=5)
    tk.Button(frame_button, text="Refresh Data", command=refresh_data, width=15).grid(row=0, column=2, padx=5)
    tk.Button(frame_button, text="Keluar", command=root.destroy, width=15).grid(row=0, column=3, padx=5)

    # Load data pertama kali
    refresh_data()

    root.mainloop()
