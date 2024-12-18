import tkinter as tk
from tkinter import messagebox, simpledialog
from modules.utils import load_accounts, save_accounts
from modules.question import main_menu

# Login system
def login():
    accounts = load_accounts()

    def validate_login():
        username = entry_user.get()
        password = entry_pass.get()
        if accounts.get(username) == password:
            messagebox.showinfo("Login Berhasil", f"Selamat Datang, {username}!")
            root.destroy()
            main_menu(username)  # Pass the username to main menu
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def register():
        new_user = simpledialog.askstring("Registrasi", "Masukkan Username Baru:")
        new_pass = simpledialog.askstring("Registrasi", "Masukkan Password Baru:", show="*")
        if new_user and new_pass:
            if new_user in accounts:
                messagebox.showerror("Error", "Username sudah terdaftar!")
            else:
                accounts[new_user] = new_pass
                save_accounts(accounts)
                messagebox.showinfo("Sukses", "Registrasi Berhasil!")
        else:
            messagebox.showerror("Error", "Username dan Password tidak boleh kosong!")

    root = tk.Tk()
    root.title("Login Kuis")
    root.configure(bg="#d9d9d9")

    tk.Label(root, text="Login", font=("Arial", 20, "bold"), bg="#d9d9d9", fg="#00539C").pack(pady=10)
    tk.Label(root, text="Username:", font=("Arial", 12), bg="#d9d9d9").pack()
    entry_user = tk.Entry(root, font=("Arial", 12))
    entry_user.pack(pady=5)

    tk.Label(root, text="Password:", font=("Arial", 12), bg="#d9d9d9").pack()
    entry_pass = tk.Entry(root, font=("Arial", 12), show="*")
    entry_pass.pack(pady=5)

    tk.Button(root, text="Login", bg="#97c1a9", fg="#ffffff", font=("Arial", 12), command=validate_login).pack(pady=5)
    tk.Button(root, text="Registrasi", bg="#97c1a9", fg="#ffffff", font=("Arial", 12), command=register).pack(pady=5)

    root.mainloop()