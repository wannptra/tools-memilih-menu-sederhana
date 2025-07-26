print("=" * 50)
print("SELAMAT DATANG DI RESTORAN KARBIT CHAMPIONS")
print("=" * 50)
print()

# Input nama pelanggan
nama_pelanggan = input("Dengan tuan/nyonya siapa? ").strip()
while not nama_pelanggan:
    print("Nama tidak boleh kosong!")
    nama_pelanggan = input("Dengan tuan/nyonya siapa? ").strip()

print()

# Dictionary menu untuk memudahkan pengelolaan
menu = {
    "1": {"nama": "Daging asap", "harga": 50000},
    "2": {"nama": "Daging makima", "harga": 1500000},
    "3": {"nama": "Paha eula", "harga": 500000},
    "4": {"nama": "Susu hutao", "harga": 1000}
}

def tampilkan_menu():
    print("=" * 40)
    print("           DAFTAR MENU")
    print("=" * 40)
    for nomor, item in menu.items():
        print(f"{nomor}. {item['nama']:<15} -- Rp. {item['harga']:,}")
    print("=" * 40)

def proses_pesanan(pilihan_input):
    """Memproses input pilihan menjadi dictionary pesanan dengan jumlah"""
    pesanan = {}
    
    # Split input berdasarkan koma atau spasi
    pilihan_list = pilihan_input.replace(" ", ",").split(",")
    
    for pilihan in pilihan_list:
        pilihan = pilihan.strip()
        if pilihan and pilihan in menu:
            # Hitung jumlah setiap item
            if pilihan in pesanan:
                pesanan[pilihan]["jumlah"] += 1
            else:
                pesanan[pilihan] = {
                    "nama": menu[pilihan]["nama"],
                    "harga": menu[pilihan]["harga"],
                    "jumlah": 1
                }
        elif pilihan and pilihan not in menu:
            return None, f"Pilihan '{pilihan}' tidak valid!"
    
    if not pesanan:
        return None, "Tidak ada pesanan yang valid!"
    
    return pesanan, None

def tampilkan_pesanan(pesanan):
    """Menampilkan ringkasan pesanan dengan jumlah"""
    print()
    print("=" * 60)
    print("              RINGKASAN PESANAN")
    print("=" * 60)
    
    total_harga = 0
    nomor = 1
    
    for nomor_menu, item in pesanan.items():
        subtotal = item['harga'] * item['jumlah']
        if item['jumlah'] > 1:
            print(f"{nomor}. {item['nama']:<20} x{item['jumlah']:<3} -- Rp. {item['harga']:,} = Rp. {subtotal:,}")
        else:
            print(f"{nomor}. {item['nama']:<20} x{item['jumlah']:<3} -- Rp. {subtotal:,}")
        total_harga += subtotal
        nomor += 1
    
    print("-" * 60)
    print(f"{'TOTAL HARGA':<25} -- Rp. {total_harga:,}")
    print("=" * 60)
    
    return total_harga

def konfirmasi_pesanan(nama, pesanan, total_harga):
    print()
    print("*" * 60)
    print("         KONFIRMASI SEBELUM PEMBAYARAN")
    print("*" * 60)
    print(f"Nama Pelanggan: {nama}")
    print()
    print("Detail Pesanan:")
    
    for nomor_menu, item in pesanan.items():
        subtotal = item['harga'] * item['jumlah']
        if item['jumlah'] > 1:
            print(f"  • {item['nama']} x{item['jumlah']} = Rp. {subtotal:,}")
        else:
            print(f"  • {item['nama']} = Rp. {subtotal:,}")
    
    print()
    print(f"Total Pembayaran: Rp. {total_harga:,}")
    print("*" * 60)
    
    while True:
        konfirmasi = input("Apakah pesanan sudah benar? (ya/tidak): ").lower().strip()
        if konfirmasi in ['ya', 'y', 'benar']:
            return True
        elif konfirmasi in ['tidak', 'no', 'n', 'salah']:
            return False
        else:
            print("Mohon ketik 'ya' atau 'tidak'")

# Loop utama program
while True:
    tampilkan_menu()
    print()
    print("Contoh pesanan:")
    print("• Ketik '1' untuk 1x Daging asap")
    print("• Ketik '1,1' untuk 2x Daging asap") 
    print("• Ketik '1,3,1' untuk 2x Daging asap + 1x Paha eula")
    print("• Ketik '2,4,2,4' untuk 2x Daging makima + 2x Susu hutao")
    print()
    
    # Input pilihan menu
    pilihan_input = input(f"Silakan pilih menu yang mau {nama_pelanggan} pesan: ").strip()
    
    if not pilihan_input:
        print("Mohon masukkan pilihan menu!")
        input("Tekan Enter untuk melanjutkan...")
        print()
        continue
    
    # Proses pesanan
    pesanan, error = proses_pesanan(pilihan_input)
    
    if error:
        print(f"Error: {error}")
        print("Silakan pilih nomor menu yang tersedia (1-4)")
        input("Tekan Enter untuk melanjutkan...")
        print()
        continue
    
    # Tampilkan ringkasan pesanan
    total_harga = tampilkan_pesanan(pesanan)
    
    # Konfirmasi pesanan
    if konfirmasi_pesanan(nama_pelanggan, pesanan, total_harga):
        print()
        print("✓ PESANAN DIKONFIRMASI!")
        break
    else:
        print()
        print("Baik, silakan pilih menu kembali...")
        input("Tekan Enter untuk melanjutkan...")
        print()

# Pesan akhir
print()
print("=" * 70)
print("            TERIMA KASIH ATAS PESANAN ANDA!")
print("=" * 70)
print(f"Nama Pelanggan: {nama_pelanggan}")
print()
print("Pesanan Anda:")

for nomor_menu, item in pesanan.items():
    subtotal = item['harga'] * item['jumlah']
    if item['jumlah'] > 1:
        print(f"  • {item['nama']} x{item['jumlah']} = Rp. {subtotal:,}")
    else:
        print(f"  • {item['nama']} = Rp. {subtotal:,}")

print()
print(f"Total Pembayaran: Rp. {total_harga:,}")
print()
print("       PESANAN ANDA AKAN SEGERA SIAP :)")
print("=" * 70)