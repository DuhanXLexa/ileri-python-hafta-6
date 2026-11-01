# duhan goksal - 20253004040
# hafta 6 gorev 2 - metin analizoru
# liste ve def kullanilmadan tek for dongusuyle yazildi

# Girdi
cumle = input("Cümle: ")

# Dogrula
if len(cumle.strip()) == 0:
    print("Hata: Bos cumle girdiniz!")
else:
    # Isle
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"
    harf_sayisi = 0
    sesli_sayisi = 0
    sessiz_sayisi = 0
    rakam_sayisi = 0
    kelime_sayisi = 0

    kelimede_mi = False
    harfler_duz = ""
    ters_cumle = ""

    # tek bir for dongusu ile butun sayimlar ve ters cevirme
    for karakter in cumle:
        # tersini olusturma
        ters_cumle = karakter + ters_cumle

        # kelime sayaci bayrak kontrolu (bosluk olmayan karaktere girildiginde yeni kelime)
        if karakter != " " and not kelimede_mi:
            kelime_sayisi += 1
            kelimede_mi = True
        elif karakter == " ":
            kelimede_mi = False

        # karakter analizi
        if karakter.isalpha():
            harf_sayisi += 1
            if karakter in sesli_harfler:
                sesli_sayisi += 1
            else:
                sessiz_sayisi += 1

            # palindrom icin harfleri kucultup birlestirme (turkce I/İ ozel durumu)
            if karakter == "İ":
                k_harf = "i"
            elif karakter == "I":
                k_harf = "ı"
            else:
                k_harf = karakter.lower()
            harfler_duz += k_harf

        elif karakter.isdigit():
            rakam_sayisi += 1

    # palindrom kontrolu (harfler_duz tersi ile ayni mi)
    harfler_ters = ""
    for h in harfler_duz:
        harfler_ters = h + harfler_ters

    if len(harfler_duz) > 0 and harfler_duz == harfler_ters:
        palindrom_sonuc = "Palindrom"
    else:
        palindrom_sonuc = "Palindrom değil"

    # Cikti
    print(f"Harf: {harf_sayisi}  Sesli: {sesli_sayisi}  Sessiz: {sessiz_sayisi}  Rakam: {rakam_sayisi}  Kelime: {kelime_sayisi}")
    print(f"Ters: {ters_cumle}")
    print(palindrom_sonuc)
