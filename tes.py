import pandas as pd

data = {
    "Nama": ["John", "Jane", "Bob", "Alice"],
    "Usia": [25, 35, 30, 28],
    "Gaji": [50000, 60000, 70000, 55000],
}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.

# pertanyaan 1
for i in df["Gaji"]:
    a = lambda bonus: bonus + bonus * 0.5
    print(a(i))


# pertanyaan 2
df["total_bonus"] = df["Gaji"] + df["Gaji"] * 0.5
print(df)

# pertanyaan 3
for i in df["Usia"]:
    if i > 30:
        df["total_bonus"] = df["total_bonus"] + df["total_bonus"] * 0.2

# # pertanyaan 4
print(df)
