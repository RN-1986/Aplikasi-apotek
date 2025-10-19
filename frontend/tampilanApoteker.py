import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.apoteker import (
    buatKeranjang,
    lihatKeranjang,
    tambahObatKeKeranjang,
    updateJumlahObatYangDiBeli,
    hapusObatDariKeranjang,
    kirimKeranjangKeKasir,
    batalkanKeranjang
)

def tampil_apoteker():
    root = tk.Tk()
    root.title("🧴 Aplikasi Apotek - Menu Apoteker")
    root.geometry("850x600")
    root.resizable(True, True)

    # ==============================
    # FRAME INFO PEMBELI
    # ==============================
    frame_info = tk.Frame(root)
    frame_info.pack(pady=5)

    nama_pembeli_label = tk.Label(frame_info, text="Nama Pembeli: -", font=("Arial", 12, "bold"))
    nama_pembeli_label.pack()

    # ==============================
    # FRAME TOMBOL
    # ==============================
    frame_tombol = tk.Frame(root)
    frame_tombol.pack(pady=10)

    # ==============================
    # FRAME TABEL
    # ==============================
    frame_tabel = tk.Frame(root)
    frame_tabel.pack(fill="both", expand=True, padx=10, pady=10)

    kolom = ("Nama Obat", "Jumlah", "Subtotal")
    tabel = ttk.Treeview(frame_tabel, columns=kolom, show="headings", height=15)
    for col in kolom:
        tabel.heading(col, text=col)
        tabel.column(col, width=200, anchor="center")
    tabel.pack(fill="both", expand=True)

    total_label = tk.Label(root, text="Total Harga: Rp 0.00", font=("Arial", 12, "bold"))
    total_label.pack(pady=10)

    # ==============================
    # FUNGSI UTILITAS
    # ==============================
    def refresh_tampilan():
        """Mengosongkan tampilan tabel dan label"""
        tabel.delete(*tabel.get_children())
        nama_pembeli_label.config(text="Nama Pembeli: -")
        total_label.config(text="Total Harga: Rp 0.00")
        messagebox.showinfo("Info", "Tampilan berhasil di-refresh.", parent=root)

    # ==============================
    # FUNGSI GUI
    # ==============================
    def buat_keranjang_gui():
        apotekerId = simpledialog.askinteger("Input", "Masukkan ID Apoteker:", parent=root)
        if not apotekerId:
            return

        nama_pembeli = simpledialog.askstring("Input", "Masukkan nama pembeli:", parent=root)
        if not nama_pembeli:
            return

        hasil = buatKeranjang(apotekerId, nama_pembeli)
        messagebox.showinfo("Info", f"Keranjang baru dibuat dengan ID: {hasil}", parent=root)

    def lihat_keranjang_gui():
        keranjang_id = simpledialog.askinteger("Input", "Masukkan ID Keranjang:", parent=root)
        if not keranjang_id:
            return

        data = lihatKeranjang(keranjang_id)
        tabel.delete(*tabel.get_children())

        if isinstance(data, dict):
            nama_pembeli_label.config(text=f"Nama Pembeli: {data.get('namaPembeli', '-')}")
            for item in data['detailObat']:
                tabel.insert("", "end", values=(item['namaObat'], item['jumlah'], item['subtotal']))
            total_label.config(text=f"Total Harga: Rp {data['totalHarga']:.2f}")
        else:
            nama_pembeli_label.config(text="Nama Pembeli: -")
            total_label.config(text="Total Harga: Rp 0.00")
            messagebox.showerror("Error", data, parent=root)

    def tambah_obat_gui():
        popup = tk.Toplevel(root)
        popup.title("Tambah Obat ke Keranjang")
        popup.geometry("300x250")
        popup.grab_set()  # Fokus ke popup

        tk.Label(popup, text="ID Keranjang:").pack(pady=5)
        entry_keranjang = tk.Entry(popup)
        entry_keranjang.pack()

        tk.Label(popup, text="ID Obat:").pack(pady=5)
        entry_obat = tk.Entry(popup)
        entry_obat.pack()

        tk.Label(popup, text="Jumlah:").pack(pady=5)
        entry_jumlah = tk.Entry(popup)
        entry_jumlah.pack()

        def submit():
            keranjang_id = entry_keranjang.get()
            obat_id = entry_obat.get()
            jumlah = entry_jumlah.get()
            if not keranjang_id or not obat_id or not jumlah:
                messagebox.showwarning("Peringatan", "Semua field wajib diisi!", parent=popup)
                return

            hasil = tambahObatKeKeranjang(int(keranjang_id), int(obat_id), int(jumlah))
            messagebox.showinfo("Info", hasil, parent=popup)
            popup.destroy()

        tk.Button(popup, text="Tambah", command=submit).pack(pady=10)
        tk.Button(popup, text="Batal", command=popup.destroy).pack()

    def update_jumlah_gui():
        detail_id = simpledialog.askinteger("Input", "Masukkan ID Detail Keranjang:", parent=root)
        jumlah_baru = simpledialog.askinteger("Input", "Masukkan jumlah baru:", parent=root)
        if not all([detail_id, jumlah_baru]):
            return

        hasil = updateJumlahObatYangDiBeli(detail_id, jumlah_baru)
        messagebox.showinfo("Info", hasil, parent=root)

    def hapus_obat_gui():
        detail_id = simpledialog.askinteger("Input", "Masukkan ID Detail Keranjang:", parent=root)
        if not detail_id:
            return

        hasil = hapusObatDariKeranjang(detail_id)
        messagebox.showinfo("Info", hasil, parent=root)

    def kirim_keranjang_gui():
        keranjang_id = simpledialog.askinteger("Input", "Masukkan ID Keranjang:", parent=root)
        if not keranjang_id:
            return

        hasil = kirimKeranjangKeKasir(keranjang_id)
        messagebox.showinfo("Info", hasil, parent=root)

    def batalkan_keranjang_gui():
        keranjang_id = simpledialog.askinteger("Input", "Masukkan ID Keranjang:", parent=root)
        if not keranjang_id:
            return

        hasil = batalkanKeranjang(keranjang_id)
        messagebox.showinfo("Info", hasil, parent=root)

    # ==============================
    # TOMBOL MENU ATAS
    # ==============================
    tombol_list = [
        ("🛒 Buat Keranjang", buat_keranjang_gui),
        ("👁️ Lihat Keranjang", lihat_keranjang_gui),
        ("➕ Tambah Obat", tambah_obat_gui),
        ("✏️ Update Jumlah", update_jumlah_gui),
        ("❌ Hapus Obat", hapus_obat_gui),
        ("📦 Kirim ke Kasir", kirim_keranjang_gui),
        ("🚫 Batalkan Keranjang", batalkan_keranjang_gui),
        ("🔄 Refresh", refresh_tampilan)
    ]

    for i, (text, cmd) in enumerate(tombol_list):
        tk.Button(frame_tombol, text=text, width=20, command=cmd).grid(row=i // 2, column=i % 2, padx=5, pady=5)

    # ==============================
    # TOMBOL KELUAR DI BAWAH
    # ==============================
    frame_keluar = tk.Frame(root)
    frame_keluar.pack(pady=15)

    tombol_keluar = tk.Button(frame_keluar, text="Keluar", width=20, bg="#ff4d4d", fg="white", command=root.destroy)
    tombol_keluar.pack()

    root.mainloop()


# Jalankan langsung jika file ini dibuka sendiri
if __name__ == "__main__":
    tampil_apoteker()
