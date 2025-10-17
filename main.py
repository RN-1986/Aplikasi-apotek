# main.py
import tkinter as tk
from tkinter import messagebox
from frontend.tampilanLogin import tampil_login
from frontend.tampilanRegister import tampil_register
from frontend.tampilanAdmin import tampil_admin
from backend.login import session

def menu_awal():
    root = tk.Tk()
    root.title("Aplikasi Apotek - Menu Awal")
    root.geometry("300x300")
    root.resizable(False, False)

    tk.Label(root, text="Selamat Datang di Aplikasi Apotek", font=("Arial", 12, "bold")).pack(pady=30)
    tk.Label(root, text="Silakan pilih menu:").pack(pady=10)

    tk.Button(root, text="Login", width=20, command=lambda: [root.destroy(), tampil_login()]).pack(pady=5)
    tk.Button(root, text="Register", width=20, command=lambda: [root.destroy(), tampil_register()]).pack(pady=5)
    tk.Button(root, text="Keluar", width=20, command=root.destroy).pack(pady=5)

    root.mainloop()

# --- Jalankan program ---
menu_awal()

# Setelah jendela login/register ditutup, periksa apakah user berhasil login
if session.get('is_login'):
    role = session['dataUser']['role']
    
    if role.lower() == 'admin':
        tampil_admin()
    else:
        messagebox.showinfo("Info", f"Role '{role}' belum memiliki tampilan GUI.")
else:
    print("Belum login atau program ditutup.")
