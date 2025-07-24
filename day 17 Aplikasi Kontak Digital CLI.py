import os
import json

os.system("cls" if os.name == "nt" else "clear")

class Kontak:
    def __init__(self, nama, no, email):
        self.nama = nama
        self.no = no
        self.email = email
    
    def tampilkan(self):
        print("------------------------")
        print(f"Nama \t: {self.nama}")
        print(f"Nomor \t: {self.no}")
        print(f"Email \t: {self.email}")
        print("------------------------")

NAMA_FILE = "python/30 day python challenge/kontak.json"
daftar_kontak = []

def load_data():
    daftar_kontak.clear()
    try:
        with open(NAMA_FILE, 'r') as f:
            data_kontak = json.load(f)
            for data in data_kontak:
                kontak = Kontak(**data)
                daftar_kontak.append(kontak)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File kontak belum ada, memulai daftar baru.")

def simpan_data():
    data_json = [kontak.__dict__ for kontak in daftar_kontak]
    with open(NAMA_FILE, 'w') as f:
        json.dump(data_json, f, indent=4)
    print("Perubahan berhasil disimpan ke file.")

def tambah_kontak():
    print("\n=== TAMBAH KONTAK BARU ===")
    nama = input("Masukkan Nama: ")
    no = input("Masukkan Nomor: ")
    email = input("Masukkan Email (optional): ")
    
    kontak_baru = Kontak(nama, no, email)
    daftar_kontak.append(kontak_baru)
    simpan_data()

def lihat_kontak():
    print("\n=== DAFTAR SEMUA KONTAK ===")
    if not daftar_kontak:
        print("Daftar kontak masih kosong.")
    else:
        for kontak in daftar_kontak:
            kontak.tampilkan()

def hapus_kontak():
    print("\n=== HAPUS KONTAK ===")
    if not daftar_kontak:
        print("Daftar kontak masih kosong, tidak ada yang bisa dihapus.")
        return

    for i, kontak in enumerate(daftar_kontak, 1):
        print(f"{i}. {kontak.nama}")
    
    try:
        pilihan_str = input("Pilih nomor kontak yang akan dihapus (atau 0 untuk batal): ")
        pilihan = int(pilihan_str)

        if pilihan == 0:
            print("Penghapusan dibatalkan.")
            return

        if 1 <= pilihan <= len(daftar_kontak):
            kontak_dihapus = daftar_kontak.pop(pilihan - 1)
            print(f"Kontak '{kontak_dihapus.nama}' berhasil dihapus.")
            simpan_data()
        else:
            print("Nomor pilihan tidak valid.")
            
    except ValueError:
        print("Input salah, harap masukkan angka.")


load_data()

while True:
    print('''
======================
    MENU KONTAK
======================
1. Tambah Kontak
2. Hapus Kontak
3. Lihat Semua Kontak
4. Keluar
''')
    pilih = input("Pilih Menu: ")

    if pilih == '1':
        tambah_kontak()
    elif pilih == '2':
        hapus_kontak()
    elif pilih == '3':
        lihat_kontak()
    elif pilih == '4':
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")

    input("\nTekan Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")