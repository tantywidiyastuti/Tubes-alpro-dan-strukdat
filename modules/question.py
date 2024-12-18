import tkinter as tk
from tkinter import messagebox, simpledialog
from modules.utils import load_data, save_data, simpan_soal
from modules.leaderboard import update_leaderboard, show_leaderboard
import json

DATA_FILE = "data_soal.json"
USER_FILE = "data_user.json"
BACKUP_FILE = "backup_soal.json"
LEADERBOARD_FILE = "leaderboard.json" 

# Function to load questions
def load_data():
    default_data = [
        {"soal": "Urutan bilangan dari yang terkecil hingga yang terbesar adalah…",
         "pilihan": ["10, 9, 8, 7, 6", "4, 5, 6, 7, 8", "3, 5, 9, 8, 7", "1, 2, 3, 4"], "jawaban": "B"},
        {"soal": "Setelah bilangan 7 adalah…",
         "pilihan": ["3", "8", "10", "11"], "jawaban": "B"},
        {"soal": "Urutan bilangan dari yang terbesar adalah…",
         "pilihan": ["7, 4, 5, 8, 9", "5, 6, 7, 8, 9", "10, 9, 8, 7, 6", "10, 9, 8, 5"], "jawaban": "C"},
        {"soal": "Urutan bilangan yang tepat adalah…",
         "pilihan": ["2, 4, 8, 6, 9", "3, 4, 5, 6, 7", "4, 7, 3, 8, 10", "5, 7, 9, 10,"], "jawaban": "B"},
        {"soal": "35 dibaca…",
         "pilihan": ["Tiga lima", "Tiga dan lima", "Tiga puluh lima", "Tiga atau lima"], "jawaban": "C"},
        {"soal": "Bilangan yang lebih besar dari 32 dan lebih kecil dari 35 adalah…",
         "pilihan": ["33 dan 34", "31 dan 36", "32 dan 35", "31 dan 33"], "jawaban": "A"},
        {"soal": "Sebuah kotak berisi 45 bungkus mie instan. Ibu mengambil 22 bungkus mie instan dari kotak tersebut. Sisa mie instan di dalam kotak adalah…",
         "pilihan": ["33", "23", "13", "24"], "jawaban": "B"},
        {"soal": "Banyaknya nilai satuan dari 38 adalah…",
         "pilihan": ["3", "0", "8", "1"], "jawaban": "C"},
        {"soal": "…. + 10 = 10 + 53",
         "pilihan": ["63", "53", "10", "35"], "jawaban": "B"},
        {"soal": "Siapakah penemu bola lampu?",
         "pilihan": ["Alexander Graham Bell", "Nikola Tesla", "Thomas Edison", "Albert Einstein"], "jawaban": "C"}
    ]
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        save_data(default_data)
        return default_data


# Function to save questions to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to backup questions to a separate file using a loop
def simpan_backup_loop(data, file):
    file.write("[\n")  # Awal array JSON
    for index, item in enumerate(data):
        json.dump(item, file, indent=4)
        if index < len(data) - 1:
            file.write(",\n")  # Tambahkan koma kecuali untuk elemen terakhir
    file.write("\n]")  # Akhir array JSON

def simpan_soal(data):
    try:
        with open(BACKUP_FILE, "w") as file:
            simpan_backup_loop(data, file)
        messagebox.showinfo("Sukses", f"Soal berhasil disimpan di {BACKUP_FILE}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan soal: {e}")

# Function to display questions using a loop
def tampilkan_soal_loop(soal_list):
    index = 0
    while index < len(soal_list):
        soal = soal_list[index]
        messagebox.showinfo(
            f"Soal {index + 1}",
            f"{soal['soal']}\n"
            f"A. {soal['pilihan'][0]}\n"
            f"B. {soal['pilihan'][1]}\n"
            f"C. {soal['pilihan'][2]}\n"
            f"D. {soal['pilihan'][3]}"
        )
        index += 1

def main_menu(username):
    data = load_data()

    def tambah_soal():
        soal = simpledialog.askstring("Tambah Soal", "Masukkan soal baru:")
        if soal:
            pilihan = [simpledialog.askstring("Tambah Pilihan", f"Pilihan {chr(65+i)}:") for i in range(4)]
            jawaban = simpledialog.askstring("Jawaban", "Huruf jawaban yang benar (A-D):").upper()
            if jawaban in ['A', 'B', 'C', 'D']:
                data.append({"soal": soal, "pilihan": pilihan, "jawaban": jawaban})
                save_data(data)
                messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")

    def hapus_soal():
        tampilkan_soal()
        nomor = simpledialog.askinteger("Hapus Soal", "Masukkan nomor soal yang ingin dihapus:")
        if nomor and 1 <= nomor <= len(data):
            data.pop(nomor - 1)
            save_data(data)
            messagebox.showinfo("Sukses", "Soal berhasil dihapus!")

    def edit_soal():
        tampilkan_soal()
        nomor = simpledialog.askinteger("Edit Soal", "Masukkan nomor soal yang ingin diedit:")
        if nomor and 1 <= nomor <= len(data):
            soal = data[nomor - 1]
            new_soal = simpledialog.askstring("Edit Soal", "Perbarui soal:", initialvalue=soal['soal'])
            pilihan = [
                simpledialog.askstring(f"Edit Pilihan {chr(65+i)}", f"Perbarui pilihan {chr(65+i)}:", initialvalue=soal['pilihan'][i]) 
                for i in range(4)
            ]
            new_jawaban = simpledialog.askstring("Edit Jawaban", "Perbarui jawaban (A-D):", initialvalue=soal['jawaban']).upper()
            
            if new_jawaban in ['A', 'B', 'C', 'D']:
                data[nomor - 1] = {"soal": new_soal, "pilihan": pilihan, "jawaban": new_jawaban}
                save_data(data)
                messagebox.showinfo("Sukses", "Soal berhasil diperbarui!")

    def simpan_soal_handler():
        simpan_soal(data)

    def tampilkan_soal():
        if data:
            tampilkan_soal_loop(data)
        else:
            messagebox.showinfo("Daftar Soal", "Tidak ada soal yang tersedia.")

    def mulai_kuis():
        skor = 0
        for i, soal in enumerate(data):
            pilihan = "\n".join([f"{chr(65+j)}. {p}" for j, p in enumerate(soal['pilihan'])])
            jawaban = simpledialog.askstring(
                f"Soal {i+1}", f"{soal['soal']}\n{pilihan}\n\nMasukkan jawaban Anda (A-D):"
            ).upper()
            if jawaban == soal['jawaban']:
                skor += 1

        messagebox.showinfo("Hasil Kuis", f"Kuis selesai! Skor Anda: {skor}/{len(data)}")