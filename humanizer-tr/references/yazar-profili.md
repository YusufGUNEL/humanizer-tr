# Yazar profili

Bir metni "doğal" yapmak, onu genel bir iyi Türkçeye yaklaştırmaktır. Bir metni
**kullanıcının** sesiyle yazmak ise onun ritmine yaklaştırmaktır. Bu dosya ikincisini
anlatır. Fikir bushrabeg/turkce-humanizer'ın yazar profili sisteminden uyarlanmıştır.
Fark şudur: Bu skill profil için **soru sormaz**. Örnek varsa kullanır, yoksa genel
iyi Türkçeyle çalışır.

## Profil ne zaman kullanılır

- Kullanıcı bu konuşmada kendi yazdığı metinlerden örnek verdiyse ("benim yazılarım
  şöyle", "bu benim eski yazım", bir dosya ya da bağlantı).
- Kullanıcı bir profil bloğu yapıştırdıysa ya da bir profil dosyasının yolunu verdiyse.
- Kullanıcı "profilimi çıkar" dediyse: örneklerden aşağıdaki biçimde bir profil
  bloğu üret ve kaydedip daha sonra yapıştırabileceğini söyle.

Register profile uygun değilse (sözleşme, mevzuat, resmi yazışma, akademik metin)
profili yalnızca bağlaç ve sözcük tercihleri için kullanın, ritim için kullanmayın.

## Örneklerden ne çıkarılır

Her başlık için örneklerde gerçekten görülen şeyi yazın. Tek örnekte bir kez geçen
bir şey profil değildir. En az iki kez görülmeli.

| Başlık | Neye bakılır |
|---|---|
| Nefes | Tipik cümle uzunluğu (sözcük), kısa ve uzun cümle karışımı, paragraf uzunluğu |
| Bağlaçlar | "ama / ancak / fakat", "yani / kısacası", "çünkü / zira" tercihleri; cümle başında bağlaç kullanıyor mu |
| Kip ve çatı | Geniş zaman mı, "-yor" mu, "-mektedir" mi; etken mi edilgen mi; "biz" mi "ben" mi |
| Devrik ve eksiltili cümle | Kullanıyor mu, ne sıklıkta |
| Sözcük | Sık kullandığı sözcükler, yerleşik terim mi kendi kavramı mı, argo ya da yöresel söz |
| Noktalama | Ünlem, üç nokta, ayraç, iki nokta, emoji alışkanlığı |
| Kaçındıkları | Hiç kullanmadığı kalıplar (örneğin hiç "-mektedir" yok) |

## Profil bloğu biçimi

```
YAZAR PROFİLİ
Nefes: kısa-orta (8-16 sözcük), arada tek uzun cümle; paragraflar 2-4 cümle
Bağlaç: "ama" (hiç "ancak" yok), cümle başında "Yani" sık; "çünkü" az
Kip: "-yor" ağırlıklı, "-mektedir" yok; "ben" diliyle
Devrik: paragraf başına bir, genelde vurgu için
Sözcük: "açıkçası", "bence", "baya"; teknik terimler İngilizce kalıyor
Noktalama: ünlem yok, ayraç sık, emoji yok
Kaçındıkları: resmi edatlar, "olarak", soru-cevap kalıbı
```

## Profil nasıl uygulanır

1. Önce yapay zeka örüntülerini temizleyin (SKILL.md adımları). Profil, temizliğin
   yerine geçmez.
2. Temizlerken seçim gereken her yerde profile bakın: hangi bağlaç, hangi kip, cümle
   ne uzunlukta.
3. Profildeki bir alışkanlık bir örüntüyle çakışıyorsa yazarın alışkanlığı kazanır.
   Yazar sık devrik kuruyorsa bu "yapay" sayılmaz. Yazar ünlem kullanıyorsa NOK-04
   yalnızca yığılmayı azaltır.
4. Profil yeni bilgi eklemenin gerekçesi olamaz. Değişmez kurallar her zaman önce gelir.
5. Örnek verilmemişse profil uydurmayın.
