# LAB-AP-01-2024
# Repositori Tugas Praktikum Algoritma Pemrograman 2024

## Requirements:
Buat akun GitHub (https://github.com/)

## Alur pengumpulan tugas ke repositori ini:

1. **Fork** repositori ini

2. **Clone** repositori hasil **fork** anda

   ```sh

   git clone https://github.com/YOUR_USERNAME/LAB-AP-09-2024.git

   ```


3. Didalam folder NIM kamu, buat sebuah folder dengan nama **Praktikum-n**, **n** = praktikum keberapa
   ```sh

   mkdir "Praktikum-n"
   cd "Praktikum n"

   ```

4. Semua _file_ untuk tugas praktikum ke-**n**, disimpan kedalam folder **Praktikum n**
5. Setiap membuat _file_ atau melakukan perubahan, lakukan proses **commit** dengan pesan yang deskriptif

   ```sh
   git add . #perintah ini memilih seluruh file sekaligus
   # atau
   git add "Praktikum n/NIM/FilePythonYangBerubahAtauDitambahkan.py" #perintah ini memilih file tertentu
   git commit -m "pesan mengenai penambahan atau perubahan apa yang anda lakukan"
   
   ```

6. Setelah asistensi dan tugas anda disetujui, **push** seluruh _file_ jawaban yang telah anda buat

   ```sh

   # pastikan proses commit telah selesai terhadap setiap file
   git push origin NIM_ANDA

   ```
   
   Jika sebelumnya anda belum pernah menghubungkan Git di komputer anda dengan akun GitHub anda, maka anda akan diminta untuk mengisi username dan password untuk
   melakukan push ke repo GitHub anda.
   ```sh

   # username = username anda
   # password = persocal access token anda

   ```
   
   Cara membuat personal access token:
   ```sh
   
   #1. Klik profile anda pada pojok kanan atas GitHub
   #2. Pilih menu settings
   #3. Scroll ke bagian bawah dan pilih menu Dveloper settings
   #4. Pilih Prsonal access tokens
   #5. Pilih Generate new tokes
   #6. Tuliskan note untuk token anda (ex: Token for LAB-AP-09-2024)
   #7. Atur waktu expiration token anda (sesuai keinginan anda)
   #8. Pada select scope, ceklis box repo
   #9. Klik generate new token
   #10. Pastikan untuk meng-copy token anda dan menyimpannya, karena token hanya bisa diliat sekali (*Jika hilang, buat token baru)

   ```
   
7. Masuk ke akun GitHub anda, dan buka repo yang telah anda **fork** dan **clone**. Lihat perubahan yang terjadi pada repo tersebut dan pastikan bahwa tugas yang
   telah anda **push** sesuai dan berada pada repo tersebut.
   
8. Pilih menu **Pull request** dan lakukan **pull request** pada tugas praktikum anda.


## Hal-hal yang harus diperhatikan:

- [x] _**Cara mengumpulkan tugas sesuai dengan aturan diatas**_.
- [x] _**Satu Soal, Satu File**_.
- [x] _**Satu Praktikum, Satu Folder**_.
- [x] _**Program Berjalan dengan Baik dan Benar Berdasarkan Ketentuan Tugas**_.
- [x] _**Tugas Sudah di Asistensikan dan Mendapat Acc**_.
