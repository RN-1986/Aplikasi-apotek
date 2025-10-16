import tkinter as tk
from tkinter import messagebox
from backend.login import login, session

def proses_login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
        return

    pesan = login(username, password)

    if session['is_login']:
        messagebox.showinfo("Login Berhasil", pesan)
        root.destroy()
    else:
        messagebox.showerror("Login Gagal", pesan)

root = tk.Tk()
root.title("Login Aplikasi Apotek")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Username").pack(pady=(20, 5))
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=(10, 5))
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=proses_login).pack(pady=20)

root.mainloop()