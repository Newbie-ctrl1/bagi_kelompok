# Program Pembagi Kelompok Random

Program ini dibuat untuk membagi daftar nama ke dalam beberapa kelompok secara acak. Nama-nama dibaca dari sebuah file teks `nama.txt`, dan hasil pembagian kelompok disimpan dalam file lain `kelompok.txt`. Program ini cocok digunakan dalam situasi seperti membagi peserta ke dalam kelompok diskusi, tim proyek, atau kelompok permainan.

## Fitur
  - Membaca daftar nama dari file nama.txt.
  - Mengacak dan membagi nama-nama ke dalam kelompok.
  - Menyimpan hasil pembagian kelompok ke file kelompok.txt.
  - Menampilkan preview hasil pembagian di terminal.

## Persyaratan Sistem
  - Python 3.x
  - File nama.txt yang berisi daftar nama yang akan dibagi (satu nama per baris).

## Cara Menggunakan
1. Persiapan File Nama
Buat file teks bernama nama.txt di folder yang sama dengan program ini. Isi file tersebut dengan daftar nama, satu nama per baris, contohnya:

```
  Alice
  Bob
  Charlie
  David
  Eve
```

2. Menjalankan Program
  - Buka terminal atau command prompt.
  - Jalankan program dengan perintah berikut:
```
  php
  python kl.py
```
3. Menu Program
Setelah menjalankan program, Anda akan melihat menu dengan dua pilihan:

  - Pilih 1 untuk membagi nama ke dalam kelompok.
  - Pilih 2 untuk keluar dari program.

4. Pembagian Kelompok
Setelah memilih opsi pembagian kelompok, program akan meminta Anda untuk memasukkan jumlah kelompok yang diinginkan. Pastikan jumlah kelompok tidak melebihi jumlah nama yang tersedia.

Setelah pembagian selesai, hasilnya akan disimpan dalam file `kelompok.txt`, dan program juga akan menampilkan preview hasil pembagian di layar.

Contoh Output
File kelompok.txt akan terlihat seperti berikut:
```
  diff
  Kelompok 1:
  - Alice
  - David

  Kelompok 2:
  - Bob
  - Charlie
  - Eve
```

## Error Handling
Jika file nama.txt tidak ditemukan, program akan menampilkan pesan error dan meminta Anda untuk menekan Enter untuk melanjutkan.
Program akan meminta Anda untuk memasukkan jumlah kelompok yang valid (lebih dari 0 dan tidak melebihi jumlah nama).

## Lisensi
Program ini dapat digunakan dan dimodifikasi sesuai kebutuhan.

