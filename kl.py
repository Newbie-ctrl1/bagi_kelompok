import random
import os

def baca_nama_dari_file(nama_file):
    """Membaca nama-nama dari file"""
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            return [nama.strip() for nama in file.readlines() if nama.strip()]
    except FileNotFoundError:
        return []

def bagi_kelompok(nama_list, jumlah_kelompok):
    """Membagi nama-nama menjadi kelompok secara acak"""
    if not nama_list:
        return []
    
    # Mengacak urutan nama
    random.shuffle(nama_list)
    
    # Menghitung jumlah anggota per kelompok
    jumlah_per_kelompok = len(nama_list) // jumlah_kelompok
    sisa = len(nama_list) % jumlah_kelompok
    
    kelompok = []
    indeks = 0
    
    # Membagi nama ke dalam kelompok
    for i in range(jumlah_kelompok):
        ukuran_kelompok = jumlah_per_kelompok + (1 if i < sisa else 0)
        kelompok_baru = nama_list[indeks:indeks + ukuran_kelompok]
        kelompok.append(kelompok_baru)
        indeks += ukuran_kelompok
    
    return kelompok

def simpan_hasil_ke_file(kelompok, output_file):
    """Menyimpan hasil pembagian kelompok ke file"""
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, k in enumerate(kelompok, 1):
            file.write(f"Kelompok {i}:\n")
            for nama in k:
                file.write(f"- {nama}\n")
            file.write("\n")

def main():
    while True:
        # Membersihkan layar
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== Program Pembagi Kelompok Random ===")
        print("\nMenu:")
        print("1. Bagi Kelompok")
        print("2. Keluar")
        
        pilihan = input("\nPilih menu (1/2): ")
        
        if pilihan == '1':
            # Membaca nama dari file
            nama_list = baca_nama_dari_file('nama.txt')
            
            if not nama_list:
                print("\nError: File nama.txt tidak ditemukan atau kosong!")
                input("\nTekan Enter untuk melanjutkan...")
                continue
            
            # Meminta input jumlah kelompok
            while True:
                try:
                    jumlah_kelompok = int(input("\nMasukkan jumlah kelompok yang diinginkan: "))
                    if jumlah_kelompok <= 0:
                        print("Jumlah kelompok harus lebih dari 0!")
                        continue
                    if jumlah_kelompok > len(nama_list):
                        print("Jumlah kelompok tidak boleh lebih besar dari jumlah nama!")
                        continue
                    break
                except ValueError:
                    print("Masukkan angka yang valid!")
            
            # Membagi kelompok
            hasil_kelompok = bagi_kelompok(nama_list, jumlah_kelompok)
            
            # Menyimpan hasil ke file
            simpan_hasil_ke_file(hasil_kelompok, 'kelompok.txt')
            
            print("\nPembagian kelompok berhasil!")
            print("Hasil telah disimpan di file 'kelompok.txt'")
            
            # Menampilkan preview hasil
            print("\nPreview hasil pembagian:")
            for i, kelompok in enumerate(hasil_kelompok, 1):
                print(f"\nKelompok {i}:")
                for nama in kelompok:
                    print(f"- {nama}")
            
            input("\nTekan Enter untuk melanjutkan...")
        
        elif pilihan == '2':
            print("\nTerima kasih telah menggunakan program ini!")
            break
        
        else:
            print("\nPilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()