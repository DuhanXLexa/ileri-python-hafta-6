# Python ile Programlama - Hafta 6 Laboratuvarı: Hesapla, Karar Ver, Tekrarla

**Öğrenci:** Duhan Göksal  
**Numara:** 20253004040  
**Ders:** Python ile Programlama  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**GitHub Deposu:** https://github.com/DuhanXLexa/ileri-python-hafta-6  

Bu labdaki bütün görevler kural gereği **liste, sözlük ve def kullanılmadan**; sadece temel değişkenler, if/elif/else karar yapıları ve for/while döngüleri kullanılarak yazılmıştır. Her kod `Girdi -> Doğrula -> İşle -> Çıktı` mantığıyla ayrılmıştır.

---

## Dosyalar ve Görevler

### 1. `hafta6_gorev1.py` - Üçgen Analizörü
- 3 kenar uzunluğunu alır.
- Kenarlar pozitif mi ve üçgen eşitsizliğine uyuyor mu kontrol eder.
- Kenarlarına göre (Eşkenar / İkizkenar / Çeşitkenar) sınıflandırır.
- Kosinüs teoremi ile en büyük açıyı bulur (`math.acos` ve `math.degrees`).
- Açıyı `math.isclose(aci, 90)` ile sınayarak Dik, Geniş veya Dar açılı olarak belirler.
- Çevre ve Heron formülü ile alanı hesaplayıp 2 ondalık basamakla ekrana yazar.

### 2. `hafta6_gorev2.py` - Metin Analizörü
- Girilen cümleyi tek bir `for` döngüsüyle baştan sona gezer.
- Toplam harf, sesli harf, sessiz harf ve rakamları sayar.
- Kelime sayısını boşluk geçişlerini takip eden bir bayrak (flag) ile sayar.
- Cümleyi tersten yazdırır.
- Sadece harfleri alıp küçük harfe çevirerek cümlenin palindrom olup olmadığını söyler.

### 3. `hafta6_gorev3.py` - T.C. Kimlik No Doğrulama
- 11 haneli mi, hepsi rakam mı ve ilk hanesi 0'dan farklı mı diye biçim kontrolü yapar.
- Tek ve çift hanelerin toplamını döngüyle bulur.
- $h_{10} = (7T - Ç) \pmod{10}$ ve $h_{11} = (T + Ç + h_{10}) \pmod{10}$ formüllerini hesaplar.
- 10. ve 11. hane ile eşleşiyorsa `GEÇERLİ`, uymuyorsa `GEÇERSİZ` yazar.

### 4. `hafta6_gorev4.py` - Collatz Kaşifi
- Girilen $n$ sayısı için 1'e ulaşana kadar Collatz adımlarını işletir. Kural tek satırda koşullu ifade ile yazılmıştır (`n = n // 2 if n % 2 == 0 else 3 * n + 1`).
- Adım sayısını ve ulaşılan maksimum değeri ekrana basar.
- İkinci kısımda verilen bir üst sınıra kadar (örn: 1000) en uzun zinciri oluşturan başlangıç sayısını ve adım sayısını iç içe döngülerle bulur.

### 5. `hafta6_gorev5.py` - Adam Asmaca
- `KOŞUL` gizli kelimesi için harf tahmin oyunu.
- Denenen harfler bir karakter dizisinde biriktirilir (`tahminler += harf`, liste kullanılmamıştır).
- Kelimeyi `_ _ _ _ _   (hata: 0/6)` formatında gösterir.
- Tek harf olmayan ve daha önce girilmiş harfleri `continue` ile atlar.
- Türkçe karakterler için `i` harfini `İ`, `ı` harfini `I` yapar.
- 6 hata dolunca `while ... else` bloğundaki `else` ile kelimeyi gösterir, bilinirse `break` ile kazanır.

### Bonus: `hafta6_bonus.py` - Luhn Algoritması
- 15 haneli `453914880343646` numarasının sonuna 0-9 arasındaki rakamları tek tek dener.
- Luhn algoritması kuralına göre toplamı 10'a tam bölünen ilk geçerli kontrol hanesini bulur ve döngüden `break` ile çıkar (Doğru kontrol hanesi: 7).

---

## Teslimat Paketi
Tüm python dosyaları yönergede belirtildiği gibi tek bir zip dosyasında toplanmıştır:
`20253004040_hafta6.zip`

