# frontend/tampilanRegister.py
import tkinter as tk
from tkinter import messagebox

# import fungsi register dari backend (pastikan backend adalah package)
from backend.register import register

# import module tampilanLogin (import module, bukan memanggil fungsi otomatis)
from frontend import tampilanLogin

def buka_login(root):
    root.destroy()      # tutup form register
    tampilanLogin.tampil_login()  # panggil fungsi tampil_login() dari tampilanLogin.py

def tampil_register():
    root = tk.Tk()
    root.title("Form Register")
    root.geometry("320x380")
    root.resizable(False, False)

    # Label dan Entry Nama
    tk.Label(root, text="Nama:").pack(pady=5)
    entry_nama = tk.Entry(root)
    entry_nama.pack()

    # Label dan Entry Username
    tk.Label(root, text="Username:").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack()

    # Label dan Entry Password
    tk.Label(root, text="Password:").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    # Label dan Entry Konfirmasi Password
    tk.Label(root, text="Konfirmasi Password:").pack(pady=5)
    entry_confirm = tk.Entry(root, show="*")
    entry_confirm.pack()

    # Dropdown Role
    tk.Label(root, text="Pilih Role:").pack(pady=5)
    role_var = tk.StringVar(value="Pilih role")
    roles = ["Admin", "Apoteker", "Kasir"]
    tk.OptionMenu(root, role_var, *roles).pack()

    # Fungsi ketika tombol Register ditekan
    def aksi_register():
        nama = entry_nama.get().strip()
        username = entry_username.get().strip()
        password = entry_password.get()
        confirm = entry_confirm.get()
        role = role_var.get()

        if not nama or not username or not password or not confirm or role == "Pilih role":
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        if password != confirm:
            messagebox.showerror("Error", "Password dan konfirmasi tidak cocok!")
            return

        # panggil backend register
        hasil = register(nama, username, password, role)
        messagebox.showinfo("Informasi", hasil)

        # jika backend mengembalikan "berhasil"
        if isinstance(hasil, str) and "berhasil" in hasil.lower():
            buka_login(root)

    # Tombol Register
    tk.Button(root, text="Register", command=aksi_register, bg="lightblue").pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    # RUN dari root package: python -m frontend.tampilanRegister
    tampil_register()
