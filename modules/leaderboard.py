from utils import load_json, save_json
from tkinter import messagebox

LEADERBOARD_FILE = "leaderboard.json"

# Fungsi untuk memuat leaderboard
def load_leaderboard():
    return load_json(LEADERBOARD_FILE, default_data={})

# Fungsi untuk menyimpan leaderboard
def save_leaderboard(leaderboard):
    save_json(LEADERBOARD_FILE, leaderboard)

# Fungsi untuk menampilkan leaderboard
def display_leaderboard(username=None):
    leaderboard = load_leaderboard()
    if not leaderboard:
        messagebox.showinfo("Leaderboard", "Leaderboard kosong. Mulai kuis untuk menambahkan skor!")
        return

    if username:
        # Menampilkan skor user tertentu
        user_scores = leaderboard.get(username, [])
        if user_scores:
            messagebox.showinfo("Leaderboard", f"{username}: {max(user_scores)} (Skor tertinggi)")
        else:
            messagebox.showinfo("Leaderboard", f"{username}: Belum memiliki skor.")
    else:
        # Menampilkan seluruh leaderboard
        leaderboard_str = "\n".join(
            [f"{user}: {max(scores)} (Skor tertinggi)" for user, scores in leaderboard.items()]
        )
        messagebox.showinfo("Leaderboard", f"Leaderboard:\n\n{leaderboard_str}")

# Fungsi untuk memperbarui skor user di leaderboard
def update_leaderboard(username, score):
    leaderboard = load_leaderboard()
    if username in leaderboard:
        leaderboard[username].append(score)
    else:
        leaderboard[username] = [score]
    save_leaderboard(leaderboard)
    messagebox.showinfo("Leaderboard", "Skor Anda berhasil disimpan!")
