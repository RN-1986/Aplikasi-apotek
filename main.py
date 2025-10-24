# main.py
import tkinter as tk
from tkinter import messagebox
from frontend.tampilanLogin import tampil_login
from frontend.tampilanRegister import tampil_register
from frontend.tampilanAdmin import tampil_admin
from frontend.tampilanApoteker import tampil_apoteker
from frontend.tampilanKasir import tampil_kasir
from backend.login import session


def menu_awal():
    """Tampilan menu utama aplikasi"""
    root = tk.Tk()
    root.title("Aplikasi Apotek - Menu Awal")
    root.geometry("300x300")
    root.resizable(False, False)

    # Pastikan session login bersih setiap kali ke menu awal
    session.clear()

    tk.Label(
        root,
        text="Selamat Datang di Aplikasi Apotek",
        font=("Arial", 12, "bold")
    ).pack(pady=30)
    tk.Label(root, text="Silakan pilih menu:").pack(pady=10)

    # Tombol-tombol menu utama
    tk.Button(
        root,
        text="Login",
        width=20,
        command=lambda: [root.destroy(), tampil_login()]
    ).pack(pady=5)

    tk.Button(
        root,
        text="Register",
        width=20,
        command=lambda: [root.destroy(), tampil_register()]
    ).pack(pady=5)

    def keluar_aplikasi():
        """Menutup aplikasi sepenuhnya"""
        konfirmasi = messagebox.askyesno("Konfirmasi", "Yakin ingin keluar dari aplikasi?")
        if konfirmasi:
            root.destroy()

    tk.Button(
        root,
        text="Keluar",
        width=20,
        bg="#ff4d4d",
        fg="white",
        command=keluar_aplikasi
    ).pack(pady=5)

    root.mainloop()


def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    menu_awal()

    # Setelah jendela menu awal ditutup, cek apakah user login
    if session.get('is_login'):
        role = session['dataUser'].get('role', '').lower()

        if role == 'admin':
            tampil_admin()
        elif role == 'apoteker':
            tampil_apoteker()
        elif role == 'kasir':
            tampil_kasir()
        else:
            messagebox.showinfo("Info", f"Role '{role}' belum memiliki tampilan GUI.")
    else:
        # Jika user keluar dari menu utama tanpa login
        print("Program ditutup oleh pengguna.")
        return


if __name__ == "__main__":
    main()
