def geser_teks(teks, pergeseran):
    teks_enkripsi = ""

    for karakter in teks:
        if karakter.islower():
            karakter_enkripsi = chr((ord(karakter) - ord('a') + pergeseran) % 26 + ord('a'))
            teks_enkripsi += karakter_enkripsi
        elif karakter.isupper():
            karakter_enkripsi = chr((ord(karakter) - ord('A') + pergeseran) % 26 + ord('A'))
            teks_enkripsi += karakter_enkripsi
        else:
            teks_enkripsi += karakter

    return teks_enkripsi

input_teks = input("Masukkan string: ")
pergeseran_jumlah = int(input("Masukkan jumlah pergeseran (bilangan bulat positif): "))
hasil = geser_teks(input_teks, pergeseran_jumlah)
print("Hasil enkripsi:", hasil)



