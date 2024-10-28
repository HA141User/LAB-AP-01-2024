penyimpanan = {}

# Fungsi untuk menambah barang
def tambah_barang():
    try:
        kode = int(input("Masukkan kode: "))
        
        if kode in penyimpanan:
            print("Kode sudah ada, masukkan kode lain.")
            return
        
        nama = input("Masukkan nama: ")
        jumlah = int(input("Masukkan jumlah: "))
        harga = float(input("Masukkan harga per unit: "))
            
        penyimpanan[kode] = {
            "nama": nama,
            "jumlah": jumlah,
            "harga": harga
        }
        print("Barang berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka untuk kode, jumlah, dan harga.")

# Fungsi untuk menghapus barang
def hapus_barang(): 
    try:
        hapus = int(input("Masukkan kode barang yang ingin dihapus: "))
        if hapus in penyimpanan:
            del penyimpanan[hapus]
            print("Barang berhasil dihapus.")
        else:
            print("Kode tidak ada.")
    except ValueError:
        print("Input tidak valid. Masukkan kode dalam bentuk angka.")

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    if penyimpanan:
        print("\n=== Daftar Barang ===")
        for kode, barang in penyimpanan.items():
            print(f"Kode: {kode}")
            print(f"Nama: {barang['nama']}")
            print(f"Jumlah: {barang['jumlah']}")
            print(f"Harga per unit: {barang['harga']}")
            print("\n")
    else:
        print("Tidak ada barang dalam penyimpanan.")

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang():
    try:
        cari = int(input("Masukkan kode barang yang ingin dicari: "))
        if cari in penyimpanan:
            barang = penyimpanan[cari]
            print("\n=== Barang Ditemukan ===")
            print(f"Kode: {cari}")
            print(f"Nama: {barang['nama']}")
            print(f"Jumlah: {barang['jumlah']}")
            print(f"Harga per unit: {barang['harga']}")
            print("\n")
        else:
            print("Barang tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Masukkan kode dalam bentuk angka.")

# Fungsi untuk memperbarui barang
def update_barang():
    try:
        kode = int(input("Masukkan kode barang yang ingin diupdate: "))
        if kode in penyimpanan:
            barang = penyimpanan[kode]
            
            jumlah_baru = int(input("Masukkan jumlah unit baru: "))
            harga_baru = float(input("Masukkan harga baru per unit: "))
            
            barang["jumlah"] = jumlah_baru
            barang["harga"] = harga_baru
            print("Barang berhasil diupdate.")
        else:
            print("Barang tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk jumlah dan harga.")

# Fungsi untuk menampilkan menu dan menangani pilihan pengguna
def menu():
    while True:
        print("\n=== Menu Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        
        try:
            opsi = int(input("Pilih opsi 1-6: "))
            if opsi == 1:
                tambah_barang()
            elif opsi == 2:
                hapus_barang()
            elif opsi == 3:
                tampilkan_barang()
            elif opsi == 4:
                cari_barang()
            elif opsi == 5:
                update_barang()
            elif opsi == 6:
                print("Keluar dari program.")
                break
            else:
                print("Opsi tidak valid. Silakan pilih opsi yang tersedia.")
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1 dan 6.")

# Jalankan menu
menu()
