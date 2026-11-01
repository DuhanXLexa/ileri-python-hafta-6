# duhan goksal - 20253004040
# hafta 6 gorev 1 - ucgen analizoru
# liste ve def kullanilmadan yazildi

import math

# Girdi
print("--- Ucgen Analizoru ---")
a = float(input("a kenari: "))
b = float(input("b kenari: "))
c = float(input("c kenari: "))

# Dogrula
# kenarlar pozitif olmali ve ucgen esitsizligini saglamali
if a <= 0 or b <= 0 or c <= 0:
    print("Hata: Kenar uzunluklari pozitif olmalidir!")
elif not (a < b + c and b < a + c and c < a + b):
    print("Hata: Bu kenar uzunluklariyla ucgen olusturulamaz (ucgen esitsizligi bozuluyor)!")
else:
    # Isle
    # 1. kenarlarina gore siniflandirma
    if a == b == c:
        kenar_turu = "Eşkenar"
    elif a == b or a == c or b == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    # 2. en uzun kenari ve diger iki kenari bulma (max ve liste kullanmadan)
    if a >= b and a >= c:
        en_uzun = a
        diger1 = b
        diger2 = c
    elif b >= a and b >= c:
        en_uzun = b
        diger1 = a
        diger2 = c
    else:
        en_uzun = c
        diger1 = a
        diger2 = b

    # 3. kosinus teoremi ile en buyuk aciyi bulma: cos(a) = (b^2 + c^2 - a^2) / (2bc)
    cos_alfa = (diger1**2 + diger2**2 - en_uzun**2) / (2 * diger1 * diger2)
    # kucuk yuvarlama hatalari yuzunden aralik disina tasmasini engelliyoruz
    if cos_alfa > 1.0:
        cos_alfa = 1.0
    elif cos_alfa < -1.0:
        cos_alfa = -1.0

    aci = math.degrees(math.acos(cos_alfa))

    # 4. acisina gore siniflandirma (isclose ile 90 kontrolu)
    if math.isclose(aci, 90.0, abs_tol=1e-5):
        aci_turu = "Dik açılı"
    elif aci > 90.0:
        aci_turu = "Geniş açılı"
    else:
        aci_turu = "Dar açılı"

    # 5. cevre ve heron formulu ile alan
    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    # Cikti
    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f}  Alan: {alan:.2f}  En büyük açı: {aci:.2f}°")
