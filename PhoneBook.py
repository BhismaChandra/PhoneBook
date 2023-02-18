#Program PhoneBook.py

import os

#Menu Awal
while True:
    print("========PHONEBOOK========")
    print("1. Tampilkan Isi Kontak")
    print("2. Tambahkan Nomor Baru")
    print("3. Cari Satu Nomor")
    print("4. Ubah Satu Nomor")
    print("5. Hapus Satu Nomor")
    print("(selain) Keluar")
    opsi = input("Pilih Opsi: ")
    if opsi == '1':
        #cek apakah file ada
        if os.path.exists("PhoneBook.txt"):
            #jika ada, maka baca
            file = open("PhoneBook.txt", "r")
            #cek apakah file masih kosong
            if os.path.getsize("PhoneBook.txt") == 0:
                #jika kosong beri tahu
                print("\nPhone Book Masih Kosong!\n")
            else:
                #jika tidak, tampilkan isi file
                print("\n=====ISI PHONE BOOK=====\n")
                print(file.read())
            file.close()
        else:
        #jika file tidak ada, akan dibuat file
        #"PhoneBook.txt" tanpa isi
            print("\nPhone Book Masih Kosong!\n")
            file = open("PhoneBook.txt", "w")
            file.close()
        
    elif opsi == '2':
    #menambahkan kontak baru
        #minta input nama dan nomor
        nama = input("Nama: ")
        nomor = input("Nomor: ")
        #append baris baru dalam file berisi input
        file = open("PhoneBook.txt", "a")
        file.write(nama + ' ' + nomor+ "\n")
        file.close()
        
    elif opsi == '3':
        # mencari kontak dalam phone book
        # baca yang ingin dicari
        dicari = input("Masukkan nama atau nomor yang dicari: \n")
        # buka file untuk membaca isi
        file = open("PhoneBook.txt", "r")
        # baca isi file per baris
        lines = file.readlines()
        file.close()
        # deklarasi variabel array untuk menyimpan baris yang mengandung input
        new_list = []
        # loop melalui setiap baris dalam file
        for line in lines:
            # jika baris mengandung kata yang dicari, simpan ke dalam list yang baru
            if dicari in line:
                new_list.append(line)
        # jika panjang list baru adalah 0, artinya kata kunci tidak ditemukan dalam file
        if len(new_list) == 0:
            print("\n\"" + dicari + "\" tidak ditemukan\n")
        else:
            # menampilkan baris yang mengandung kata kunci
            print("\nKontak \"" + dicari + "\" ditemukan:")
            for line in new_list:
                print(" ", end=line)
            print()

        
    elif opsi == '4':
        #mengubah isi satu kontak
        sebelum = input("Masukkan nama atau nomor yang ingin diganti:\n")
        setelah = input("Masukkan ingin diganti dengan apa:\n")
    
        # baca file
        file = open("PhoneBook.txt", "r")
        # baca baris yang ingin diubah
        lines = file.readlines()
        file.close()
        # buka kembali file untuk menulis
        with open("PhoneBook.txt", "w") as fw:
            for line in lines:
                # cek apakah baris saat ini mengandung kata yang ingin diubah
                if sebelum in line:
                    # jika iya, ganti kata tersebut dengan kata yang baru
                    line = line.replace(sebelum, setelah)
                # tulis baris ke file
                fw.write(line)
        print("\nData berhasil diubah!\n")

        
    elif opsi == '5':
    # menghapus satu kontak
        # baca file
        file = open("PhoneBook.txt", "r")
        # baca yang ingin dihapus
        dihapus = input("Masukkan nama atau nomor yang ingin dihapus: \n")
        # simpan isi file per baris
        lines = file.readlines()
        file.close()
        # buka kembali file untuk menulis
        with open("PhoneBook.txt", "w") as fw:
            i = 1
            for line in lines:
                if dihapus not in line:
                    fw.write(line)
                    i += 1
        print("\nBerhasil Dihapus!\n")
    
    else:
        print("Keluar Program")
        break
    
