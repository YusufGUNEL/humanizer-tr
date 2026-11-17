# Türkçe yapay zeka örüntüleri

Bu dosya, Türkçe metinlerde yapay zeka izi bırakan örüntülerin kataloğudur. Her örüntü aynı şablonu kullanan bağımsız bir bloktur. Yeni bir örüntü eklemek için en alttaki şablonu kopyalayıp doldurmanız yeterli. Ayrıntılı katkı kuralları için deponun `CONTRIBUTING.md` dosyasına bakın.

**Okuma notu (skill için):** Bu bir yasak listesi değildir. "Bu bağlamda" sözü tek başına yanlış değildir. Sorun, bu tür kalıpların yığılması ve metni içi boş bir resmiyetle doldurmasıdır. Her bloktaki **Dokunma** satırı, örüntünün meşru olduğu durumları gösterir. Bir örüntüyü kaldırırken anlamın, sayıların, terimlerin ve özel isimlerin aynen korunması şarttır.

## Kategoriler

| Önek | Kategori |
|---|---|
| `YAPI` | Cümle ve paragraf yapısı |
| `SOZ` | Klişe ve şişirilmiş sözcük seçimi |
| `CEV` | İngilizceden çeviri kokan ifadeler |
| `NOK` | Noktalama ve tipografi |
| `BIC` | Biçim ve düzen (başlık, madde, kalın yazı) |
| `DOL` | Açılış ve kapanış dolguları |
| `YAZ` | Yazım hataları |
| `SAH` | Sahneleme: söylemek yerine hazırlık, dram ve sahte tartışma |
| `PLZ` | Plaza ve bürokrasi dili |
| `OTR` | Ödünç otorite ve doğrulanamayan iddia |
| `KAL` | Sohbet ve taslak kalıntıları |

**Kaynak notu:** `SAH`, `OTR`, `KAL` kategorileri ve `SOZ-07`–`SOZ-10`, `YAPI-09`–`YAPI-10`
örüntüleri İngilizce humanizer çalışmalarındaki dilden bağımsız kalıpların (blader/humanizer,
Wikipedia "Signs of AI writing") Türkçe karşılıklarıdır. `NOK-05`–`NOK-07`, `SOZ-07`,
`SOZ-11`, `YAPI-10` bushrabeg/turkce-humanizer sinyallerinden uyarlanmıştır. `PLZ` ve
`CEV-05` bu projede eklenen Türkçeye özgü örüntülerdir.

## Dizin

- [YAPI-01 Tekdüze dizilim ve eşit cümle uzunluğu](#yapi-01)
- [YAPI-02 ve/ama/çünkü tekeli](#yapi-02)
- [YAPI-03 -mektedir/-maktadır yığılması](#yapi-03)
- [YAPI-04 Gereksiz edilgen yapı](#yapi-04)
- [YAPI-05 Üçlü sıralama alışkanlığı](#yapi-05)
- [YAPI-06 "Sadece X değil, aynı zamanda Y" kalıbı](#yapi-06)
- [YAPI-07 Kendi sorup kendi cevaplama](#yapi-07)
- [YAPI-08 Her paragrafı özet cümlesiyle bitirme](#yapi-08)
- [SOZ-01 "Önemli bir rol oynamaktadır" ailesi](#soz-01)
- [SOZ-02 Geçiş ve bağlam klişeleri](#soz-02)
- [SOZ-03 Pekiştirme şişirmesi](#soz-03)
- [SOZ-04 "olarak" ve "-mekte olup" fazlalığı](#soz-04)
- [SOZ-05 "Bu durum" / "Bu da" ile açılış](#soz-05)
- [SOZ-06 Gösterişli mecaz öbekleri](#soz-06)
- [CEV-01 Çeviri deyimler](#cev-01)
- [CEV-02 "-e sahip olmak" fazlalığı](#cev-02)
- [CEV-03 "tarafından" ve "için" yığılması](#cev-03)
- [CEV-04 Gereksiz iyelik zamiri ve "bir"](#cev-04)
- [NOK-01 Cümle içinde uzun çizgi (—)](#nok-01)
- [NOK-02 "ve"den önce virgül](#nok-02)
- [NOK-03 İngilizce sayı ve yüzde biçimi](#nok-03)
- [NOK-04 Ünlem ve emoji bolluğu](#nok-04)
- [BIC-01 Gereksiz başlık, madde işareti ve kalın yazı](#bic-01)
- [DOL-01 Açılış dolguları](#dol-01)
- [DOL-02 Kapanış dolguları](#dol-02)
- [DOL-03 Sıralama dolguları: "Öncelikle ... İkinci olarak ... Son olarak ..."](#dol-03)
- [YAZ-01 Bağlaç de/da](#yaz-01)
- [YAZ-02 ki](#yaz-02)
- [YAZ-03 Soru eki mi](#yaz-03)
- [YAZ-04 Kesme işareti](#yaz-04)
- [YAZ-05 Büyük harf](#yaz-05)
- [YAPI-09 Tekrarlanan cümle açılışları](#yapi-09)
- [YAPI-10 Eş anlamlı rotasyonu](#yapi-10)
- [YAPI-11 Zincirleme isim tamlaması yığılması](#yapi-11)
- [SOZ-07 Vurgu doldurucuları](#soz-07)
- [SOZ-08 Satış dili](#soz-08)
- [SOZ-09 Derin görünen özdeyişler](#soz-09)
- [SOZ-10 Temkin yığını](#soz-10)
- [SOZ-11 "Adeta" ve "sanki" ile örtme](#soz-11)
- [SOZ-12 Fiil şişirmesi: gerçekleştirmek, sağlamak, yapmak](#soz-12)
- [CEV-05 "Olanak sağlamak / mümkün kılmak" kalıbı](#cev-05)
- [CEV-06 "X konusuna gelecek olursak / değinecek olursak"](#cev-06)
- [CEV-07 "Sadece X ile sınırlı kalmayıp" kalıbı](#cev-07)
- [NOK-05 Eğik çizgiyle sıralama](#nok-05)
- [NOK-06 İki nokta enflasyonu ve "X şudur: Y"](#nok-06)
- [NOK-07 Noktalı virgül ve karşıtlık bağlacından önce virgül](#nok-07)
- [SAH-01 Tek satırlık dramatik kapanış](#sah-01)
- [SAH-02 Asıl sözden önce hazırlık cümlesi](#sah-02)
- [SAH-03 Kimseyle tartışmak](#sah-03)
- [SAH-04 Okurun bildiğini yeniden anlatmak](#sah-04)
- [SAH-05 "Unutulmamalıdır ki / Şunu unutmamak gerekir ki"](#sah-05)
- [PLZ-01 Plaza dili](#plz-01)
- [PLZ-02 Bürokratik edat yığını](#plz-02)
- [OTR-01 Belirsiz otorite](#otr-01)
- [OTR-02 Abartılmış önem ve tarihsellik](#otr-02)
- [OTR-03 Sahte denge ve çit üstünde oturma (fence-sitting)](#otr-03)
- [KAL-01 Sohbet kalıntısı ve bilgi sınırı feragati](#kal-01)
- [KAL-02 Metnin kendinden söz etmesi](#kal-02)

---

<a id="yapi-01"></a>
### YAPI-01 · Tekdüze dizilim ve eşit cümle uzunluğu

- **Belirti:** Paragraftaki cümlelerin neredeyse hepsi özne + tümleç + nesne + yüklem sırasında ve 14-22 sözcük arasında. Cümle başları birbirine benziyor.
- **Neden yapay:** İnsan yazısında uzunluk dalgalanır. Kısa bir cümle vurgu yapar, uzun bir cümle bağlamı açar. Dil modelleri ise "güvenli" orta uzunlukta toplanır.
- **Ne yapmalı:** Bir iki cümleyi birleştirin (zarf-fiil, sıfat-fiil), birini kısaltın, bir iki cümlede öğe sırasını değiştirin. Araçlar için bkz. `cumle-turleri.md`.
- **Dokunma:** Teknik talimat, sözleşme maddesi ve adım adım kılavuzda düzenli yapı bir erdemdir.
- **Önce:** *Şirketimiz 2015 yılında İzmir'de kurulmuştur. Ekibimiz yazılım geliştirme alanında uzmanlaşmış kişilerden oluşmaktadır. Müşterilerimize uçtan uca çözümler sunmaktayız. Projelerimizde çevik yöntemleri benimsemekteyiz.*
- **Sonra:** *2015'te İzmir'de kurulduk. Yazılım geliştirmede uzmanlaşmış ekibimizle müşterilerimize uçtan uca çözümler sunuyoruz. Projelerde çevik yöntemlerle çalışıyoruz.*

<a id="yapi-02"></a>
### YAPI-02 · ve/ama/çünkü tekeli

- **Belirti:** Bir paragrafta "ve" üçten çok, "ama" ya da "çünkü" ikiden çok geçiyor. Cümleler hep bu üç bağlaçla bağlanıyor.
- **Neden yapay:** Türkçede iki cümleyi bağlamanın en doğal yolu çoğu zaman bağlaç değil, ektir (-ıp, -ınca, -dığı için). Ayrıca karşıtlık ve sebep için çok zengin bir bağlaç envanteri vardır. Modeller İngilizcedeki *and/but/because* düzenini taşır.
- **Ne yapmalı:** Önce bağlacı silmeyi deneyin (nokta, virgül, zarf-fiil, "da/de"). Gerekiyorsa ilişkiye en uygun bağlacı seçin. Bkz. `baglaclar.md`.
- **Dokunma:** Sayılan öğeler arasındaki "ve" ("elma ve armut") doğaldır. Tek bir "ama" ya da "çünkü" sorun değildir.
- **Önce:** *Uygulama hızlı ve kullanımı kolay ama bazı özellikler eksik çünkü ekip küçük ve kaynaklar sınırlı.*
- **Sonra:** *Uygulama hızlı, kullanımı da kolay. Yine de bazı özellikler eksik: Ekip küçük, kaynaklar sınırlı.*

<a id="yapi-03"></a>
### YAPI-03 · -mektedir/-maktadır yığılması

- **Belirti:** Art arda cümleler "-mektedir, -maktadır, -ilmektedir, -mekteyiz" ile bitiyor.
- **Neden yapay:** Bu çekim resmi yazıda yerindedir, ama her cümlede kullanıldığında metin bürokratik ve ağır bir hal alır. İnsanlar resmi yazıda bile geniş zamanı (-ır/-ar), şimdiki zamanı (-yor) ve -dır'lı isim cümlesini karıştırarak kullanır.
- **Ne yapmalı:** Gündelik ve yarı resmi metinde çoğunu "-yor" ya da geniş zamana çevirin. Akademik ve resmi metinde bir kısmını koruyun, ama hepsini aynı ekle bitirmeyin: biri geniş zaman, biri isim cümlesi olabilir.
- **Dokunma:** Resmi yazışmada, mevzuat dilinde ve akademik metinde bu çekim registerin parçasıdır. Tamamen kaldırmayın, yalnızca yoğunluğunu azaltın.
- **Önce:** *Proje kapsamında veriler toplanmaktadır. Toplanan veriler analiz edilmektedir. Analiz sonuçları raporlanmaktadır.*
- **Sonra (gündelik):** *Projede önce verileri topluyoruz, sonra analiz edip raporluyoruz.*
- **Sonra (akademik):** *Proje kapsamında toplanan veriler analiz edilerek raporlanmaktadır.*

<a id="yapi-04"></a>
### YAPI-04 · Gereksiz edilgen yapı

- **Belirti:** Eylemi yapan belli olduğu hâlde edilgen kullanılıyor: "tarafımızca incelenmiştir", "kararlaştırılmıştır", "tavsiye edilmektedir".
- **Neden yapay:** Edilgen yapı nesnellik görüntüsü verir. Ancak eylemi yapan biliniyorsa metni dolaylı ve kaçamak gösterir.
- **Ne yapmalı:** Özne metinde açıkça varsa ya da konuşan belliyse etken yapıya çevirin. Özne belli değilse uydurmayın.
- **Dokunma:** Akademik yöntem bölümleri ("Örneklem rastgele seçilmiştir.") ve öznenin önemsiz olduğu durumlar.
- **Önce:** *Talebiniz tarafımızca incelenmiş olup gerekli düzenlemelerin yapılmasına karar verilmiştir.*
- **Sonra:** *Talebinizi inceledik ve gerekli düzenlemeleri yapmaya karar verdik.*

<a id="yapi-05"></a>
### YAPI-05 · Üçlü sıralama alışkanlığı

- **Belirti:** Sıfatlar, örnekler ve maddeler hep üçlü geliyor: "hızlı, güvenilir ve ölçeklenebilir", "verimlilik, şeffaflık ve sürdürülebilirlik".
- **Neden yapay:** Üçlü dizi retorikte güçlü bir kalıptır, ama modeller bunu bir refleks gibi her yerde kullanır. Üçüncü öğe çoğu zaman bilgi taşımaz, ritmi tamamlamak için eklenmiştir.
- **Ne yapmalı:** Gerçekten üç ayrı bilgi varsa koruyun. Biri ötekilerin tekrarıysa ya da boşsa (ve kaldırmak bilgi kaybına yol açmıyorsa) çıkarın ya da sayıyı değiştirin. **Dikkat:** Kaynakta somut bilgi taşıyan öğeyi silmek bilgi çıkarmaktır, yasaktır.
- **Dokunma:** Teknik özellik listeleri ve kaynakta gerçekten üç olgu sayılan cümleler.
- **Önce:** *Yeni panelimiz sezgisel, kullanıcı dostu ve kolay anlaşılır bir arayüz sunuyor.*
- **Sonra:** *Yeni panelin arayüzü kolay anlaşılıyor.* (Üç sıfat aynı şeyi söylüyor.)

<a id="yapi-06"></a>
### YAPI-06 · "Sadece X değil, aynı zamanda Y" kalıbı

- **Belirti:** "Bu sadece bir X değil, aynı zamanda bir Y", "Bu bir X değil, bir Y" kalıbı metinde tekrar ediyor.
- **Neden yapay:** İngilizce *not just X, but Y* kalıbının çevirisidir. Bir kez etkili olabilir. Tekrarlandığında yapay bir dramatiklik yaratır.
- **Ne yapmalı:** Doğrudan söyleyin. İki bilgi de önemliyse "hem ... hem" ya da iki ayrı cümle kullanın.
- **Dokunma:** Gerçek bir yanlış anlamayı düzelten tek bir kullanım ("Bu bir hata değil, bilinçli bir tercih.").
- **Önce:** *Bu uygulama sadece bir not defteri değil, aynı zamanda kişisel bir verimlilik asistanı.*
- **Sonra:** *Uygulama not almanın yanında verimliliğinizi artırmanıza da yardım ediyor.*

<a id="yapi-07"></a>
### YAPI-07 · Kendi sorup kendi cevaplama

- **Belirti:** "Peki bu ne anlama geliyor?", "Peki neden?", "Sonuç mu? ..." gibi sorular ve hemen ardından cevapları.
- **Neden yapay:** Okurun aklından geçmeyen bir soruyu sahnelemek, metne sahte bir konuşma havası verir.
- **Ne yapmalı:** Soruyu silip cevabı doğrudan söyleyin.
- **Dokunma:** Gerçekten okurun soracağı bir soruysa (SSS bölümü, öğretici bir blog) ve metinde bir kez geçiyorsa.
- **Önce:** *Peki bu değişiklik kullanıcılar için ne anlama geliyor? Kısacası, daha hızlı bir deneyim.*
- **Sonra:** *Değişiklikten sonra uygulama kullanıcılar için daha hızlı çalışıyor.*

<a id="yapi-08"></a>
### YAPI-08 · Her paragrafı özet cümlesiyle bitirme

- **Belirti:** Paragraflar az önce söyleneni tekrar eden bir cümleyle bitiyor: "Bu da gösteriyor ki ...", "Kısacası ...", "Dolayısıyla X büyük önem taşımaktadır."
- **Neden yapay:** Modeller her bölümü kapatma eğilimindedir. Okur ise aynı bilgiyi ikinci kez okumaya ihtiyaç duymaz.
- **Ne yapmalı:** Yeni bilgi taşımayan kapanış cümlesini silin. Yeni bilgi taşıyorsa (bir çıkarım, sonuç) yalnızca o kısmı tutun.
- **Dokunma:** Uzun raporların ve akademik makalelerin sonuç bölümü.
- **Önce:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü. Bu da müşteri memnuniyetinin ne kadar önemli olduğunu açıkça göstermektedir.*
- **Sonra:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü.*

---

<a id="soz-01"></a>
### SOZ-01 · "Önemli bir rol oynamaktadır" ailesi

- **Belirti:** önemli bir rol oynamaktadır, büyük önem taşımaktadır, kritik bir öneme sahiptir, vazgeçilmez bir unsurdur, ayrılmaz bir parçasıdır, hayati önem arz etmektedir.
- **Neden yapay:** Bu kalıplar bir şeyin önemli olduğunu söyler ama neden önemli olduğunu söylemez. Yerini somut bir yükleme bırakmalıdır.
- **Ne yapmalı:** Önemin ne olduğunu söyleyen fiili bulun ("etkiler", "belirler", "sağlar", "düşürür"). Kaynakta bu bilgi yoksa daha sade bir ifadeye indirin ("önemlidir"). Bilgi uydurmayın.
- **Dokunma:** Akademik metinde ölçülü ve tek kullanım.
- **Önce:** *Düzenli uyku, öğrencilerin akademik başarısında önemli bir rol oynamaktadır.*
- **Sonra:** *Düzenli uyku, öğrencilerin akademik başarısını etkiler.*

<a id="soz-02"></a>
### SOZ-02 · Geçiş ve bağlam klişeleri

- **Belirti:** bu bağlamda, bu çerçevede, söz konusu, göz önünde bulundurulduğunda, dikkate alındığında, günümüzde, son yıllarda, hızla gelişen dünyada, teknolojinin hızla ilerlediği günümüzde, sonuç olarak.
- **Neden yapay:** Bu sözler cümleler arasında bir bağ varmış izlenimi verir ama çoğu zaman hiçbir şey bağlamaz. "Günümüzde" ile başlayan açılış, yapay zekanın en tanıdık imzalarından biridir.
- **Ne yapmalı:** Silin ve cümlenin hâlâ ayakta durup durmadığına bakın. Çoğu zaman durur. "Söz konusu X"i "bu X" ya da yalnızca "X" yapın.
- **Dokunma:** Resmi yazışmada "söz konusu" belirli bir belgeyi işaret ediyorsa ("söz konusu sözleşme") kalabilir.
- **Önce:** *Teknolojinin hızla geliştiği günümüzde, yapay zeka birçok sektörü dönüştürmektedir. Bu bağlamda, söz konusu dönüşüm göz önünde bulundurulduğunda şirketlerin hazırlıklı olması gerekmektedir.*
- **Sonra:** *Yapay zeka birçok sektörü dönüştürüyor ve şirketlerin buna hazırlanması gerekiyor.*

<a id="soz-03"></a>
### SOZ-03 · Pekiştirme şişirmesi

- **Belirti:** oldukça, son derece, büyük ölçüde, son derece önemli, kritik, kilit, eşsiz, benzersiz, muazzam, inanılmaz, devrim niteliğinde.
- **Neden yapay:** Her şey "son derece" önemli olunca hiçbir şey önemli olmaz. Modeller tarafsız bilgiyi pekiştirmelerle süsler.
- **Ne yapmalı:** Pekiştirmeyi silin. Gerçek bir derece bilgisi varsa sayı ya da somut karşılaştırmayla verin (kaynakta varsa).
- **Dokunma:** Kaynakta ölçülebilir bir karşılığı olan tek bir pekiştirme.
- **Önce:** *Bu son derece kritik güncelleme, sistemin performansını büyük ölçüde artırarak eşsiz bir deneyim sunuyor.*
- **Sonra:** *Bu güncelleme sistemin performansını artırıyor.*

<a id="soz-04"></a>
### SOZ-04 · "olarak" ve "-mekte olup" fazlalığı

- **Belirti:** "şirket olarak", "ekip olarak", "genel olarak", "temel olarak", "aktif olarak", "düzenli olarak"; "-mekte olup", "-miş olup".
- **Neden yapay:** "Olarak" çoğu yerde bilgi taşımaz. "-mekte olup" ise iki cümleyi resmi yazışma havasında yapıştırır.
- **Ne yapmalı:** "Olarak"ı silin ya da ekle karşılayın ("düzenli olarak" → "düzenli"). "-mekte olup"u iki cümleye bölün ya da zarf-fiil kullanın.
- **Dokunma:** "Şirket olarak" konuşanın kurum adına konuştuğunu vurgulamak için bir kez kullanılabilir.
- **Önce:** *Şirket olarak müşterilerimizle aktif olarak iletişim kurmakta olup geri bildirimleri düzenli olarak değerlendirmekteyiz.*
- **Sonra:** *Müşterilerimizle sürekli iletişim kuruyor, geri bildirimleri düzenli değerlendiriyoruz.*

<a id="soz-05"></a>
### SOZ-05 · "Bu durum" / "Bu da" ile açılış

- **Belirti:** Art arda cümleler "Bu durum ...", "Bu da ...", "Bu sayede ...", "Bu noktada ..." ile başlıyor.
- **Neden yapay:** Cümleler arasında bağ kurmak için modeller önceki cümlenin tamamını "bu" ile işaret eder. Sık tekrarlanınca metin zincirleme bir hâl alır.
- **Ne yapmalı:** İki cümleyi birleştirin (sıfat-fiil, zarf-fiil) ya da "bu"nun neyi işaret ettiğini adıyla söyleyin.
- **Dokunma:** Bir paragrafta bir kez.
- **Önce:** *Sunucular yeni veri merkezine taşındı. Bu durum gecikmeyi azalttı. Bu da kullanıcı deneyimini iyileştirdi.*
- **Sonra:** *Sunucuların yeni veri merkezine taşınmasıyla gecikme azaldı, kullanıcı deneyimi iyileşti.*

<a id="soz-06"></a>
### SOZ-06 · Gösterişli mecaz öbekleri

- **Belirti:** yeni bir boyut kazandırmak, kapılarını aralamak, dönüşüm yolculuğu, yolculuğa çıkmak, yeni bir sayfa açmak, köprü kurmak, ufuk açıcı, çıtayı yükseltmek, potansiyelini açığa çıkarmak.
- **Neden yapay:** Somut bir bilgi yerine duygu yükü taşıyan genel mecazlar kullanılır. Kurumsal ve pazarlama metinlerinde yapay zekanın en bariz izidir.
- **Ne yapmalı:** Mecazın arkasındaki somut iddiayı yazın. Kaynakta somut bir iddia yoksa düz ve sade bir ifadeye indirin.
- **Dokunma:** Edebi metin ve kullanıcının bilinçli üslubu.
- **Önce:** *Bu iş birliği, eğitimde dijital dönüşüm yolculuğumuza yeni bir boyut kazandıracak.*
- **Sonra:** *Bu iş birliğiyle eğitimde dijitalleşme çalışmalarımızı genişleteceğiz.*

---

<a id="cev-01"></a>
### CEV-01 · Çeviri deyimler

- **Belirti:** günün sonunda (*at the end of the day*), derinlemesine dalmak (*deep dive*), oyunun kurallarını değiştiren (*game-changer*), masaya getirmek (*bring to the table*), bir adım öne çıkmak (*step up*), aynı sayfada olmak (*be on the same page*), kutunun dışında düşünmek (*think outside the box*), ileriye dönük (*going forward*), kazan-kazan.
- **Neden yapay:** İngilizce deyimlerin sözcük sözcük çevirisidir. Türkçe okur bunları ya yadırgar ya da "plaza dili" olarak algılar.
- **Ne yapmalı:** Türkçe karşılığını ya da düz anlamını kullanın: günün sonunda → sonuçta / nihayetinde; derinlemesine dalmak → ayrıntılı incelemek; oyunun kurallarını değiştiren → alışılmış düzeni değiştiren / çığır açan (ölçülü); masaya getirmek → katmak, sunmak; aynı sayfada olmak → aynı fikirde olmak, uzlaşmak.
- **Dokunma:** Kullanıcı bilinçli olarak plaza dili ya da ironik bir dil kullanıyorsa.
- **Önce:** *Bu yazıda yapay zekanın eğitimdeki rolüne derinlemesine dalacağız. Günün sonunda, bu teknoloji oyunun kurallarını değiştiren bir güç.*
- **Sonra:** *Bu yazıda yapay zekanın eğitimdeki yerini ayrıntılı olarak inceliyoruz. Sonuçta bu teknoloji, öğretimin alışılmış düzenini değiştiriyor.*

<a id="cev-02"></a>
### CEV-02 · "-e sahip olmak" fazlalığı

- **Belirti:** "geniş bir deneyime sahip", "yüksek bir performansa sahiptir", "üç odaya sahip", "önemli bir yere sahiptir".
- **Neden yapay:** İngilizce *have/has* yapısının çevirisidir. Türkçe bunu çoğu zaman "-lı/-li", "var" ya da doğrudan sıfatla söyler.
- **Ne yapmalı:** "-lı/-li" ekini, "var/yok" yapısını ya da isim cümlesini kullanın.
- **Dokunma:** Mülkiyet ya da hak vurgusu ("şirketin %51'ine sahip", "telif hakkına sahip").
- **Önce:** *Ekibimiz geniş bir deneyime sahip olup ürünümüz yüksek bir performansa sahiptir.*
- **Sonra:** *Ekibimiz deneyimli, ürünümüz de yüksek performanslı.*

<a id="cev-03"></a>
### CEV-03 · "tarafından" ve "için" yığılması

- **Belirti:** "X tarafından geliştirilen Y tarafından kullanılan", "bu, kullanıcılar için önemlidir", "işletmeler için faydalı olmak".
- **Neden yapay:** İngilizce *by* ve *for* yapılarının çevirisidir. Türkçede etken çatı ve yönelme durumu daha doğaldır.
- **Ne yapmalı:** "X tarafından yapılan" → "X'in yaptığı". "Y için önemli" → bağlama göre "Y'yi ilgilendirir", "Y'nin işine yarar".
- **Dokunma:** Resmi yazışmada ve akademik metinde tek bir "tarafından". Kurum adı geçen resmi bildirimler.
- **Önce:** *Ekibimiz tarafından geliştirilen bu araç, küçük işletmeler için oldukça faydalı olacaktır.*
- **Sonra:** *Ekibimizin geliştirdiği bu araç küçük işletmelerin işine yarayacak.*

<a id="cev-04"></a>
### CEV-04 · Gereksiz iyelik zamiri ve "bir"

- **Belirti:** "bizim ekibimiz", "sizin hesabınız", "onun fikri" (iyelik eki zaten varken). "Bir" sözcüğünün belirsiz tanımlık (*a/an*) gibi her ada eklenmesi: "harika bir fırsat sunan bir platform".
- **Neden yapay:** Türkçede iyelik eki kişiyi zaten gösterir. Zamir yalnızca vurgu için kullanılır. "Bir" ise İngilizcedeki tanımlık refleksiyle çoğalır.
- **Ne yapmalı:** Vurgu yoksa zamiri silin. Fazladan "bir"leri ayıklayın.
- **Dokunma:** Karşıtlık vurgusu ("Bizim ekibimiz değil, onların ekibi yaptı.").
- **Önce:** *Bizim ekibimiz sizin projeniz için harika bir çözüm sunan bir yaklaşım geliştirdi.*
- **Sonra:** *Ekibimiz projeniz için yeni bir yaklaşım geliştirdi.* ("harika" bilgi taşımıyor. "çözüm sunan" ise "yaklaşım"ın tekrarı.)

---

<a id="nok-01"></a>
### NOK-01 · Cümle içinde uzun çizgi (—)

- **Belirti:** Cümle içinde ara söz, açıklama ya da ani dönüş için "—" kullanılıyor.
- **Neden yapay:** TDK'ya göre uzun çizgi yalnızca satır başındaki konuşmaları gösterir. Cümle içindeki kullanım İngilizce tipografiden gelir ve yapay zeka metinlerinin en kolay fark edilen izidir.
- **Ne yapmalı:** Ara söz için virgül, -kısa çizgi- ya da ayraç. Açıklama için iki nokta. Ani dönüş için nokta ve yeni cümle. Bkz. `noktalama.md` §1.
- **Dokunma:** Satır başındaki diyalog çizgisi. Kullanıcının açıkça korumak istediği tipografi.
- **Önce:** *Toplantıda tek bir konu konuşuldu — bütçe. Herkes — finans ekibi de dahil — şaşırdı.*
- **Sonra:** *Toplantıda tek bir konu konuşuldu: bütçe. Finans ekibi de dâhil herkes şaşırdı.*

<a id="nok-02"></a>
### NOK-02 · "ve"den önce virgül

- **Belirti:** Sıralamada son öğeden önce "..., ve ..." (Oxford virgülü).
- **Neden yapay:** İngilizce noktalama kuralıdır. TDK'ya göre "ve, veya, ya da" öncesine virgül konmaz.
- **Ne yapmalı:** Virgülü silin.
- **Dokunma:** —
- **Önce:** *Tasarım, geliştirme, ve test aşamaları tamamlandı.*
- **Sonra:** *Tasarım, geliştirme ve test aşamaları tamamlandı.*

<a id="nok-03"></a>
### NOK-03 · İngilizce sayı ve yüzde biçimi

- **Belirti:** *25%*, *3.5 milyon*, *1,200 kişi*.
- **Neden yapay:** Türkçede yüzde işareti önde (*%25*), ondalık ayırıcı virgül (*3,5*), binlik ayırıcı noktadır (*1.200*).
- **Ne yapmalı:** Biçimi düzeltin, **değeri asla değiştirmeyin.** "1,200" ifadesinin binlik mi ondalık mı olduğu bağlamdan net değilse dokunmayın ve özette belirtin.
- **Dokunma:** Kod, sürüm numarası (*v2.5*), IP adresi, ürün kodu, alıntılanmış İngilizce veri.
- **Önce:** *Satışlar 12.5% artarak 3,400 adede ulaştı.*
- **Sonra:** *Satışlar %12,5 artarak 3.400 adede ulaştı.*

<a id="nok-04"></a>
### NOK-04 · Ünlem ve emoji bolluğu

- **Belirti:** Her paragraf ünlemle bitiyor. Madde başlarında 🚀 ✅ 💡 gibi emojiler var.
- **Neden yapay:** Sosyal medya için üretilmiş yapay zeka metninin tipik süslemesidir.
- **Ne yapmalı:** Ünlemleri metin başına en fazla bire indirin. Emojileri, kullanıcı açıkça istemedikçe kaldırın ya da bire indirin.
- **Dokunma:** Kullanıcının kendi markasının bilinçli sosyal medya dili.
- **Önce:** *Büyük haber! 🚀 Yeni ürünümüz yayında! Hemen deneyin! 💡*
- **Sonra:** *Yeni ürünümüz yayında. Hemen deneyebilirsiniz!*

---

<a id="bic-01"></a>
### BIC-01 · Gereksiz başlık, madde işareti ve kalın yazı

- **Belirti:** Üç paragraflık bir e-postada başlıklar, her cümlenin madde işaretine dönüşmesi, cümle ortalarında **kalın** yazılmış sözcükler.
- **Neden yapay:** Modeller her metni bir rapor gibi yapılandırır. Akıcı bir metin parçalanınca okur bağlantıları kendisi kurmak zorunda kalır.
- **Ne yapmalı:** Kısa metinde başlıkları kaldırın. Birbiriyle ilişkili maddeleri düzyazıya çevirin. Kalın yazıyı yalnızca gerçekten taranacak bilgi (tarih, son gün) için bırakın. **İçerik aynen korunmalıdır:** Maddedeki her bilgi düzyazıda da yer almalıdır.
- **Dokunma:** Adım adım talimatlar, gerçekten taranacak listeler, kullanıcının belirlediği şablon.
- **Önce:**
  ```
  **Konu:** Toplantı
  **Tarih:** Perşembe
  - Toplantı perşembe günü yapılacaktır.
  - Gündem bütçe planlamasıdır.
  - Katılım önemlidir.
  ```
- **Sonra:** *Perşembe günü bütçe planlamasını konuşmak için toplanıyoruz. Katılımınız önemli.*

---

<a id="dol-01"></a>
### DOL-01 · Açılış dolguları

- **Belirti:** "Harika bir soru!", "Elbette!", "Tabii ki, işte ...", "Bu yazıda ... ele alacağız", "Merhaba! Bugün sizlerle ... paylaşmak istiyorum".
- **Neden yapay:** Sohbet modelinin cevap refleksidir. Metne bilgi katmaz.
- **Ne yapmalı:** Silin, metin doğrudan konuyla başlasın.
- **Dokunma:** Mektup ve e-postadaki olağan selamlama ("Merhaba Ayşe Hanım,").
- **Önce:** *Harika bir soru! Bu yazıda uzaktan çalışmanın avantajlarını ele alacağız.*
- **Sonra:** *Uzaktan çalışmanın birkaç avantajı var.*

<a id="dol-02"></a>
### DOL-02 · Kapanış dolguları

- **Belirti:** "Umarım yardımcı olur!", "Başka sorunuz olursa çekinmeden sorun.", "Bu konuda daha fazla bilgi almak isterseniz ...", "Unutmayın, ...".
- **Neden yapay:** Sohbet modelinin kapanış refleksidir.
- **Ne yapmalı:** Silin. E-postada gerçek bir iletişim daveti gerekiyorsa sade bir kapanış bırakın ("Sorunuz olursa yazabilirsiniz.").
- **Dokunma:** E-postanın imza bloğu ve olağan kapanışı ("Saygılarımla,").
- **Önce:** *Umarım bu bilgiler size yardımcı olur! Başka bir sorunuz olursa çekinmeden sormaktan lütfen çekinmeyin.*
- **Sonra:** *(silinir)*

<a id="dol-03"></a>
### DOL-03 · Sıralama dolguları: "Öncelikle ... İkinci olarak ... Son olarak ..."

- **Belirti:** Paragraf ya da argüman başlarında düzenli olarak "Öncelikle,", "İkinci olarak,", "Üçüncü olarak,", "Son olarak," sayaçlarının kullanımı.
- **Neden yapay:** İngilizcedeki *First of all / Secondly / Lastly* düzeninin düzyazıya mekanik aktarımıdır. Türkçe düzyazıda bu sayaçlar yerine konuya doğrudan girilir ya da organik geçişler kullanılır.
- **Ne yapmalı:** Sıralama sayaçlarını kaldırın; argümanları veya eylemleri doğrudan söyleyin ya da zarf-fiil/doğal bağlaçla bağlayın.
- **Dokunma:** Adım adım teknik talimatlar, yemek tarifleri ve resmi yönergeler.
- **Önce:** *Öncelikle pazar araştırması yapılmalıdır. İkinci olarak prototip geliştirilmelidir. Son olarak kullanıcı testleri tamamlanmalıdır.*
- **Sonra:** *Önce pazar araştırması yapılır, ardından prototip geliştirilir ve kullanıcı testlerine geçilir.*

---

<a id="yaz-01"></a>
### YAZ-01 · Bağlaç de/da

- **Belirti:** "bende geliyorum", "Ali'de biliyor", "gidip te".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Bağlaç de/da'yı ayırın, kesmeyi kaldırın, "te/ta"yı "de/da" yapın. Bkz. `noktalama.md` §4.
- **Dokunma:** Bulunma eki (-de/-da/-te/-ta) bitişik kalır.
- **Önce:** *Bende bu toplantıya katılacağım, Elif'te gelecek.*
- **Sonra:** *Ben de bu toplantıya katılacağım, Elif de gelecek.*

<a id="yaz-02"></a>
### YAZ-02 · ki

- **Belirti:** "demekki", "halbuki" (TDK: hâlbuki), "yarın ki toplantı", "masada ki kitap".
- **Ne yapmalı:** Bağlaç "ki"yi ayırın (yedi kalıplaşmış söz hariç: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki). Ek olan "-ki"yi bitiştirin.
- **Dokunma:** —
- **Önce:** *Yarın ki toplantıda konuşacağız, demekki karar ertelendi.*
- **Sonra:** *Yarınki toplantıda konuşacağız, demek ki karar ertelendi.*

<a id="yaz-03"></a>
### YAZ-03 · Soru eki mi

- **Belirti:** "gelecekmisin", "doğrumu", "biliyormusun".
- **Ne yapmalı:** Soru ekini ayırın. Sonraki ekleri soru ekine bitiştirin.
- **Dokunma:** —
- **Önce:** *Raporu yarına yetiştirebilecekmisiniz?*
- **Sonra:** *Raporu yarına yetiştirebilecek misiniz?*

<a id="yaz-04"></a>
### YAZ-04 · Kesme işareti

- **Belirti:** Kurum adlarına kesme ("Türk Dil Kurumu'na"), yapım ekine kesme ("Türkiye'li"), kısaltmaya yanlış ünlü ("TDK'ya").
- **Ne yapmalı:** Kurum adlarında kesmeyi kaldırın, yapım ekinde ayırmayın, kısaltmaya gelen eki okunuşa uydurun. Bkz. `noktalama.md` §5.
- **Dokunma:** Kullanıcının marka adı yazımı (marka kendi adını tescilli olarak kesmeyle yazıyorsa).
- **Önce:** *Başvurular Ankara Üniversitesi'ne yapılacak, sonuçlar TDK'ya bildirilecek.*
- **Sonra:** *Başvurular Ankara Üniversitesine yapılacak, sonuçlar TDK'ye bildirilecek.*

<a id="yaz-05"></a>
### YAZ-05 · Büyük harf

- **Belirti:** "Kasım ayında" (genel zaman), "Türk Lirası" (para birimi), "İstanbul İli", iki noktadan sonra öbeğin büyük harfle başlaması.
- **Ne yapmalı:** Bkz. `noktalama.md` §3 ve §6.
- **Dokunma:** Başlıkların büyük harf düzeni (metin içinde tutarlıysa).
- **Önce:** *Fiyatlar Kasım ayında 500 Türk Lirası'na çıkacak. Üç seçenek var: Aylık, yıllık ve ömür boyu.*
- **Sonra:** *Fiyatlar kasım ayında 500 Türk lirasına çıkacak. Üç seçenek var: aylık, yıllık ve ömür boyu.*

---

<a id="yapi-09"></a>
### YAPI-09 · Tekrarlanan cümle açılışları

- **Belirti:** Art arda üç cümle aynı sözcük ya da yapıyla başlıyor: "Bu uygulama ... Bu uygulama ... Bu sayede ...", "Ayrıca ... Ayrıca ...", "Kullanıcılar ... Kullanıcılar ...".
- **Neden yapay:** Model her cümleyi bağımsız kurar ve özneyi her seferinde baştan söyler. Türkçe özneyi düşürmeye ve öğe sırasını oynatmaya çok elverişlidir.
- **Ne yapmalı:** Özne belliyse düşürün, cümleleri zarf-fiille birleştirin ya da birinin öğe sırasını değiştirin.
- **Dokunma:** Bilinçli paralellik (konuşma metni, slogan, adım listesi).
- **Önce:** *Uygulama verilerinizi yedekler. Uygulama ayrıca şifreleme kullanır. Uygulama her gün otomatik çalışır.*
- **Sonra:** *Uygulama verilerinizi her gün kendiliğinden, şifreleyerek yedekler.*

<a id="yapi-10"></a>
### YAPI-10 · Eş anlamlı rotasyonu

- **Belirti:** Aynı şeye bir paragrafta üç ayrı ad veriliyor: "platform ... sistem ... çözüm ... araç".
- **Neden yapay:** Model tekrar etmekten kaçınmak için eş anlamlı döndürür. Okur ise farklı adların farklı şeyler olduğunu sanabilir.
- **Ne yapmalı:** Bir ad seçin ve onu kullanın. Gerekirse öznesini düşürün.
- **Dokunma:** Metonim eş anlamlı değildir ("Türkiye / Ankara / hükümet" farklı şeyleri gösterebilir). Emin değilseniz dokunmayın.
- **Önce:** *Platform kullanıcılarına hızlı erişim sunuyor. Sistem ayrıca raporlama yapıyor. Çözüm, ekiplerin işini kolaylaştırıyor.*
- **Sonra:** *Platform hızlı erişim sunuyor, rapor da çıkarıyor. Ekiplerin işini kolaylaştırıyor.*

<a id="yapi-11"></a>
### YAPI-11 · Zincirleme isim tamlaması yığılması

- **Belirti:** Art arda 3-4 ismin birbirine bağlandığı hantal tamlamalar: "kullanıcı deneyimi optimizasyonu süreç yönetimi", "müşteri memnuniyeti artırma stratejisi planlaması".
- **Neden yapay:** İngilizce isim öbeklerinin (noun stacking) Türkçede yapay tamlama zincirlerine dönüştürülmesidir. Metnin nefes almasını ve okunmasını zorlaştırır.
- **Ne yapmalı:** Tamlamayı fiilimsilerle açın veya cümleye bölün: "kullanıcı deneyimini iyileştirme süreçleri".
- **Dokunma:** Yerleşik kurumsal unvanlar ve resmi proje/mevzuat adları.
- **Önce:** *Şirketimiz müşteri memnuniyeti artırma stratejisi planlaması üzerine odaklanmaktadır.*
- **Sonra:** *Şirketimiz müşteri memnuniyetini artırmaya yönelik planlara odaklanıyor.*

<a id="soz-07"></a>
### SOZ-07 · Vurgu doldurucuları

- **Belirti:** tam da, tam anlamıyla, gerçekten de, aslında, kesinlikle, esasen, nihayetinde, bir bakıma, gerçek anlamda, cümle başında dolgu "işte".
- **Neden yapay:** İngilizce *precisely, literally, indeed, ultimately* doldurucularının izidir. Türkçe vurguyu sözcük ekleyerek değil, dizilimle yapar.
- **Ne yapmalı:** Silin ve cümlenin anlamının değişmediğini kontrol edin. Vurgu gerekiyorsa vurgulanan öğeyi yüklemin hemen önüne alın.
- **Dokunma:** Gerçek bir karşıtlık bildiren "aslında" ("Herkes geç kaldığını sandı, aslında erken gelmişti.").
- **Önce:** *Bu yöntem gerçekten de tam anlamıyla işe yarıyor ve kesinlikle zaman kazandırıyor.*
- **Sonra:** *Bu yöntem işe yarıyor, zaman da kazandırıyor.*

<a id="soz-08"></a>
### SOZ-08 · Satış dili

- **Belirti:** kaçırılmayacak fırsat, hayatınızı kolaylaştıracak, bir üst seviyeye taşıyın, fark yaratın, mükemmel çözüm, tam size göre, hemen keşfedin.
- **Neden yapay:** Model nötr bilgiyi reklam metnine çevirir. Ürün metni dışında bu ses güveni azaltır.
- **Ne yapmalı:** Somut özelliği ya da faydayı söyleyin. Kaynakta yoksa sade bir cümleye indirin.
- **Dokunma:** Kullanıcının bilinçli reklam metni. Orada yalnızca yığılmayı azaltın.
- **Önce:** *Bu kurs, kariyerinizi bir üst seviyeye taşıyacak kaçırılmayacak bir fırsat.*
- **Sonra:** *Kurs, iş başvurularında istenen SQL becerilerini öğretiyor.* (Kaynakta "SQL" geçiyorsa. Geçmiyorsa: *Kurs kariyerinize katkı sağlayabilir.*)

<a id="soz-09"></a>
### SOZ-09 · Derin görünen özdeyişler

- **Belirti:** "Unutmayın, başarı bir varış noktası değil, bir yolculuktur.", "Değişim kaçınılmazdır, önemli olan ona nasıl uyum sağladığımızdır.", "başarının anahtarıdır", "işin sırrı", "büyük değişimler küçük adımlarla başlar". Yazar profiliyle yeniden yazarken de bu kalıplar kalmaz; profil yalnızca sesi belirler.
- **Neden yapay:** Paragrafı bilgece bir cümleyle kapatma refleksi. Bilgi taşımaz.
- **Ne yapmalı:** Silin. Arkasında somut bir öneri varsa onu düz söyleyin.
- **Dokunma:** Edebi metin, konuşma metni, kullanıcının kendi aforizması.
- **Önce:** *Yeni sisteme geçiş zor olabilir. Unutmayın, her büyük değişim küçük bir adımla başlar.*
- **Sonra:** *Yeni sisteme geçiş zor olabilir.*

<a id="soz-10"></a>
### SOZ-10 · Temkin yığını

- **Belirti:** Tek cümlede birden çok çekince: "genellikle çoğu durumda belirli ölçüde etkili olabileceği düşünülmektedir".
- **Neden yapay:** Model riskten kaçmak için çekinceleri üst üste koyar.
- **Ne yapmalı:** Yinelenen çekinceleri teke indirin. **Dikkat:** İddianın gücü değişmemeli. Kaynakta bir çekince varsa bir çekince kalır, hiç kalmazsa iddia güçlenmiş olur ve bu yasaktır.
- **Dokunma:** Akademik metinde gerçekten farklı iki belirsizliği anlatan çekinceler.
- **Önce:** *Bu ilacın genellikle çoğu hastada belirli ölçüde etkili olabileceği düşünülmektedir.*
- **Sonra:** *Bu ilaç çoğu hastada etkili olabilir.*

<a id="soz-11"></a>
### SOZ-11 · "Adeta" ve "sanki" ile örtme

- **Belirti:** "adeta bir zaman kapsülü", "sanki bir sanat eseri", "adeta bir şölen".
- **Neden yapay:** Somut bilgi yerine benzetme konur. Yapay zeka metinlerinde, özellikle gezi ve ürün tanıtımında, çok yoğundur.
- **Ne yapmalı:** Benzetmenin arkasındaki somut özelliği yazın. Kaynakta yoksa benzetmeyi silin.
- **Dokunma:** Edebi metin ve tek, yerinde bir benzetme.
- **Önce:** *Eski çarşı, adeta bir zaman kapsülü gibi ziyaretçileri geçmişe götürüyor.*
- **Sonra:** *Eski çarşının dükkânları yüz yıl önceki düzeniyle duruyor.* (Kaynakta bu bilgi varsa. Yoksa: *Eski çarşı tarihî dokusunu koruyor.*)

<a id="soz-12"></a>
### SOZ-12 · Fiil şişirmesi: gerçekleştirmek, sağlamak, yapmak

- **Belirti:** "toplantı gerçekleştirildi", "iletişim sağlandı", "kontrol sağlanması", "değerlendirme yapılması", "katılım gösterdi", "destek vermek".
- **Neden yapay:** Basit bir fiil, isim + yardımcı fiil öbeğine şişirilir. Türkçenin resmi yazışma alışkanlığıyla yapay zekanın uzatma eğilimi birleşir.
- **Ne yapmalı:** Asıl fiili kullanın: toplantı gerçekleştirildi → toplandık / toplantı yapıldı; iletişim sağlamak → iletişim kurmak / haberleşmek; kontrol sağlamak → kontrol etmek; katılım gösterdi → katıldı.
- **Dokunma:** Resmi tutanak ve mevzuat dili. Orada yalnızca yığılmayı azaltın.
- **Önce:** *Ekiple bir toplantı gerçekleştirilmiş ve sürecin kontrolünün sağlanması konusunda bir değerlendirme yapılmıştır.*
- **Sonra:** *Ekiple toplanıp süreci nasıl denetleyeceğimizi konuştuk.* (Kişi biz değilse: *Ekiple toplanıldı ve sürecin nasıl denetleneceği değerlendirildi.*)

<a id="cev-05"></a>
### CEV-05 · "Olanak sağlamak / mümkün kılmak" kalıbı

- **Belirti:** "X, Y yapmanıza olanak sağlar", "mümkün kılar", "imkân tanır", "kolaylık sağlar".
- **Neden yapay:** İngilizce *enable / allow you to* kalıbının çevirisidir. Türkçe bunu "-ebilmek" ya da doğrudan fiille söyler.
- **Ne yapmalı:** "Uygulama, dosyaları paylaşmanıza olanak sağlar" → "Uygulamayla dosyaları paylaşabilirsiniz."
- **Dokunma:** Metinde bir kez geçen ve vurgu taşıyan kullanım.
- **Önce:** *Yeni özellik, kullanıcıların raporları tek tıkla indirmesine olanak sağlamaktadır.*
- **Sonra:** *Yeni özellikle raporlar tek tıkla indirilebiliyor.*

<a id="cev-06"></a>
### CEV-06 · "X konusuna gelecek olursak / değinecek olursak"

- **Belirti:** "Fiyatlandırmaya gelecek olursak...", "Performans konusuna değinecek olursak...", "Güvenlik boyutuna bakacak olursak...".
- **Neden yapay:** İngilizce *When it comes to X / Moving on to X* kalıplarının çevirisidir. Konu geçişlerini pürüzsüz yapmak yerine yapay bir anons havası yaratır.
- **Ne yapmalı:** Kalıbı kaldırıp konuyu cümlenin doğal öznesi veya tümleci yapın.
- **Dokunma:** Sözlü sunumlar ve video/podcast konuşma metinleri.
- **Önce:** *Ürünün fiyatlandırma konusuna gelecek olursak, rakiplerine göre oldukça avantajlıdır.*
- **Sonra:** *Ürün rakiplerine göre daha uygun fiyatlı.*

<a id="cev-07"></a>
### CEV-07 · "Sadece X ile sınırlı kalmayıp" kalıbı

- **Belirti:** "...sadece bununla sınırlı kalmayıp aynı zamanda...", "...yalnızca X ile sınırlı değildir".
- **Neden yapay:** İngilizce *not limited to / not only... but also...* refleksinin Türkçeye gereksiz uzatılarak aktarılmasıdır.
- **Ne yapmalı:** "Sınırlı kalmayıp" dolgusunu silip "hem ... hem", "ayrıca" ya da "-le birlikte" ile bağlayın.
- **Dokunma:** Hukuki kapsam maddeleri ve garanti şartları.
- **Önce:** *Sistemimiz sadece masaüstüyle sınırlı kalmayıp mobil cihazlarda da sorunsuz çalışmaktadır.*
- **Sonra:** *Sistemimiz masaüstünün yanında mobil cihazlarda da sorunsuz çalışıyor.*

<a id="nok-05"></a>
### NOK-05 · Eğik çizgiyle sıralama

- **Belirti:** "kullanıcı/müşteri/üye", "öğrenci/öğretmen ilişkisi", "ve/veya".
- **Neden yapay:** İngilizce teknik yazımdan gelir. Türkçe metinde virgül ve "veya" ile yazılır.
- **Ne yapmalı:** "A, B veya C" ya da "A ile B" yapın. Anlam "ikisi de olabilir" ise "A ya da B (ya da ikisi)" yazın.
- **Dokunma:** Kod, dosya yolu, birim (km/sa), kesir, tarih (06/11/2026), sabit terim ("ön/arka yüz" gibi form alanları).
- **Önce:** *Kayıt sırasında öğrenci/veli/öğretmen bilgileri istenir.*
- **Sonra:** *Kayıt sırasında öğrenci, veli ve öğretmen bilgileri istenir.*

<a id="nok-06"></a>
### NOK-06 · İki nokta enflasyonu ve "X şudur: Y"

- **Belirti:** Bir paragrafta birden çok cümle-içi iki nokta. "Sorun şu: ...", "Kesin olan tek şey şudur: ...", "Cevap basit: ...".
- **Neden yapay:** İngilizcedeki *The thing is: / Here's the deal:* kalıbının çevirisidir. Bir kez etkili olabilir, tekrarlandığında sahnelenmiş bir gerilim yaratır (bkz. SAH-02).
- **Ne yapmalı:** Hazırlık kısmını silip asıl sözü doğrudan söyleyin. Açıklayıcı iki nokta paragrafta bir kez kalabilir.
- **Dokunma:** Sıralama öncesi iki nokta ("Üç belge gerekiyor: kimlik, diploma ve fotoğraf."), konuşma öncesi iki nokta.
- **Önce:** *Sorun şu: Sunucu yetmiyor. Çözüm basit: Yeni bir sunucu almak.*
- **Sonra:** *Sunucu yetmediği için yenisini almamız gerekiyor.*

<a id="nok-07"></a>
### NOK-07 · Noktalı virgül ve karşıtlık bağlacından önce virgül

- **Belirti:** Cümleleri noktalı virgülle bağlamak ("; ancak", "; ayrıca"). "Plan hazırdı, ancak ...", "Reform yapıldı, ama ..." yapısının metinde düzenli tekrarlanması.
- **Neden yapay:** İngilizce *; however* ve *, but* alışkanlığının Türkçeye aktarılmasıdır. Türkçe yazıda noktalı virgül seyrek kullanılır, "ama/ancak/fakat" öncesindeki virgül de çoğu zaman gereksizdir.
- **Ne yapmalı:** Noktalı virgülü noktaya çevirin ya da cümleleri birleştirin. Karşıtlık bağlacından önceki virgülü kaldırın: "Plan hazırdı ancak uygulamada aksadı."
- **Dokunma:** Noktalı virgülün gerçekten gerektiği yerler: içinde virgül olan öğeleri sıralamak ("Ankara, Çankaya; İzmir, Konak"), mevzuat ve sözleşme dili. Karşıtlık bağlacından önceki virgül, araya uzun bir ara söz girdiyse kalabilir.
- **Önce:** *Ekip hazırdı; ancak bütçe onaylanmadı, ama proje yine de başladı.*
- **Sonra:** *Ekip hazırdı ama bütçe onaylanmadı. Proje yine de başladı.*

<a id="sah-01"></a>
### SAH-01 · Tek satırlık dramatik kapanış

- **Belirti:** Paragraf, tek başına duran kısa ve etkili olmaya çalışan bir cümleyle bitiyor: "Ve bu her şeyi değiştirdi.", "Sonuç mu? Muhteşem.", "İşte fark bu."
- **Neden yapay:** Sosyal medya için üretilmiş yapay zeka metninin en tanıdık ritmidir. Bilgi taşımaz, yalnızca vurgu taklidi yapar.
- **Ne yapmalı:** Silin ya da önceki cümleye bilgi olarak katın. Yarım cümleyi tam cümleye tamamlayın.
- **Dokunma:** Blog ve deneme yazısında yazarın bilinçli tek bir vuruşu.
- **Önce:** *Sipariş sistemini yeniledik ve bekleme süresi 12 dakikadan 4 dakikaya indi. Ve bu her şeyi değiştirdi.*
- **Sonra:** *Sipariş sistemini yeniledik, bekleme süresi 12 dakikadan 4 dakikaya indi.*

<a id="sah-02"></a>
### SAH-02 · Asıl sözden önce hazırlık cümlesi

- **Belirti:** "Şunu söylemek gerekir ki ...", "Gelelim asıl meseleye.", "İşin ilginç yanı şu ...", "Bir şeyi açıkça belirtmek isterim: ...", "Peki, bu ne anlama geliyor?"
- **Neden yapay:** Model söyleyeceği şeyi duyurmakla zaman kazanır. Okur duyuruya değil, sözün kendisine ihtiyaç duyar.
- **Ne yapmalı:** Hazırlık cümlesini silin, asıl sözle başlayın.
- **Dokunma:** Konuşma metni ve sunum notları.
- **Önce:** *Şunu açıkça belirtmek gerekir ki, bu yıl satışlar düştü.*
- **Sonra:** *Bu yıl satışlar düştü.*

<a id="sah-03"></a>
### SAH-03 · Kimseyle tartışmak

- **Belirti:** "Birçok kişi X'in kolay olduğunu düşünür, ancak ...", "Sanılanın aksine ...", "Yaygın bir yanılgıdır ki ...".
- **Neden yapay:** Model, kimsenin ileri sürmediği bir görüşü kurup çürüterek metne gerilim ekler. Okur o görüşte değilse, metin onu yanlış bir yere yerleştirmiş olur.
- **Ne yapmalı:** Kurgulanmış görüşü silip doğru bilgiyi doğrudan söyleyin.
- **Dokunma:** Kaynakta gerçekten yaygın bir yanılgı anlatılıyorsa (adı ya da kaynağıyla).
- **Önce:** *Birçok kişi kompostun kötü koktuğunu düşünür, ancak doğru yapıldığında koku oluşmaz.*
- **Sonra:** *Doğru yapılan kompost kokmaz.*

<a id="sah-04"></a>
### SAH-04 · Okurun bildiğini yeniden anlatmak

- **Belirti:** Uzmana yazılan metinde temel kavramın tanımı ("E-posta, elektronik ortamda gönderilen bir mesajdır."), herkesin bildiği bağlamın uzun açıklaması.
- **Neden yapay:** Model okurun kim olduğunu bilmez ve her metni sıfırdan anlatır.
- **Ne yapmalı:** Okurun zaten bildiği açıklamayı silin.
- **Dokunma:** Başlangıç düzeyi eğitim metni, terimler sözlüğü.
- **Önce:** *Değerli ekip arkadaşlarım, bildiğiniz üzere yazılım geliştirme, bilgisayar programlarının tasarlanması ve yazılması sürecidir. Bu sprintte ödeme modülünü bitireceğiz.*
- **Sonra:** *Bu sprintte ödeme modülünü bitireceğiz.*

<a id="sah-05"></a>
### SAH-05 · "Unutulmamalıdır ki / Şunu unutmamak gerekir ki"

- **Belirti:** "Unutulmamalıdır ki...", "Şunu unutmamak gerekir ki...", "Gözden kaçırılmaması gereken bir diğer husus...".
- **Neden yapay:** SAH-02 benzeri bir hazırlık ve sahte bilgece uyarı kalıbıdır. Okura akıl öğretme havası verir.
- **Ne yapmalı:** Kalıbı silin, asıl bilgiyi doğrudan söyleyin.
- **Dokunma:** Güvenlik uyarıları ve yasal sorumluluk reddi metinleri.
- **Önce:** *Unutulmamalıdır ki, düzenli yedekleme yapılmadığı takdirde veri kaybı yaşanabilir.*
- **Sonra:** *Düzenli yedekleme yapılmazsa veri kaybı yaşanabilir.*

<a id="plz-01"></a>
### PLZ-01 · Plaza dili

- **Belirti:** aksiyon almak, feedback vermek, toplantı set etmek, update geçmek, ownership almak, deadline'a yetiştirmek, challenge etmek, align olmak, efor sarf etmek.
- **Neden yapay:** İş yazışmasında İngilizce sözcüğün Türkçe yardımcı fiille birleştirilmesidir. Yapay zeka bu dili kurumsal metinlerde aşırı kullanır.
- **Ne yapmalı:** Türkçe karşılığını kullanın: aksiyon almak → harekete geçmek / önlem almak; feedback vermek → geri bildirim vermek / görüş bildirmek; toplantı set etmek → toplantı ayarlamak; update geçmek → bilgi vermek; align olmak → uzlaşmak / aynı noktada buluşmak.
- **Dokunma:** Ekibin günlük iç yazışması ve kullanıcının bilinçli olarak kullandığı terimler (sektör terimi hâline gelmiş "sprint", "deploy" gibi).
- **Önce:** *Bu konuda aksiyon almak için yarın bir toplantı set edelim, herkes feedback'ini paylaşsın.*
- **Sonra:** *Yarın toplanıp ne yapacağımıza karar verelim. Herkes görüşünü getirsin.*

<a id="plz-02"></a>
### PLZ-02 · Bürokratik edat yığını

- **Belirti:** konusunda, hususunda, nezdinde, itibarıyla, kapsamında, doğrultusunda, istikametinde, mahiyetinde, bakımından.
- **Neden yapay:** Resmi dilin edatları, gerekmeyen yerde ve art arda kullanılır.
- **Ne yapmalı:** Edatı silip ekle anlatın ya da daha sade bir edat kullanın: "ödeme konusunda bilgi vermek" → "ödemeyle ilgili bilgi vermek" ya da "ödemeyi anlatmak".
- **Dokunma:** Resmi yazışma ve mevzuatta yerleşik kalıplar ("1 Ocak itibarıyla", "proje kapsamında" bir kez).
- **Önce:** *Talebiniz doğrultusunda, sözleşme kapsamında, ödeme hususunda tarafınıza bilgi verilecektir.*
- **Sonra:** *Talebiniz üzerine ödemeyle ilgili size bilgi vereceğiz.* (Resmi yazışmada: *Talebiniz üzerine, sözleşmedeki ödeme koşulları hakkında tarafınıza bilgi verilecektir.*)

<a id="otr-01"></a>
### OTR-01 · Belirsiz otorite

- **Belirti:** "Uzmanlar ... belirtiyor", "Araştırmalar gösteriyor ki ...", "Bilim insanlarına göre ...", "Yapılan çalışmalar ortaya koymuştur ki ..." (kaynak adı yok).
- **Neden yapay:** Model iddiayı güçlendirmek için adı olmayan bir otoriteye dayanır. Okur kaynağı soramaz.
- **Ne yapmalı:** Kaynakta adı varsa adıyla yazın. Yoksa **kaynak uydurmayın** ve otoriteyi **silmeyin**: silerseniz iddia yazarın kendi kesin bilgisi gibi görünür ve güçlenir. Kalıbı sadeleştirin ama iddianın aktarılmış olduğu belli kalsın ("Araştırmalara göre", "... deniyor"). Metnin altına "kaynak belirtilmemiş" notu düşün.
- **Dokunma:** Kaynak adı metnin başka bir yerinde verilmişse.
- **Önce:** *Yapılan araştırmalar gösteriyor ki günde 10.000 adım atmak sağlık için şarttır.*
- **Sonra:** *Araştırmalara göre günde 10.000 adım atmak sağlık için şart.* + not: "Kaynak belirtilmemiş, iddia doğrulanmalı."

<a id="otr-02"></a>
### OTR-02 · Abartılmış önem ve tarihsellik

- **Belirti:** "tarihi bir dönüm noktası", "yeni bir çağın başlangıcı", "sektörde devrim", "eşi benzeri görülmemiş", "her şeyi değiştirecek".
- **Neden yapay:** Model sıradan bir gelişmeyi büyük bir anlatıya bağlar.
- **Ne yapmalı:** Ne olduğunu ölçüsüyle söyleyin. Kaynakta karşılaştırma ya da sayı varsa onu kullanın.
- **Dokunma:** Gerçekten tarihi bir olayı anlatan metin.
- **Önce:** *Belediyenin yeni otobüs hattı, şehrin ulaşım tarihinde yeni bir çağın başlangıcı oldu.*
- **Sonra:** *Belediye yeni bir otobüs hattı açtı.*

<a id="otr-03"></a>
### OTR-03 · Sahte denge ve çit üstünde oturma (fence-sitting)

- **Belirti:** Karşılaştırmalı veya tartışmalı konularda net bir argüman kurmaktan kaçınıp *"Her ne kadar X avantajlı olsa da Y'nin de göz ardı edilemeyecek yönleri bulunmaktadır. Dolayısıyla en iyi yaklaşım dengeli bir yol izlemektir."* gibi kalıplarla bitirme.
- **Neden yapay:** Modellerin tarafsız kalma eğitiminden (RLHF) kaynaklanan refleksidir. Metnin bir yere varmasını engeller.
- **Ne yapmalı:** İçi boş orta yol cümlelerini silin; kaynakta somut argümanlar varsa bırakın ama yapay uzlaşma kalıbını kaldırın.
- **Dokunma:** Tarafsız haber metinleri ve çok sesli bilimsel derlemeler.
- **Önce:** *Uzaktan çalışmanın esneklik gibi avantajları olsa da ofiste çalışmanın da sosyalleşme gibi faydaları vardır. Sonuçta en doğrusu her iki yaklaşımın dengeli bir sentezini yapmaktır.*
- **Sonra:** *Uzaktan çalışma esneklik sunarken ofiste çalışma yüz yüze iletişimi kolaylaştırıyor.*

<a id="kal-01"></a>
### KAL-01 · Sohbet kalıntısı ve bilgi sınırı feragati

- **Belirti:** "Bir yapay zeka olarak ...", "Son bilgilerime göre ...", "2023 itibarıyla ...", "[buraya şirket adını ekleyin]", "Tabii, işte metniniz:", "Umarım beğenirsiniz!".
- **Neden yapay:** Metin bir sohbet cevabından kopyalanmış ve temizlenmemiştir.
- **Ne yapmalı:** Kalıntıyı silin. Doldurulmamış yer tutucuyu silmeyin, olduğu gibi bırakıp kullanıcıya not düşün (bilgi uydurmayın).
- **Dokunma:** —
- **Önce:** *Tabii, işte duyuru metniniz: Değerli müşterilerimiz, [tarih] tarihinde bakım çalışması yapılacaktır.*
- **Sonra:** *Değerli müşterilerimiz, [tarih] tarihinde bakım çalışması yapılacak.* + not: "[tarih] doldurulmamış."

<a id="kal-02"></a>
### KAL-02 · Metnin kendinden söz etmesi

- **Belirti:** "Bu yazıda ... ele alacağız", "Bu makale ... incelemeyi amaçlamaktadır", başlığın ilk cümlede aynen tekrarı, "Aşağıda ... bulabilirsiniz".
- **Neden yapay:** Model içerik yerine içeriğin tanıtımını yazar.
- **Ne yapmalı:** Duyuruyu silip doğrudan içerikle başlayın.
- **Dokunma:** Akademik makalenin özeti ve giriş bölümündeki amaç cümlesi (registerin parçası), uzun raporun yol haritası.
- **Önce:** *Başlık: Evde Kompost Yapımı. Bu yazıda evde kompost yapımını adım adım ele alacağız. Kompost, ...*
- **Sonra:** *Başlık: Evde Kompost Yapımı. Kompost, ...*

---

## Yeni örüntü şablonu

Aşağıdaki bloğu kopyalayın, uygun kategoriye ekleyin, sıradaki numarayı verin ve dizine bir satır ekleyin.

```markdown
<a id="kat-nn"></a>
### KAT-NN · Kısa ad

- **Belirti:** Metinde nasıl görünür? Somut sözcükler ya da yapılar.
- **Neden yapay:** İnsan yazısından nasıl ayrışıyor? Kaynağı nedir (çeviri, model refleksi...)?
- **Ne yapmalı:** Hangi dönüşüm uygulanmalı? İlgili referans dosyasına bağlantı verin.
- **Dokunma:** Örüntünün meşru olduğu durumlar. Bu satır zorunludur.
- **Önce:** *Özgün, yapay zeka tarzında bir örnek.*
- **Sonra:** *Anlamı, sayıları ve özel isimleri aynen koruyan düzeltilmiş hali.*
```
