import tkinter as tk
from tkinter import ttk, messagebox
from backend.kasir import lihatDaftarKeranjangDikirim, lihatDetailKeranjangUntukKasir, kondisiTransaksi
from backend.admin import lihatSemuaTransaksi, lihatDetailTransaksi

def tampil_kasir():
    root = tk.Tk()
    root.title("Dashboard Kasir - Aplikasi Apotek")
    root.geometry("1000x620")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # =========================
    # TAB 1: KERANJANG DIKIRIM
    # =========================
    frame_keranjang = tk.Frame(notebook)
    notebook.add(frame_keranjang, text="Keranjang Dikirim")

    tk.Label(frame_keranjang, text="Daftar Keranjang Dikirim", font=("Arial", 16, "bold")).pack(pady=10)

    columns_keranjang = ("keranjangId", "namaPembeli", "totalHarga", "namaApoteker", "status")
    tabel_keranjang = ttk.Treeview(frame_keranjang, columns=columns_keranjang, show="headings", height=10)
    for col in columns_keranjang:
        tabel_keranjang.heading(col, text=col)
        tabel_keranjang.column(col, width=150)
    tabel_keranjang.pack(fill="both", expand=True, padx=10)

    def refresh_keranjang():
        tabel_keranjang.delete(*tabel_keranjang.get_children())
        data = lihatDaftarKeranjangDikirim()
        if isinstance(data, str):
            messagebox.showinfo("Info", data)
            return
        for d in data:
            tabel_keranjang.insert("", "end", values=d)

    def lihat_detail_keranjang():
        selected = tabel_keranjang.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih keranjang untuk melihat detail!")
            return
        keranjangId = tabel_keranjang.item(selected[0])["values"][0]
        dataDetail = lihatDetailKeranjangUntukKasir(keranjangId)
        if isinstance(dataDetail, str):
            messagebox.showinfo("Info", dataDetail)
            return

        detail_window = tk.Toplevel(root)
        detail_window.title(f"Detail Keranjang {keranjangId}")
        detail_window.geometry("500x300")

        columns_detail = ("namaObat", "jumlah", "subtotal")
        tabel_detail = ttk.Treeview(detail_window, columns=columns_detail, show="headings")
        for col in columns_detail:
            tabel_detail.heading(col, text=col)
            tabel_detail.column(col, width=150)
        tabel_detail.pack(fill="both", expand=True, padx=10, pady=10)

        for d in dataDetail["detail"]:
            tabel_detail.insert("", "end", values=(d["namaObat"], d["jumlah"], d["subtotal"]))

    def bayar_keranjang():
        selected = tabel_keranjang.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih keranjang yang ingin dibayar!")
            return
        keranjangId = tabel_keranjang.item(selected[0])["values"][0]
        pesan = kondisiTransaksi(keranjangId, "dibayar")
        messagebox.showinfo("Info", pesan)
        refresh_keranjang()
        refresh_transaksi()

    def batal_keranjang():
        selected = tabel_keranjang.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih keranjang yang ingin dibatalkan!")
            return
        keranjangId = tabel_keranjang.item(selected[0])["values"][0]
        pesan = kondisiTransaksi(keranjangId, "dibatalkan")
        messagebox.showinfo("Info", pesan)
        refresh_keranjang()

    frame_btn_keranjang = tk.Frame(frame_keranjang)
    frame_btn_keranjang.pack(pady=10)
    tk.Button(frame_btn_keranjang, text="Refresh", command=refresh_keranjang, width=15).grid(row=0, column=0, padx=5)
    tk.Button(frame_btn_keranjang, text="Lihat Detail", command=lihat_detail_keranjang, width=15).grid(row=0, column=1, padx=5)
    tk.Button(frame_btn_keranjang, text="Bayar", command=bayar_keranjang, bg="green", fg="white", width=15).grid(row=0, column=2, padx=5)
    tk.Button(frame_btn_keranjang, text="Batalkan", command=batal_keranjang, bg="red", fg="white", width=15).grid(row=0, column=3, padx=5)

    # =========================
    # TAB 2: RIWAYAT TRANSAKSI
    # =========================
    frame_transaksi = tk.Frame(notebook)
    notebook.add(frame_transaksi, text="Riwayat Transaksi")

    tk.Label(frame_transaksi, text="Riwayat Transaksi", font=("Arial", 16, "bold")).pack(pady=10)

    columns_trans = ("transaksiId", "tanggalTransaksi", "Kasir", "totalHarga")
    tabel_transaksi = ttk.Treeview(frame_transaksi, columns=columns_trans, show="headings", height=10)
    for col in columns_trans:
        tabel_transaksi.heading(col, text=col)
        tabel_transaksi.column(col, width=150)
    tabel_transaksi.pack(fill="both", expand=True, padx=10)

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

    # =========================
    # KELUAR KE MENU UTAMA
    # =========================
    def keluar_dari_aplikasi():
        from backend.logout import logout
        pesan = logout()
        messagebox.showinfo("Logout", pesan)
        root.destroy()
        from main import main
        main()

    tk.Button(root, text="Keluar", command=keluar_dari_aplikasi, width=15, bg="#ff4d4d", fg="white").pack(pady=10)

    # Load data awal
    refresh_keranjang()
    refresh_transaksi()

    root.mainloop()

if __name__ == "__main__":
    tampil_kasir()