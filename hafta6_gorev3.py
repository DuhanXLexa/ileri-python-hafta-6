# duhan goksal - 20253004040
# hafta 6 gorev 3 - tc kimlik numarasi dogrulama
# liste ve def kullanilmadan yazildi

# Girdi
tc = input("T.C. kimlik no: ").strip()

# Dogrula
# 11 haneli mi, hepsi rakam mi ve ilk hane 0 dan farkli mi
bicim_gecerli = True

if len(tc) != 11:
    bicim_gecerli = False
elif not tc.isdigit():
    bicim_gecerli = False
elif tc[0] == "0":
    bicim_gecerli = False

if not bicim_gecerli:
    print(f"T.C. kimlik no: {tc} -> GEÇERSİZ")
else:
    # Isle
    # 1., 3., 5., 7., 9. haneler (indeks 0, 2, 4, 6, 8) -> tek haneler
    # 2., 4., 6., 8. haneler (indeks 1, 3, 5, 7) -> cift haneler
    tekler_toplami = 0
    ciftler_toplami = 0

    for i in range(9):
        rakam = int(tc[i])
        if i % 2 == 0:
            tekler_toplami += rakam
        else:
            ciftler_toplami += rakam

    # kontrol haneleri hesaplama
    h10 = (7 * tekler_toplami - ciftler_toplami) % 10
    h11 = (tekler_toplami + ciftler_toplami + h10) % 10

    gercek_h10 = int(tc[9])
    gercek_h11 = int(tc[10])

    # Cikti
    if h10 == gercek_h10 and h11 == gercek_h11:
        print(f"Tek: {tekler_toplami}  Çift: {ciftler_toplami}  10. hane: {h10}  11. hane: {h11} -> GEÇERLİ")
    else:
        print(f"T.C. kimlik no: {tc} -> GEÇERSİZ")
