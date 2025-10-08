print("SELAMAT DATANG DI RESTORAN KARBIT CHAMPIONS")
print(" ")

nama_pelanggan = input("Dengan tuan/nyonya siapa? ")
print(" ")

print('''                Daging rendang-----Rp. 50.000
                Daging rusdi---Rp. 1.500.000
                Paha ambatukam-------Rp. 500.000
                Susu tringgiling------Rp. 1000
''')

pesanan = input(f"Silakan pilih menu yang mau {nama_pelanggan} pesan: ")
print(" ")

iya = "benar"
tidak = "salah"

print("**KONFIRMASI SEBELUM PEMBAYARAN**")
print(f"Pesanan {nama_pelanggan} adalah {pesanan}, apakah benar?")

konfirmasi = input(f'''Silakan ketik salah satu dari opsi berikut ini: 
                {iya}/{tidak}
''')
print(" ")

if konfirmasi == iya:
    print("SYUKURLAH KALAU BEGITU")
else: input('''                Daging asap-----Rp. 50.000
                Daging makima---Rp. 1.500.000
                Paha eula-------Rp. 500.000
                Susu hutao------Rp. 1000
            
            MAAF ATAS KESALAHAN KAMI, SILAKAN PESAN KEMBALI: ''')
print(" ")

print("TERIMA KASIH ATAS PESANAN ANDA, PESANAN ANDA AKAN SEGERA SIAP :)")