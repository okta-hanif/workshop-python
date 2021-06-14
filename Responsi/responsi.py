import crudfunc as fun

menu = 1
while menu>=0 and menu<=4:
    #  MENU UTAMA
    print("=== Menu Informasi Mahasiswa ===")
    print("1    Masukkan data baru ")
    print("2    Tampilkan data ")
    print("3    Perbaharui data ")
    print("4    Hapus data")
    print("0    Selesai (Keluar) ")
    menu = int(input("[P]ilihan : "))
    print('')

    if menu== 1:
        print("=== MEMASUKKAN DATA BARU ===")
        nim = input("NIM : ")
        nama = input("Nama : ")
        prodi = input("Prodi : ")
        ipk = float(input("IPK : "))
        #funtion dari file crudfunc
        fun.masukkan_data(nim,nama,prodi,ipk)
        print(" >> Sukses Memasukkan Data!! ") 
        print('')

    elif menu== 2:
        print("=== MENAMPILKAN DATA ===")
        nim = input("Masukkan NIM data yang akan ditampilkan : ")
        print('')
        fun.baca_data(nim)
        print('')

    elif menu== 3:
        print("=== MEMPERBARUI DATA ===")
        nim = input("Masukkan NIM data yang akan diperbarui : ")
        nama = input("Nama baru : ")
        prodi = input("Prodi baru : ")
        ipk = float(input("IPK baru : "))
        fun.perbarui_data(nim,nama,prodi,ipk)
        print(" >> Sukses Memperbarui Data!! ")
        print('')

    elif menu== 4 :
        print("=== MENGHAPUS DATA ===")
        nim = input("Masukkan NIM data yang akan di[HAPUS] : ")
        fun.hapus_data(nim)
        print(" >> Sukses Menghapus Data!! ")
        print('')
    
    elif menu== 0:
        print("*** KELUAR DARI PROGRAM ***")
        print('')
        break
else:
  print("[ERROR!] HANYA MENERIMA INPUT SESUAI MENU!!! ")



