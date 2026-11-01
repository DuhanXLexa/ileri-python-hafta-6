# duhan goksal - 20253004040
# hafta 6 gorev 4 - collatz kasifi
# liste ve def kullanilmadan yazildi

# Girdi (a bolumu)
print("--- Collatz Kasifi ---")
n_girdi = int(input("n: "))

# Dogrula
if n_girdi <= 0:
    print("Hata: Pozitif bir tamsayi girmelisiniz!")
else:
    # Isle (a)
    n = n_girdi
    adim_sayisi = 0
    en_yuksek = n

    while n != 1:
        # Kurali kosullu ifadeyle tek satirda uyguluyoruz
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        adim_sayisi += 1
        if n > en_yuksek:
            en_yuksek = n

    # Cikti (a)
    print(f"{n_girdi} -> 1: {adim_sayisi} adım, en yüksek değer {en_yuksek}")

    # Girdi (b bolumu)
    ust_sinir = int(input("Üst sınır: "))

    if ust_sinir <= 0:
        print("Hata: Ust sinir pozitif olmalidir!")
    else:
        # Isle (b): 1'den ust sinira kadar en uzun zinciri bulma
        en_uzun_baslangic = 1
        maks_adim = 0

        for sayi in range(1, ust_sinir + 1):
            temp = sayi
            adim = 0
            while temp != 1:
                # Tek satirda kural
                temp = temp // 2 if temp % 2 == 0 else 3 * temp + 1
                adim += 1

            if adim > maks_adim:
                maks_adim = adim
                en_uzun_baslangic = sayi

        # Cikti (b)
        print(f"1-{ust_sinir} arasında en uzun zincir: {en_uzun_baslangic} ({maks_adim} adım)")
