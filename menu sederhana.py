# Menu restoran sebagai dictionary
menu = {
    "Daging asap": 50000,
    "Daging makima": 1500000,
    "Paha eula": 500000,
    "Susu hutao": 1000
}

print("SELAMAT DATANG DI RESTORAN KARBIT CHAMPIONS")
print(" ")

# Input nama pelanggan
nama_pelanggan = input("Dengan tuan/nyonya siapa? ")
print(" ")

# Tampilkan menu
print("------ MENU MAKANAN ------")
for item, harga in menu.items():
    print(f"{item:<20} - Rp. {harga:,}")
print(" ")

# Proses pemesanan
while True:
    pesanan = input(f"Silakan pilih menu yang mau {nama_pelanggan} pesan: ")
    print(" ")

    if pesanan in menu:
        print("**KONFIRMASI SEBELUM PEMBAYARAN**")
        print(f"Pesanan {nama_pelanggan} adalah {pesanan} seharga Rp. {menu[pesanan]:,}, apakah benar?")
        konfirmasi = input("Silakan ketik 'benar' atau 'salah': ").lower()
        print(" ")

        if konfirmasi == "benar":
            print("SYUKURLAH KALAU BEGITU")
            break
        else:
            print("MAAF ATAS KESALAHAN KAMI, SILAKAN PESAN KEMBALI.")
            print(" ")
    else:
        print("Menu tidak tersedia. Silakan pilih dari daftar menu.")
        print(" ")

print(" ")
print("TERIMA KASIH ATAS PESANAN ANDA, PESANAN ANDA AKAN SEGERA SIAP :)")
