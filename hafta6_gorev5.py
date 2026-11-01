# duhan goksal - 20253004040
# hafta 6 gorev 5 - adam asmaca
# liste ve def kullanilmadan yazildi

# Girdi / Baslangic Degiskenleri
kelime = "KOŞUL"
tahminler = ""
hata_sayisi = 0
maks_hata = 6

print("--- Adam Asmaca Oyunu ---")

while hata_sayisi < maks_hata:
    # Kelimenin anlik durumunu ekrana hazirlama
    gorunum = ""
    tamamlandi_mi = True

    for k_harfi in kelime:
        if k_harfi in tahminler:
            gorunum += k_harfi + " "
        else:
            gorunum += "_ "
            tamamlandi_mi = False

    gorunum = gorunum.strip()

    # Eger tum harfler bilindiyse kazandik
    if tamamlandi_mi:
        print(f"{gorunum}   (hata: {hata_sayisi}/{maks_hata})  Kazandınız!")
        break

    # Durumu goster
    print(f"{gorunum}   (hata: {hata_sayisi}/{maks_hata})")

    # Kullanicidan harf alma
    giris = input("Harf: ").strip()

    # Dogrulama kontrolleri
    if len(giris) != 1 or not giris.isalpha():
        print("Lütfen tek bir geçerli harf giriniz.")
        continue

    # Turkce karakter donusumu (i -> İ, ı -> I)
    if giris == "i":
        harf = "İ"
    elif giris == "ı":
        harf = "I"
    else:
        harf = giris.upper()

    # Daha once denenmis mi kontrolu
    if harf in tahminler:
        print("->  Bu harfi zaten denediniz.")
        continue

    # Yeni harfi tahminlere ekleme (stringde biriktirme, liste yok)
    tahminler += harf

    # Harf kelimede var mi?
    if harf not in kelime:
        hata_sayisi += 1

else:
    # 6 hata dolunca calisan while-else blogu
    print(f"\nKaybettiniz! Gizli kelime: {kelime} (hata: {hata_sayisi}/{maks_hata})")
