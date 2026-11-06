---
name: humanizer-tr
description: Türkçe metinleri yapay zeka izlerinden arındırıp doğal bir insan yazısına dönüştürür; anlamı, sayıları, terimleri ve özel isimleri olduğu gibi korur, örnek verilmişse yazarın kendi ritmini taklit eder. Kullanıcı "insanlaştır", "doğallaştır", "humanize", "yapay zeka gibi durmasın", "AI kokuyor", "robot gibi olmuş", "daha doğal yaz", "Türkçeleştir", "elden geçir", "redakte et" dediğinde ya da bir Türkçe metnin (blog, e-posta, akademik paragraf, ürün açıklaması, sosyal medya gönderisi, rapor) üslubunu düzeltmek istediğinde kullan. "Bu metin yapay zeka mı, analiz et" isteğinde de kullan. Use for any request to humanize, de-AI or analyze AI patterns in Turkish text.
---

# Humanizer TR

Türkçede yapay zeka izi sözcüklerden çok **yapıda** görülür: tekdüze dizilim, eşit cümle
uzunlukları, "ve/ama/çünkü" tekeli, "-mektedir" yığılması, çeviri kokan kalıplar, İngilizce
noktalama ve sahnelenmiş vurgu. Bu skill'in işi, metni bu izlerden arındırırken **söylediği
hiçbir şeyi değiştirmemektir.** Hedef, iyi bir Türk yazarın bu metni nasıl yazacağıdır.
Yapay zeka dedektörünü atlatmak hedef değildir.

## Değişmez kurallar

Bu kurallar üslupla ilgili her karardan önce gelir. Kullanıcı bu metni gönderecek ya da
yayımlayacak, yanlış bir sayı ya da uydurulmuş bir iddia ona zarar verir.

1. **Anlamı değiştirme.** İddiaların gücünü de koru: "olabilir" "olur"a, "bazı" "birçok"a,
   "artırabilir" "artırır"a dönüşmesin.
2. **Sayıları, tarihleri, birimleri, terimleri, özel isimleri, alıntıları, URL'leri ve kodu
   aynen koru.** Yalnızca sayının **biçimini** Türkçeye uydurabilirsin (*25%* → *%25*).
   Değerden emin değilsen dokunma.
3. **Bilgi ekleme.** Kaynakta olmayan örnek, gerekçe, sonuç, rakam, kaynak ya da özne
   uydurma. Edilgen bir cümlede eylemi yapan metinde açıkça yoksa edilgen bırak.
4. **Bilgi çıkarma.** Yalnızca gerçekten boş olan dolguları sil. Bir maddeyi düzyazıya
   çevirirsen içindeki her bilgi yerinde kalmalı.
5. **Registerı ve hitabı koru.** Akademik metin akademik, resmi yazışma resmi kalır. Siz/sen
   ve biz/ben/edilgen değişmez.

## Çalışma adımları

### 1. Metni tanı (soru sormadan)

**Register:** Aşağıdakilerden birini seç. Kararsızsan daha resmi olanı seç. Resmi bir metni
gündelikleştirmek, gündelik bir metni biraz resmi bırakmaktan daha büyük hatadır. Kullanıcı
türü söylediyse onu kullan. Teşhisi kullanıcıya onaylatma, çıktının sonunda tek satırla
belirtmen yeterli (yalnızca analiz modunda ya da emin değilsen).

| Register | Örnek | Ritim düzenlemesi (adım 3c) |
|---|---|---|
| Hukuki-idari | sözleşme, KVKK metni, resmi yazı | Yok. Yalnızca dolgu ve noktalama |
| Akademik-kurumsal | makale, tez, rapor | Kısıtlı: cümle uzunluğu çeşitliliği |
| İş yazışması | e-posta, duyuru, toplantı notu | Kısıtlı |
| Analitik-gazetecilik | haber, analiz, bülten | Tam, gündelik bağlaçlar hariç |
| Blog-sosyal medya-pazarlama | blog, gönderi, ürün metni | Tam |
| Edebi | öykü, deneme | Tam, yazarın sesi önce gelir |

**Korunacaklar listesi:** Metindeki bütün sayıları, tarihleri, özel isimleri, terimleri,
alıntıları ve iddiaların kesinlik derecesini çıkar. Son adımda bu listeyle karşılaştıracaksın.

**Yazar profili:** Kullanıcı bu konuşmada kendi metinlerinden örnek verdiyse, bir profil
bloğu yapıştırdıysa ya da "profilimi çıkar" dediyse `references/yazar-profili.md` dosyasını
oku ve uygula. Bu durumda profil zorunludur: çıktı yazarın belirgin alışkanlıklarını
(hitap ve kişi, sık sözcükleri, bağlaçları, noktalama huyu) taşımalıdır. Yalnızca temizlenmiş
genel bir Türkçe teslim etmek bu durumda eksik iştir. Örneklerdeki olayları ve anıları yeni
metne taşıma, yalnızca sesi al. Örnek yoksa profil isteme, genel iyi Türkçeyle devam et.

### 2. Örüntüleri bul

`references/ai-oruntuleri.md` dosyasını oku: 50'yi aşkın örüntü, her biri önce/sonra örneği
ve **Dokunma** satırıyla. Aynı kalıp bir registerda iz, ötekinde olağan dildir. Tek bir
"bu bağlamda" sorun değildir; sorun yığılmadır.

Gerektiğinde:
- `references/cumle-turleri.md`: tekdüze paragrafı hangi yapılarla kıracağın.
- `references/baglaclar.md`: ve/ama/çünkü tekeline alternatifler ve anlam tuzakları.
- `references/noktalama.md`: TDK'ya dayalı noktalama ve yazım (uzun çizgi, de/da, ki, mi,
  kesme, büyük harf, sayılar).

### 3. Yeniden yaz

**a. Önce sadeleştir.** En etkili düzeltme çoğu zaman silmektir: klişe, pekiştirme, hazırlık
cümlesi, boş kapanış, sohbet kalıntısı, okurun bildiği açıklama.

**b. Sonra yapıyı düzelt.** Birleştir (zarf-fiil, sıfat-fiil), şişirilmiş fiili sadeleştir
("gerçekleştirildi" → "yapıldı"), çeviri kalıbını Türkçeleştir, edilgeni (öznesi belliyse)
etkene çevir. Bağlaçları dağıtma, seç: "ama" yerine sırayla "oysa, ne var ki, buna karşın"
koymak da bir örüntüdür. Çoğu zaman bağlacı tamamen kaldır.

**c. Register izin veriyorsa ritmi aç.** Cümle uzunlukları dalgalansın: bir uzun cümleyi
böl, iki kısa cümleyi birleştir. Blog ve sosyal medyada bir iki devrik cümle ya da
tek bir kısa vurgu cümlesi sese katkı yapar. Bunlar **tam cümle** olmalı ("Bitti." gibi
yarım cümle değil). Metne "insan" süsü vermek için eklenen devrik cümle, düzeltilen
tekdüzelik kadar yapay durur. Akademik, resmi ve hukuki metinde devrik ve eksiltili
cümle kullanma.

**d. Biçimi metne uydur.** Kısa bir e-postadaki başlıkları ve gereksiz madde işaretlerini
düzyazıya çevir. Gerçek adım listelerini, tabloları, kodu ve kullanıcının şablonunu koru.

**e. Noktalama ve yazımı düzelt.** Cümle içindeki uzun çizgiyi (—) kaldır, "ve"den önceki
virgülü sil, noktalı virgülü azalt, de/da, ki, mi ve kesme işaretini TDK'ya göre düzelt.

**Ölçülü ol.** Her cümleyi değiştirmek hedef değildir. İyi bir cümleye dokunma.

### 4. Denetle

Teslim etmeden önce yeni metni korunacaklar listesiyle karşılaştır:
- Her sayı, tarih ve özel isim yerinde ve aynı mı?
- Her iddia aynı kesinlikte mi? Kaynakta olmayan bir özne, gerekçe ya da kaynak eklendi mi?
- Silinen her şey gerçekten boş muydu?
- Register ve hitap aynı mı?
- Yeni metinde yeni bir örüntü doğdu mu (aynı bağlacın tekrarı, art arda devrik cümle,
  her paragrafı kısa vurguyla bitirme)?

Şüphe varsa kaynaktaki hâline dön. Anlamca güvenli ama biraz daha az akıcı bir metin,
akıcı ama yanlış bir metinden her zaman iyidir.

## Çıktı

**Varsayılan (düzelt):** Yalnızca düzeltilmiş metin. Önsöz yok, "İşte düzeltilmiş metin:"
yok, kapanış yok. Kaynağın biçimini (paragraflar, gerçek listeler, imza bloğu) koru.

Metnin altına yalnızca şu durumlarda kısa bir not ekle:
- Anlamdan emin olamadığın için bir şeye dokunmadıysan (ör. "1,500" binlik mi ondalık mı).
- Metinde bir olgu hatası, kaynağı belirtilmemiş bir iddia (OTR-01) ya da doldurulmamış bir
  yer tutucu (KAL-01) gördüysen. Olguyu sen düzeltme, yalnızca belirt.
- Kullanıcı değişiklikleri istediyse.

**Değişiklik özeti** (istenirse, en çok 7 madde):

```
**Değişiklik özeti**
- YAPI-03: "-mektedir" ile biten 6 yüklemin 4'ü geniş zaman ve şimdiki zamana çevrildi.
- NOK-01: 3 uzun çizgi kaldırıldı.
- SAH-02, SOZ-02: "Şunu belirtmek gerekir ki", "Bu bağlamda" silindi.
- Dokunulmayanlar: "1,500" (binlik mi ondalık mı belirsiz).
```

**Analiz modu** ("analiz et", "yapay zeka mı", "ne kadar yapay"): metni değiştirmeden şunu ver:
1. Register teşhisi.
2. Bulunan örüntüler: kod, metindeki yeri (kısa alıntı), kaç kez.
3. Yoğunluk: 100 sözcükte örüntü sayısı ve tek cümlelik yorum ("yoğun / orta / az").
4. Kullanıcı isterse ardından düzeltilmiş metin.
Bu bir yapay zeka dedektörü değildir. "Bunu kesin yapay zeka yazdı" ya da "kesin insan
yazdı" deme. Yalnızca örüntüleri raporla.

## Özel durumlar

- **Metin zaten doğalsa** küçük düzeltmelerle (yazım, noktalama) yetin ve bunu tek cümleyle
  söyle. Yapacak bir şey yokken değişiklik üretme.
- **Metin Türkçe değilse ve kullanıcı "Türkçeleştir" diyorsa** metni bu ilkelere göre doğal
  Türkçeye çevir, kelime kelime çevirme. Çeviri olduğunu belirt.
- **Türkçe metin içinde İngilizce terim** varsa dokunma. Terim kullanıcının tercihidir. Plaza
  dili (PLZ-01) yalnızca register iş dışı ya da resmi ise ve terim değil de alışkanlık ise
  düzeltilir.
- **Kod blokları, alıntılar, yasal metinden aktarılan maddeler** olduğu gibi kalır.
- **Uzun metinlerde** paragraf paragraf ilerle, her paragraftan sonra korunacaklar listesini
  kontrol et.
- **Kullanıcının bilinçli üslubu** (edebi devrik dil, kasıtlı plaza dili, markanın emojisi)
  belirginse koru. Yalnızca yapay zekadan gelen katmanı temizle.

## Örnekler

`examples/` klasöründe beş metin türü için (blog, e-posta, akademik paragraf, ürün açıklaması,
LinkedIn gönderisi) tam önce/sonra çiftleri var. `examples/00-guclu-cumleler-kaynak.md`
güçlü Türkçe cümle mimarisine örnekler içerir. Bir türle ilk kez karşılaştığında ilgili
örneğe bakmak ölçüyü tutturmana yardım eder.
