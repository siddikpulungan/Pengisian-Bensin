# Pengisian-Bensin
## Identitas
- Nama : AULIA SIDDIK PULUNGAN
- NPM  : 2410017514009
- Kelas: A1

  ### Studi kasus
  -Program ini dibuat untuk mensimulasikan pengisian bahan bakar di Pom Bensin.
  -Pengguna dapat memilih jenis bahan bakar yaitu Pertalite atau Pertamax,kemudian memasukkan jumlah liter yang ingin
   dibeli.
  -Program akan menghitung total harga pembelian berdasarkan harga per liter dari masing-masing jenis bensin, lalu
   menampilkan struk pembelian secara otomatis.
  -Selain itu, program memberikan kesempatan kepada pengguna untuk mengulang pengisian tanpa perlu menutup program
   terlebih dahulu.

  #### Fitur Program
  [1] Meminta input jenis bensin dari pengguna (Pertalite atau Pertamax).
  [2] Meminta input jumlah liter dengan validasi minimal 1 liter.
  [3] Menghitung total harga sesuai dengan jenis bensin yang dipilih.
  [4] Menampilkan hasil transaksi dalam bentuk struk pembelian.
  [5] Menawarkan opsi untuk melakukan transaksi ulang atau keluar dari program.

  #####Teknik yang Digunakan
  -Input → Untuk menerima jenis bensin dan jumlah liter dari pengguna.
  -While Loop → Untuk mengulang proses selama pengguna ingin melakukan
   pengisian bensin lagi.
  -Do-While Pattern → Diterapkan dengan struktur while True: yang memastikan
   program berjalan minimal satu kali sebelum dicek kondisi keluar.
  -For Loop → Tidak digunakan pada program ini.
  -Nesting If → Untuk memvalidasi jenis bensin dan jumlah liter di dalam
   perulangan utama.
  
######Screenshot Output

  <img width="1138" height="845" alt="Cuplikan layar 2025-11-08 110939" src="https://github.com/user-attachments/assets/bcb9736c-4361-4054-ab14-e2c8a0182b18" />

  #######Cara Menjalankan
 1. Simpan file dengan nama: PomBensin.py
 2. Jalankan program menggunakan terminal atau CMD:
    python PomBensin.py
3.  Ikuti instruksi input sesuai perintah di layar (masukkan jenis bensin,
    jumlah liter, dan konfirmasi pengulangan).
