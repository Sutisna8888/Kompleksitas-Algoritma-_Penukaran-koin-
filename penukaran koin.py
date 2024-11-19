def tukar_koin(koin, jumlah):
    koin.sort(reverse=True)
    hasil = []
    total = 0
    
    for k in koin:
        while total + k <= jumlah:
            hasil.append(k)
            total += k

    if total == jumlah:
        return hasil
    else:
        return "Tidak bisa ditukar dengan jumlah koin yang tersedia"

koin = [2, 3, 5, 10, 15]
jumlah = int(input("Masukkan jumlah uang yang ingin ditukar: "))
hasil = tukar_koin(koin, jumlah)
if isinstance(hasil, list):
    print(f"Koin yang digunakan: {hasil}")
    print(f"Jumlah total: {sum(hasil)}")
else:
    print(hasil)
