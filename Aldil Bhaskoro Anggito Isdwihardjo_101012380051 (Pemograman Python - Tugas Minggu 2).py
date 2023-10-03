'''
Nama : Aldil Bhaskoro Anggito Isdwihardjo
NIM  : 101012380051
Tugas Minggu 2 Pemograman Python
'''

'''
Soal No. 1
Buatlah program untuk menghitung volume dan luas permukaan dari 
tabung dengan menggunakan inputan nilai (pi=3.14).
'''
# Penyelesaiannya sebagai berikut
def hitung_volume_tabung(radius, tinggi):
    volume = 3.14 * radius * radius * tinggi
    return volume

# Fungsi untuk menghitung luas permukaan tabung
def hitung_luas_permukaan_tabung(radius, tinggi):
    luas_permukaan = 2 * 3.14 * radius * (radius + tinggi)
    return luas_permukaan

# Input nilai radius/jari-jari dan tinggi
radius = float(input("Masukkan nilai jari-jari tabung: "))
tinggi = float(input("Masukkan nilai tinggi tabung: "))

# Menghitung volume dan luas permukaan tabung
volume = hitung_volume_tabung(radius, tinggi)
luas_permukaan = hitung_luas_permukaan_tabung(radius, tinggi)

# Menampilkan hasil pada terminal
print("Volume tabung:", volume)
print("Luas permukaan tabung:", luas_permukaan)


'''
Soal No. 2
Buatlah program untuk melakukan check apakah bilangan tersebut lebih dari sama 
dengan 10 sampai kurang dari sama dengan 20 dan juga bilangan genap.
'''
# Penyelesaiannya sebagai berikut
def verifikasi_bilangan(bilangan):
    ''''
    Fungsi untuk melakukan verifikasi apakah bilangan lebih dari sama dengan 10
    hingga kurang dari sama dengan 20 dan merupakan bilangan genap.

    Parameters:
    bilangan (int): Bilangan yang akan diverifikasi.

    Returns:
    bool: True jika memenuhi kriteria, False jika tidak.
    '''
    if bilangan >= 10 and bilangan <= 20 and bilangan % 2 == 0:
        return True
    else:
        return False

# Input nilai dari pengguna
bilangan_input = int(input("Masukkan sebuah bilangan: "))

# Memanggil fungsi verifikasi_bilangan
if verifikasi_bilangan(bilangan_input):
    print(f"{bilangan_input} adalah bilangan genap dan berada di antara 10 hingga 20.")
else:
    print(f"{bilangan_input} bukan bilangan antara 10 sampai 20 atau bilangan ganjil.")
