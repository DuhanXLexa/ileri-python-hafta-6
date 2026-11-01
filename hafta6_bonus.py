# duhan goksal - 20253004040
# hafta 6 bonus - luhn algoritmasi ile kontrol hanesi bulma
# liste ve def kullanilmadan yazildi

numara_15 = "453914880343646"
bulunan_hane = -1

# 0-9 arasi rakamlari sirayla deniyoruz
for kontrol_adayi in range(10):
    kart_numarasi = numara_15 + str(kontrol_adayi)
    toplam = 0

    # 16 haneli numarayi Luhn algoritmasi ile dogrulama
    # cift indeksler (bastan 1., 3., 5... yani sondan 2., 4... haneler) 2 ile carpilir
    for i in range(16):
        rakam = int(kart_numarasi[i])
        if i % 2 == 0:
            carpim = rakam * 2
            toplam += carpim - 9 if carpim > 9 else carpim
        else:
            toplam += rakam

    # toplam 10'a tam bolunuyorsa gecerlidir
    if toplam % 10 == 0:
        bulunan_hane = kontrol_adayi
        print(f"Luhn algoritması kontrol hanesi bulundu: {bulunan_hane}")
        print(f"Tam 16 haneli geçerli numara: {kart_numarasi}")
        break
