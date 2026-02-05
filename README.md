# 🔧 Sistem Pakar Diagnosis Kerusakan Handphone

Sistem pakar untuk mendiagnosis kerusakan handphone menggunakan metode **Forward Chaining** berbasis Python dengan GUI Tkinter.

## 📋 Deskripsi

Sistem ini merupakan implementasi dari jurnal penelitian **"Sistem Pakar Untuk Kerusakan Handphone Dengan Metode Forward Chaining"** oleh Dilla Kusumawati, Fanisya Alva Mustika, dan Ni Wayan Parwati Septiani (JRKT Vol 03 No 04 Tahun 2023).

Sistem dapat mendiagnosis 6 jenis kerusakan handphone berdasarkan 28 gejala yang dialami menggunakan algoritma Forward Chaining.

## ✨ Fitur

- ✅ Diagnosis 6 jenis kerusakan handphone
- ✅ 28 gejala kerusakan yang dapat dipilih
- ✅ Metode Forward Chaining untuk inferensi
- ✅ Perhitungan Confidence Level (%)
- ✅ Multiple diagnosis output
- ✅ Antarmuka GUI modern dengan Tkinter
- ✅ Solusi dan rekomendasi penanganan

## 🛠️ Jenis Kerusakan yang Dapat Didiagnosis

| Kode | Kerusakan | Jumlah Gejala |
|------|-----------|---------------|
| T1 | IC Power | 6 gejala |
| T2 | IC Emmc | 6 gejala |
| T3 | Baterai Drop | 7 gejala |
| T4 | LCD Rusak | 7 gejala |
| T5 | IC PA (Power Amplifier) | 6 gejala |
| T6 | IC Charging | 3 gejala |

## 🚀 Cara Menjalankan

### Requirement
- Python 3.x
- Tkinter (biasanya sudah built-in di Python)

### Instalasi

1. Clone repository ini
```bash
git clone https://github.com/[username]/Sistem-Pakar-Kerusakan-Handphone.git
cd Sistem-Pakar-Kerusakan-Handphone
```

2. Jalankan aplikasi
```bash
main.py
```

## 📖 Cara Penggunaan

1. **Buka Aplikasi** - Jalankan file `main.py`
2. **Klik "Mulai Diagnosa"** - Masuk ke halaman diagnosis
3. **Pilih Gejala** - Centang gejala yang dialami handphone (minimal 1)
4. **Klik "Diagnosa Sekarang"** - Sistem akan memproses dengan Forward Chaining
5. **Lihat Hasil** - Sistem menampilkan diagnosis dengan confidence level dan solusi
6. **Diagnosa Lagi** - Dapat melakukan diagnosis ulang dengan gejala berbeda

## 🧠 Metode Forward Chaining

Forward Chaining adalah metode inferensi yang bekerja dengan:
1. Menerima input gejala dari pengguna
2. Mencocokkan gejala dengan aturan dalam basis pengetahuan
3. Menghitung confidence level: `(Gejala Cocok / Total Gejala) × 100%`
4. Mengurutkan hasil dari confidence tertinggi
5. Menampilkan semua kemungkinan diagnosis

```

## 📚 Referensi

Kusumawati, D., Mustika, F. A., & Septiani, N. W. P. (2023). Sistem Pakar Untuk Kerusakan Handphone Dengan Metode Forward Chaining. *JRKT (Jurnal Rekayasa Komputasi Terapan)*, 03(04), 186-192.

