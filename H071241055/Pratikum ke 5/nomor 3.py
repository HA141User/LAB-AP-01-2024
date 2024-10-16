def jumlah_penghapusan_anagram(teks1, teks2):
    frekuensi1 = [0] * 26
    frekuensi2 = [0] * 26
    def indeks_huruf(karakter):
        return 'abcdefghijklmnopqrstuvwxyz'.index(karakter)
    for karakter in teks1:
        if 'a' <= karakter <= 'z':
            frekuensi1[indeks_huruf(karakter)] += 1
    for karakter in teks2:
        if 'a' <= karakter <= 'z':
            frekuensi2[indeks_huruf(karakter)] += 1
    print(frekuensi1)
    print(frekuensi2)
    penghapusan = 0
    for i in range(26):
        penghapusan += abs(frekuensi1[i] - frekuensi2[i])
    return penghapusan

input_teks1 = input("Masukkan string pertama: ").lower()
input_teks2 = input("Masukkan string kedua: ").lower()

hasil = jumlah_penghapusan_anagram(input_teks1, input_teks2)
print("Jumlah minimum karakter yang harus dihapus untuk membuat kedua string menjadi anagram:", hasil)


