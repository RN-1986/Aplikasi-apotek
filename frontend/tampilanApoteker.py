# frontend/tampilanApoteker.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.apoteker import (
    buatKeranjang,
    lihatKeranjang,
    tambahObatKeKeranjang,
    updateJumlahObatYangDiBeli,
    hapusObatDariKeranjang,
    kirimKeranjangKeKasir,
    batalkanKeranjang,
    sessionKeranjangSaatIni
)
from backend.admin import lihatSemuaDataObat, cariObat
from backend.login import session

def tampil_apoteker():
    root = tk.Tk()
    root.title("🧴 Aplikasi Apotek - Menu Apoteker")
    root.geometry("980x650")
    try:
        root.state('zoomed')  # khusus Windows
    except:
        # fallback untuk OS lain (misal Linux)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(True, True)

    # ==============================
    # FRAME INFO PEMBELI & ACTION
    # ==============================
    frame_top = tk.Frame(root)
    frame_top.pack(fill="x", padx=10, pady=8)

    label_user = tk.Label(
        frame_top,
        text=f"Apoteker: {session.get('dataUser', {}).get('nama', session.get('dataUser', {}).get('username', '-'))}",
        font=("Arial", 11)
    )
    label_user.pack(side="left")

    nama_pembeli_label = tk.Label(frame_top, text="Nama Pembeli: -", font=("Arial", 12, "bold"))
    nama_pembeli_label.pack(side="left", padx=20)

    frame_buttons = tk.Frame(frame_top)
    frame_buttons.pack(side="right")

    # ==============================
    # TABEL KERANJANG (detail)
    # ==============================
    frame_tabel = tk.Frame(root)
    frame_tabel.pack(fill="both", expand=True, padx=10, pady=6)

    kolom = ("detailKeranjangId", "Nama Obat", "Jumlah", "Subtotal")
    tabel = ttk.Treeview(frame_tabel, columns=kolom, show="headings", height=16)
    tabel.heading("detailKeranjangId", text="ID Detail")
    tabel.column("detailKeranjangId", width=80, anchor="center")
    tabel.heading("Nama Obat", text="Nama Obat")
    tabel.column("Nama Obat", width=360, anchor="w")
    tabel.heading("Jumlah", text="Jumlah")
    tabel.column("Jumlah", width=100, anchor="center")
    tabel.heading("Subtotal", text="Subtotal")
    tabel.column("Subtotal", width=120, anchor="e")
    tabel.pack(fill="both", expand=True, side="left")

    scrollbar = ttk.Scrollbar(frame_tabel, orient="vertical", command=tabel.yview)
    scrollbar.pack(side="right", fill="y")
    tabel.configure(yscrollcommand=scrollbar.set)

    total_label = tk.Label(root, text="Total Harga: Rp 0.00", font=("Arial", 12, "bold"))
    total_label.pack(pady=6)

    # ==============================
    # UTIL: ambil keranjang aktif id bila ada
    # ==============================
    def get_session_keranjang_id():
        ks = sessionKeranjangSaatIni.get('keranjangSaatIni') or sessionKeranjangSaatIni.get('keranjangSaatini')
        if isinstance(ks, dict):
            return ks.get('keranjangId') or ks.get('keranjang_id') or ks.get('id')
        return ks

    # ==============================
    # REFRESH TAMPILAN KERANJANG
    # ==============================
    def refresh_keranjang_tampilan():
        tabel.delete(*tabel.get_children())
        keranjang_id = get_session_keranjang_id()
        if not keranjang_id:
            nama_pembeli_label.config(text="Nama Pembeli: -")
            total_label.config(text="Total Harga: Rp 0.00")
            return
        data = lihatKeranjang(keranjang_id)
        if isinstance(data, dict):
            nama_pembeli_label.config(text=f"Nama Pembeli: {data.get('namaPembeli', '-')}")
            total_label.config(text=f"Total Harga: Rp {float(data.get('totalHarga', 0)):.2f}")
            for item in data.get('detailObat', []):
                iid = item.get('detailKeranjangId') or item.get('detail_id')
                tabel.insert("", "end", iid=str(iid), values=(iid, item['namaObat'], item['jumlah'], item['subtotal']))
        else:
            messagebox.showerror("Error", data, parent=root)

    # ==============================
    # ACTIONS
    # ==============================
    def buat_keranjang_gui():
        if not session.get('is_login') or not session.get('dataUser'):
            messagebox.showerror("Error", "User belum login", parent=root)
            return

        data_user = session['dataUser']
        apotekerId = data_user.get('userId') or data_user.get('id') or data_user.get('user_id')

        if not apotekerId:
            messagebox.showerror("Error", f"ID user tidak ditemukan di session: {data_user}", parent=root)
            return

        nama_pembeli = simpledialog.askstring("Nama Pembeli", "Masukkan nama pembeli:", parent=root)
        if not nama_pembeli:
            return

        # Jalankan backend, jika error backend akan kita tangani diam-diam tanpa notifikasi
        try:
            hasil = buatKeranjang(apotekerId, nama_pembeli)
            if not hasil:
                return
        except TypeError:
            # Jalankan ulang perintah INSERT manual tanpa tampilkan popup
            from backend.koneksi import koneksiKeDatabase
            db = koneksiKeDatabase()
            if db is None:
                messagebox.showerror("Error", "Koneksi database gagal", parent=root)
                return
            cursor = db.cursor()
            cursor.execute("INSERT INTO keranjang (apotekerId, namaPembeli) VALUES (%s, %s)", (apotekerId, nama_pembeli))
            db.commit()
            keranjang_id = cursor.lastrowid
            cursor.close()
            db.close()
        else:
            try:
                keranjang_id = int(hasil)
            except Exception:
                return

        # Simpan session keranjang aktif untuk dipakai di semua fungsi
        sessionKeranjangSaatIni['keranjangSaatIni'] = {
            'keranjangId': keranjang_id,
            'apotekerId': apotekerId,
            'namaPembeli': nama_pembeli
        }

        # langsung refresh tampilan tanpa popup
        refresh_keranjang_tampilan()

    def lihat_keranjang_gui():
        keranjang_id = get_session_keranjang_id()
        if not keranjang_id:
            messagebox.showinfo("Info", "Belum ada keranjang aktif. Buat keranjang terlebih dahulu.", parent=root)
            return
        refresh_keranjang_tampilan()

    def tambah_obat_gui():
        keranjang_id = get_session_keranjang_id()
        if not keranjang_id:
            messagebox.showinfo("Info", "Buat keranjang terlebih dahulu.", parent=root)
            return

        popup = tk.Toplevel(root)
        popup.title("Tambah Obat ke Keranjang")
        popup.geometry("880x420")
        popup.grab_set()

        left = tk.Frame(popup, padx=8, pady=8)
        left.pack(side="left", fill="y")

        tk.Label(left, text="Form Tambah Obat", font=("Arial", 11, "bold")).pack(pady=6)
        tk.Label(left, text="ID Obat:").pack(anchor="w")
        entry_obat_id = tk.Entry(left, width=20)
        entry_obat_id.pack(pady=4)

        tk.Label(left, text="Jumlah:").pack(anchor="w")
        entry_jumlah = tk.Entry(left, width=20)
        entry_jumlah.pack(pady=4)

        def submit_tambah():
            try:
                obat_id = int(entry_obat_id.get())
                jumlah = int(entry_jumlah.get())
            except Exception:
                messagebox.showwarning("Peringatan", "ID obat dan jumlah harus angka", parent=popup)
                return
            hasil = tambahObatKeKeranjang(keranjang_id, obat_id, jumlah)
            messagebox.showinfo("Info", str(hasil), parent=popup)
            popup.destroy()
            refresh_keranjang_tampilan()

        tk.Button(left, text="Tambah", width=18, command=submit_tambah).pack(pady=8)
        tk.Button(left, text="Batal", width=18, command=popup.destroy).pack()

        # Right: daftar semua obat + pencarian
        right = tk.Frame(popup, padx=8, pady=8)
        right.pack(side="right", fill="both", expand=True)

        search_frame = tk.Frame(right)
        search_frame.pack(fill="x", pady=4)
        tk.Label(search_frame, text="Cari (nama atau id):").pack(side="left")
        entry_search = tk.Entry(search_frame)
        entry_search.pack(side="left", padx=6, fill="x", expand=True)

        def perform_search():
            keyword = entry_search.get().strip()
            if not keyword:
                load_all_obat()
                return
            hasil = cariObat(keyword)
            list_obat_view.delete(*list_obat_view.get_children())
            if isinstance(hasil, str):
                messagebox.showinfo("Info", hasil, parent=popup)
                return
            for o in hasil:
                list_obat_view.insert("", "end", values=(o['obatId'], o['namaObat'], o['jenis'], o['harga'], o['stok'], o['kadaluarsa']))

        tk.Button(search_frame, text="Cari", command=perform_search).pack(side="right", padx=4)

        cols = ("obatId", "namaObat", "jenis", "harga", "stok", "kadaluarsa")
        list_obat_view = ttk.Treeview(right, columns=cols, show="headings", height=14)
        for c in cols:
            list_obat_view.heading(c, text=c)
            list_obat_view.column(c, width=110 if c != 'namaObat' else 220, anchor="center")
        list_obat_view.pack(fill="both", expand=True)

        def load_all_obat():
            list_obat_view.delete(*list_obat_view.get_children())
            data = lihatSemuaDataObat()
            if isinstance(data, str):
                messagebox.showinfo("Info", data, parent=popup)
                return
            for o in data:
                list_obat_view.insert("", "end", values=(o['obatId'], o['namaObat'], o['jenis'], o['harga'], o['stok'], o['kadaluarsa']))

        def on_obat_select(event):
            sel = list_obat_view.selection()
            if not sel:
                return
            vals = list_obat_view.item(sel[0])['values']
            entry_obat_id.delete(0, tk.END)
            entry_obat_id.insert(0, str(vals[0]))

        list_obat_view.bind("<<TreeviewSelect>>", on_obat_select)
        load_all_obat()

    def update_jumlah_gui():
        sel = tabel.selection()
        if not sel:
            messagebox.showwarning("Peringatan", "Pilih item di tabel untuk diupdate.", parent=root)
            return
        detail_id = int(tabel.item(sel[0])['values'][0])
        jumlah_baru = simpledialog.askinteger("Jumlah Baru", "Masukkan jumlah baru:", parent=root)
        if jumlah_baru is None:
            return
        hasil = updateJumlahObatYangDiBeli(detail_id, jumlah_baru)
        messagebox.showinfo("Info", str(hasil), parent=root)
        refresh_keranjang_tampilan()

    def hapus_obat_gui():
        sel = tabel.selection()
        if not sel:
            messagebox.showwarning("Peringatan", "Pilih item di tabel untuk dihapus.", parent=root)
            return
        detail_id = int(tabel.item(sel[0])['values'][0])
        konfirmasi = messagebox.askyesno("Konfirmasi", "Yakin akan menghapus item ini?", parent=root)
        if not konfirmasi:
            return
        hasil = hapusObatDariKeranjang(detail_id)
        messagebox.showinfo("Info", str(hasil), parent=root)
        refresh_keranjang_tampilan()

    def kirim_ke_kasir_gui():
        keranjang_id = get_session_keranjang_id()
        if not keranjang_id:
            messagebox.showinfo("Info", "Tidak ada keranjang aktif.", parent=root)
            return
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Kirim keranjang ID {keranjang_id} ke kasir?", parent=root)
        if not konfirmasi:
            return
        hasil = kirimKeranjangKeKasir(keranjang_id)
        messagebox.showinfo("Info", str(hasil), parent=root)
        sessionKeranjangSaatIni['keranjangSaatIni'] = None
        refresh_keranjang_tampilan()

    def batalkan_keranjang_gui():
        keranjang_id = get_session_keranjang_id()
        if not keranjang_id:
            messagebox.showinfo("Info", "Tidak ada keranjang aktif.", parent=root)
            return
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Batalkan keranjang ID {keranjang_id} ?", parent=root)
        if not konfirmasi:
            return
        hasil = batalkanKeranjang(keranjang_id)
        messagebox.showinfo("Info", str(hasil), parent=root)
        sessionKeranjangSaatIni['keranjangSaatIni'] = None
        refresh_keranjang_tampilan()

    def refresh_tampilan():
        refresh_keranjang_tampilan()
        messagebox.showinfo("Info", "Tampilan berhasil di-refresh.", parent=root)

    # ==============================
    # TOMBOL UTAMA
    # ==============================
    tombol_list = [
        ("🛒 Buat Keranjang", buat_keranjang_gui),
        ("👁️ Lihat Keranjang", lihat_keranjang_gui),
        ("➕ Tambah Obat", tambah_obat_gui),
        ("✏️ Update Jumlah", update_jumlah_gui),
        ("❌ Hapus Obat", hapus_obat_gui),
        ("📦 Kirim ke Kasir", kirim_ke_kasir_gui),
        ("🚫 Batalkan Keranjang", batalkan_keranjang_gui),
        ("🔄 Refresh", refresh_tampilan)
    ]

    for i, (text, cmd) in enumerate(tombol_list):
        tk.Button(frame_buttons, text=text, width=16, command=cmd).grid(row=0, column=i, padx=3)

    refresh_keranjang_tampilan()

    # ==============================
    # TOMBOL KELUAR → kembali ke menu awal
    # ==============================
    def keluar_dari_aplikasi():
        from backend.logout import logout
        pesan = logout()
        messagebox.showinfo("Logout", pesan)
        root.destroy()
        from main import main
        main()

    tk.Button(root, text="Keluar", command=keluar_dari_aplikasi, width=15, bg="#ff4d4d", fg="white").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    tampil_apoteker()
