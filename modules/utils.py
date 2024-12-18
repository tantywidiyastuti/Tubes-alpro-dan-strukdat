import json
import os
from tkinter import messagebox

# File paths
DATA_FILE = "data/data_soal.json"
USER_FILE = "data/data_user.json"
BACKUP_FILE = "data/backup_soal.json"
LEADERBOARD_FILE = "data/leaderboard.json"

# Generic file handling functions
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def simpan_soal(data):
    try:
        with open(BACKUP_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan soal: {e}")

def load_accounts():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"admin": "1234"}  # Default account

def save_accounts(accounts):
    with open(USER_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)
