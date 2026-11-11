print("================================")
print("     DAFTAR MENU      ")
print("================================")

nasi_bakar = 0
mie_goreng = 0
ayam_penyet = 0
soto_ayam = 0
teh_manis = 0
ikan_bakar = 0
ayam_pop = 0
vanilla_cokelat = 0

while True:
    print("\n--- DAFTAR MENU MAKANAN ---")
    print("1. Nasi Bakar        - Rp 22.000")
    print("2. Mie Goreng        - Rp 15.000")
    print("3. Ayam Penyet       - Rp 18.000")
    print("4. Soto Ayam         - Rp 20.000")
    print("5. Teh Manis Dingin  - Rp 15.000")
    print("6. Ikan Bakar        - Rp 30.000")
    print("7. Ayam Pop          - Rp 17.000")
    print("8. Vanilla Cokelat   - Rp 13.000")
    print("0. Selesai Memilih")
    print("---------------------------")

    pilihan = input("Pilih nomor menu (0 untuk selesai): ")

    if pilihan == "0":
        break

    if pilihan == "1":
        jumlah = int(input("Jumlah Nasi Bakar: "))
        nasi_bakar = nasi_bakar + jumlah

    elif pilihan == "2":
        jumlah = int(input("Jumlah Mie Goreng: "))
        mie_goreng = mie_goreng + jumlah

    elif pilihan == "3":
        jumlah = int(input("Jumlah Ayam Penyet: "))
        ayam_penyet = ayam_penyet + jumlah

    elif pilihan == "4":
        jumlah = int(input("Jumlah Soto Ayam: "))
        soto_ayam = soto_ayam + jumlah

    elif pilihan == "5":
        jumlah = int(input("Jumlah Teh Manis Dingin: "))
        teh_manis = teh_manis + jumlah

    elif pilihan == "6":
        jumlah = int(input("Jumlah Ikan Bakar: "))
        ikan_bakar = ikan_bakar + jumlah

    elif pilihan == "7":
        jumlah = int(input("Jumlah Ayam Pop: "))
        ayam_pop = ayam_pop + jumlah

    elif pilihan == "8":
        jumlah = int(input("Jumlah Vanilla Cokelat: "))
        vanilla_cokelat = vanilla_cokelat + jumlah

    else:
        print("Menu tidak tersedia!")

total = (nasi_bakar * 22000) + (mie_goreng * 15000) + (ayam_penyet * 18000) + (soto_ayam * 20000) + (teh_manis * 15000) + (ikan_bakar * 30000) + (ayam_pop * 17000) + (vanilla_cokelat * 13000)

print("\n=========================================")
print("           STRUK PEMBAYARAN              ")
print("=========================================")

if nasi_bakar > 0:
    print("Nasi Bakar        :", nasi_bakar, "x Rp 22.000 =", nasi_bakar * 22000)

if mie_goreng > 0:
    print("Mie Goreng        :", mie_goreng, "x Rp 15.000 =", mie_goreng * 15000)

if ayam_penyet > 0:
    print("Ayam Penyet       :", ayam_penyet, "x Rp 18.000 =", ayam_penyet * 18000)

if soto_ayam > 0:
    print("Soto Ayam         :", soto_ayam, "x Rp 20.000 =", soto_ayam * 20000)

if teh_manis > 0:
    print("Teh Manis Dingin  :", teh_manis, "x Rp 15.000 =", teh_manis * 15000)

if ikan_bakar > 0:
    print("Ikan Bakar        :", ikan_bakar, "x Rp 30.000 =", ikan_bakar * 30000)

if ayam_pop > 0:
    print("Ayam Pop          :", ayam_pop, "x Rp 17.000 =", ayam_pop * 17000)

if vanilla_cokelat > 0:
    print("Vanilla Cokelat   :", vanilla_cokelat, "x Rp 13.000 =", vanilla_cokelat * 13000)

print("-----------------------------------------")
print("Total Belanja :", total)

if total > 100000:
    potongan = total * 30 // 100
    total_bayar = total - potongan

    print("Diskon        : 30%")
    print("Potongan      :", potongan)
else:
    potongan = 0
    total_bayar = total

    print("Diskon        : Tidak ada")

print("-----------------------------------------")
print("Total Bayar   :", total_bayar)
print("=========================================")
print("              TERIMA KASIH               ")
print("=========================================")