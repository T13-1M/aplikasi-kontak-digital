# Aplikasi Kontak Digital (CLI)

Sebuah aplikasi Command-Line Interface (CLI) sederhana yang dibuat dengan Python untuk mengelola daftar kontak pribadi. Aplikasi ini memungkinkan pengguna untuk menambah, melihat, dan menghapus kontak. Semua data disimpan secara lokal dalam format JSON, membuatnya ringan dan mudah dikelola.

Project ini dibuat sebagai bagian dari proses belajar fundamental Python, mencakup manipulasi data, Object-Oriented Programming (OOP), dan operasi file (File I/O).

---

## Fitur Utama

* **Tambah Kontak:** Menyimpan kontak baru (nama, nomor telepon, dan email) ke dalam daftar.
* **Lihat Semua Kontak:** Menampilkan seluruh daftar kontak yang tersimpan dengan format yang rapi.
* **Hapus Kontak:** Menghapus kontak dari daftar berdasarkan pilihan nomor urut yang interaktif.
* **Penyimpanan Permanen:** Data kontak secara otomatis disimpan dalam file `kontak.json`, sehingga tidak akan hilang saat program ditutup dan dibuka kembali.

---

## Cara Menjalankan Aplikasi

1.  Pastikan kamu sudah menginstall Python (versi 3.x direkomendasikan) di komputermu.
2.  *Clone* atau *download* repositori ini ke komputermu.
3.  Buka terminal atau command prompt, lalu navigasi ke direktori tempat kamu menyimpan project ini.
4.  Jalankan script dengan perintah:
    ```bash
    python nama_file_kamu.py
    ```
    *(Ganti `nama_file_kamu.py` dengan nama file Python-mu yang sebenarnya)*
5.  Aplikasi akan berjalan di terminal dan kamu bisa langsung mengikuti instruksi yang muncul di menu.

---

## Struktur File

* **`nama_file_kamu.py`**: File utama yang berisi semua logika aplikasi, mulai dari Class `Kontak` hingga fungsi menu.
* **`kontak.json`**: File database yang akan dibuat dan diperbarui secara otomatis oleh aplikasi. File ini menyimpan semua data kontakmu dalam format JSON.

---

Dibuat dengan semangat belajar Python! 🐍
