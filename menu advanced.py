menu = {
    "Daging asap": 50000,
    "Daging rusdi": 1500000,
    "Paha ambatukam": 500000,
    "Susu tringgiling": 1000
}

print("SELAMAT DATANG DI RESTORAN DODO NASIHIN")
nama = input("Dengan tuan/nyonya siapa? ")
print()

print("------ MENU MAKANAN ------")
for item, harga in menu.items():
    print(f"{item:<20} - Rp {harga:,}")
print()

pesanan = {}

while True:
    item = input("Pilih menu (mohon huruf kecil/besarnya diperhatikan, spasinya juga. ketik 'selesai' kalau sudah): ")
    if item.lower() == "selesai":
        break
    if item in menu:
        try:
            qty = int(input(f"Berapa banyak '{item}'? "))
            pesanan[item] = pesanan.get(item, 0) + qty
        except ValueError:
            print("Masukkan angka untuk jumlah.")
    else:
        print("Menu tidak tersedia, cek lagi nama menu.")

    print()

if not pesanan:
    print("Anda tidak memesan apapun. Terima kasih.")
    exit()

# Hitung total
total = sum(menu[item] * qty for item, qty in pesanan.items())

# Konfirmasi pesanan
print("** KONFIRMASI SEBELUM PEMBAYARAN **")
desc = ", ".join(f"{item} {qty}" for item, qty in pesanan.items())
print(f"Pesanan {nama} adalah: {desc}.")
print(f"Total pesanan adalah Rp {total:,}.")
konfirmasi = input("Ketik 'benar' jika sesuai, atau 'salah' untuk ulang: ").lower()
print()

if konfirmasi == "benar":
    print("Pesanan dikonfirmasi. Terima kasih!")
    print("Pesanan Anda akan segera disiapkan :)")
else:
    print("Oke, silakan pesan kembali ya!")