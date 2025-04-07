# Buku Tamu Digital

Aplikasi Buku Tamu Digital adalah aplikasi berbasis Streamlit yang dirancang untuk mencatat data pengunjung secara digital. Data yang diinput (nama, email, dan komentar) akan disimpan ke Firebase Firestore dan ditampilkan dalam bentuk tabel.

## Fitur
- **Input Data Pengunjung:**  
  Pengguna dapat mengisi form dengan informasi seperti nama, email, dan komentar.
- **Penyimpanan Data:**  
  Data yang dimasukkan langsung dikirim ke Firebase Firestore menggunakan Firebase Admin SDK.
- **Tampilan Data:**  
  Data pengunjung yang telah disimpan ditampilkan dalam bentuk tabel rapi di halaman aplikasi.
- **Reset Form Otomatis:**  
  Form input akan otomatis di-reset setelah data berhasil dikirim.

## Prasyarat
- **Python 3:** Pastikan Python versi 3.7 ke atas sudah terinstall.
- **Git:** Untuk mengelola dan mengunggah kode ke GitHub.
- **Akun Firebase:** Untuk mengkonfigurasi Firestore dan mendapatkan file kredensial.
- **Akun GitHub:** Untuk menyimpan repository kode.

## Instalasi & Persiapan
1. **Clone Repository:**  
   Jika sudah diupload ke GitHub, clone repository dengan:
   ```bash
   git clone https://github.com/username/web-buku-tamu-digital.git
   cd buku-tamu-digital
2. **Buat Virtual Environment (Opsional):**
   Membuat virtual environment sangat disarankan:
python -m venv venv

- Aktifkan virtual environment:
    - Windows:
    venv\Scripts\activate
    - Linux/Mac:
    source venv/bin/activate

3. **Install Dependencies:**
Pastikan file requirements.txt sudah ada di folder project. Lalu, jalankan:
pip install -r requirements.txt

## Konfigurasi Firebase
1. **File Kredensial:**
   - Dapatkan file JSON kredensial Firebase Admin SDK dari Firebase Console.
   - Simpan file tersebut di root folder project dengan nama misalnya:
     buku-tamu-web-firebase-adminsdk-fbsvc-44b290c091.json

2. **Keamanan File Kredensial:**
   File kredensial bersifat rahasia. Jangan commit file ini ke repository publik!
   Untuk menghindarinya, tambahkan baris berikut pada file .gitignore:
   *.json
   Pastikan file kredensial tidak ikut ter-upload ke GitHub.

## Menjalankan Aplikasi
Setelah instalasi dan konfigurasi selesai, jalankan aplikasi dengan perintah:
streamlit run app.py
Aplikasi akan terbuka di browser, dan kamu dapat mulai mengisi form Buku Tamu Digital.

## Deployment
Aplikasi ini dapat dideploy menggunakan berbagai platform, antara lain:
- **Streamlit Community Cloud:**  
  Upload repository ke GitHub dan deploy melalui [Streamlit Community Cloud](https://share.streamlit.io/).

- **Heroku:**
  - Buat file `Procfile` di root folder project dengan isi:
    ```Procfile
    web: streamlit run app.py --server.port=$PORT
    ```
  - Lalu deploy ke Heroku menggunakan Git.

- **Platform Lain:**
  Kamu juga dapat menggunakan layanan seperti AWS, Google Cloud, atau Docker untuk deployment.

## Struktur Proyek

```bash
buku-tamu-digital/
├── app.py                         # Kode utama aplikasi
├── buku-tamu-web-firebase-adminsdk-fbsvc-44b290c091.json   # File kredensial Firebase (JANGAN commit file ini ke repository publik!)
├── requirements.txt               # Daftar dependencies
├── .gitignore                     # Daftar file/extension yang diabaikan oleh Git
└── README.md                      # Dokumentasi proyek
```

## Catatan
- **Keamanan:**  
  Pastikan file kredensial diatur dengan benar dan tidak disimpan di repository publik.

- **Firebase:**  
  Sebelum menjalankan aplikasi, pastikan Firestore sudah diaktifkan dan dikonfigurasi pada project Firebase kamu.

- **Testing:**  
  Lakukan testing secara lokal sebelum deployment untuk memastikan aplikasi berjalan dengan baik.

© 2025 Daffa Asyqar. All rights reserved.
