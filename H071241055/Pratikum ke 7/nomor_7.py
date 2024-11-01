import os
import time

# Paths for storing film and ticket files
FILM_FILE_PATH = r"c:\ngoding\Tugas lab\Tugas Pratikum\LAB-AP-01-2024\H071241055\Pratikum ke 7\daftar_film.txt"
TICKET_FILE_PATH = r"c:\ngoding\Tugas lab\Tugas Pratikum\LAB-AP-01-2024\H071241055\Pratikum ke 7\tiket_film.txt"

# Ensure directory exists
os.makedirs(os.path.dirname(FILM_FILE_PATH), exist_ok=True)

def menu_utama():
    while True:
        print("""\n--- Sistem Pemesanan Tiket Bioskop ---
1. Admin
2. Pengunjung
3. Keluar""")
        
        try:
            pesanan = int(input("Pilih opsi (1-3): "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka 1-3.")
            continue

        if pesanan == 1:
            admin()
        elif pesanan == 2:
            pengunjung()
        elif pesanan == 3:
            print("Terima kasih telah mengunjungi kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")

def admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")

        try:
            opsi = int(input("Pilih opsi (1-4): "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka 1-4.")
            continue

        if opsi == 1:
            tambah_film()
        elif opsi == 2:
            hapus_film()
        elif opsi == 3:
            daftar_ticket()
        elif opsi == 4:
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")

def tambah_film():
    nama_film = input("Masukkan nama film yang ingin ditambahkan (atau klik enter untuk kembali): ").strip()
    if not nama_film:
        return

    # Check if film already exists in daftar_film.txt
    if os.path.exists(FILM_FILE_PATH):
        with open(FILM_FILE_PATH, "r") as file:
            films = file.readlines()
            if any(nama_film in line for line in films):
                print(f"Film '{nama_film}' sudah ada.")
                return

    # Add the new film to daftar_film.txt
    try:
        with open(FILM_FILE_PATH, "a") as file:
            file.write(f"{nama_film}\n")
        print("Film berhasil ditambahkan.")
    except IOError as e:
        print(f"Terjadi kesalahan saat menambahkan film: {e}")

def hapus_film():
    hapus = input("Masukkan nama film yang ingin dihapus (atau enter untuk kembali): ").strip()
    if not hapus:
        return

    if not os.path.exists(FILM_FILE_PATH):
        print("Daftar film tidak ditemukan.")
        return

    # Remove the specified film from daftar_film.txt
    try:
        with open(FILM_FILE_PATH, "r") as file:
            films = file.readlines()
        
        with open(FILM_FILE_PATH, "w") as file:
            found = False
            for film in films:
                if film.strip() != hapus:
                    file.write(film)
                else:
                    found = True

        if found:
            print(f"Film '{hapus}' berhasil dihapus.")
        else:
            print("Film tidak ditemukan.")
    except IOError as e:
        print(f"Terjadi kesalahan saat menghapus film: {e}")

def daftar_ticket():
    print("\nDaftar Tiket:")
    # Cek jika file tiket ada dan tidak kosong
    if not os.path.exists(TICKET_FILE_PATH) or os.stat(TICKET_FILE_PATH).st_size == 0:
        print("Belum ada tiket yang dipesan.")
        return

    try:
        with open(TICKET_FILE_PATH, "r") as file:
            tickets = file.readlines()
            
        if not tickets:
            print("Tidak ada tiket yang tersedia.")
        else:
            for ticket in tickets:
                print(ticket.strip())
    except FileNotFoundError:
        print("File tiket tidak ditemukan.")


def pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Lihat Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")

        try:
            opsi = int(input("Pilih opsi (1-3): "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka 1-3.")
            continue

        if opsi == 1:
            lihat_film()
        elif opsi == 2:
            beli_tiket()
        elif opsi == 3:
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")

def lihat_film():
    if not os.path.exists(FILM_FILE_PATH):
        print("Daftar film tidak ditemukan.")
        return

    print("\nDaftar Film:")
    with open(FILM_FILE_PATH, "r") as file:
        films = file.readlines()
        if not films:
            print("Tidak ada film yang tersedia.")
        else:
            for index, film in enumerate(films, start=1):
                print(f"{index}. {film.strip()}")

def beli_tiket():
    lihat_film()
    if not os.path.exists(FILM_FILE_PATH):
        print("Daftar film tidak ditemukan.")
        return

    films = []
    with open(FILM_FILE_PATH, "r") as file:
        films = file.readlines()
    
    try:
        beli = int(input("Pilih nomor film yang ingin dibeli (atau 0 untuk kembali): "))
        if beli == 0:
            return
        if 1 <= beli <= len(films):
            film_terpilih = films[beli - 1].strip()
            time_sekarang = time.strftime("%d%m%Y%H%M%S", time.localtime())
            id_tiket = f"TICK{time_sekarang}"
            ticket_line = f"Film: {film_terpilih} | ID Tiket: {id_tiket} | Tanggal: {time.strftime('%d-%m-%Y %H:%M:%S')}\n"

            # Append the new ticket to tiket_film.txt
            with open(TICKET_FILE_PATH, "a") as f:
                f.writelines(ticket_line)
                
            print(f"Tiket berhasil dibeli. ID tiket anda: {id_tiket}")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")

# Start the program
menu_utama()
