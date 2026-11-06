# Humanizer TR

Türkçe metinlerdeki yapay zeka izlerini temizleyen bir Claude skill'i. Metni iyi bir
Türk yazarın yazacağı hâle getirir, **söylediği hiçbir şeyi değiştirmeden**: sayılar,
tarihler, özel isimler ve iddiaların kesinliği aynen kalır, yeni bilgi eklenmez.

Türkçede yapay zeka izi sözcüklerden çok yapıda görülür: "-mektedir" yığını, eşit
uzunlukta cümleler, çeviri kokan kalıplar, plaza dili, İngilizce noktalama, sahnelenmiş
vurgu ("Sonuç mu? ..."). Skill bunları 11 kategoride 53 örüntüyle tanır. Her örüntünün
önce/sonra örneği ve "dokunma" satırı vardır, yani hangi durumda doğal olduğu da yazılıdır.

Amaç yapay zeka dedektörlerini atlatmak değil, okunur ve doğru bir metin.

## Ne yapar

- **Metin türünü kendisi tanır.** Hukuki, akademik, iş yazışması, gazetecilik,
  blog/sosyal medya, edebi. Resmi metin resmi kalır, ritim düzenlemesi yalnızca türün
  izin verdiği kadar yapılır.
- **Soru sormaz.** Metni verirsiniz, düzeltilmiş metni alırsınız.
- **Sizin gibi yazar.** Kendi yazılarınızdan iki üç parça verirseniz sık kullandığınız
  sözcükleri, bağlaçları ve noktalama alışkanlığınızı çıkarıp metni o sesle yazar.
  Örneklerdeki olayları yeni metne taşımaz, yalnızca sesi alır.
- **Kaynak uydurmaz.** "Uzmanlara göre", "Araştırmalar gösteriyor" gibi kaynaksız bir
  iddia görürse ne kaynak ekler ne de iddiayı siler. İddiayı bırakır ve altına
  "kaynak belirtilmemiş" notu düşer.
- **Analiz modu.** "Bu metin yapay zeka mı, analiz et" derseniz metne dokunmadan
  bulduğu örüntüleri, yerlerini ve yoğunluğunu listeler. "Kesin yapay zeka yazdı"
  gibi bir hüküm vermez.

## Kurulum

| Nerede | Nasıl |
|---|---|
| Claude Code | `humanizer-tr/` klasörünü `~/.claude/skills/` altına kopyalayın. |
| Claude.ai | `dist/humanizer-tr.zip` dosyasını Ayarlar > Yetenekler (Skills) bölümünden yükleyin. |
| ChatGPT, Gemini vb. | `dist/humanizer-tr-tek-dosya.md` dosyasını sohbete ya da özel talimatlara ekleyin. |

Kullanım: "Bu metni insanlaştır", "AI kokuyor, düzelt", "daha doğal yaz", "şu paragrafı
benim gibi yaz" gibi bir istekle metni verin.

## Örnekler

Aşağıdaki çıktıların hepsi aynı model (Claude Sonnet) ile, aynı metin üzerinde, yalnızca
skill değiştirilerek alındı. Kıyas için Türkçe için yazılmış iki açık kaynak skill
kullanıldı: [DevVettel/turkish-humanizer](https://github.com/DevVettel/turkish-humanizer)
ve [bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer). Bu proje
ikisinin üzerine kuruldu (bkz. Teşekkür). Her skill her metinde birer kez çalıştırıldı;
bu bir ölçüm çalışması değil, fark gösteren örnektir.

### 1. Yöneticiye e-posta (plaza dili)

**Kaynak**

> Şunu belirtmek isterim ki, geçen hafta gerçekleştirilen toplantı sonrasında ödeme
> modülü konusunda gerekli aksiyonların alınması hususunda ekip olarak align olduk. Bu
> bağlamda, yeni ödeme akışı kullanıcıların 3 adımda ödeme yapmasına olanak
> sağlamaktadır; ancak test sürecinin tamamlanması için ek efor sarf edilmesi
> gerekmektedir.
>
> Uzmanlar, ödeme adımlarının azaltılmasının dönüşümü %20 artırdığını belirtiyor. Sonuç
> mu? Daha mutlu kullanıcılar.
>
> Deadline olan 14 Kasım'a yetiştirmek adına cuma günü bir toplantı set etmeyi
> öneriyorum. Feedback'lerinizi bekliyorum.

**DevVettel**

> ... ödeme modülü için gerekli aksiyonlar konusunda ekip olarak align olduk. ... test
> sürecinin tamamlanması için ek efor gerekiyor. ... Deadline olan 14 Kasım'a
> yetiştirmek için cuma günü bir toplantı set etmeyi öneriyorum. Feedback'lerinizi
> bekliyorum.

Plaza dili ("align", "aksiyon", "efor", "set etmek", "deadline", "feedback") kaldı.

**bushrabeg**

> ... Uzmanlara göre ödeme adımlarını azaltmak dönüşümü %20 artırıyor. Bunun sonucunda
> kullanıcılar daha memnun olacak.

Plaza dili temizlendi. Ama "daha mutlu kullanıcılar" kesin bir gelecek tahminine döndü
ve kaynaksız iddia için uyarı yok.

**Humanizer TR**

> Geçen haftaki toplantıdan sonra ödeme modülüyle ilgili atılacak adımlar konusunda ekip
> olarak uzlaştık. Yeni ödeme akışıyla kullanıcılar 3 adımda ödeme yapabiliyor ama
> testlerin tamamlanması için ek emek gerekiyor.
>
> Ödeme adımlarını azaltmanın dönüşümü %20 artırdığı belirtiliyor. Sonuçta kullanıcılar
> daha mutlu.
>
> Son tarih olan 14 Kasım'a yetişmek için cuma günü bir toplantı ayarlamayı öneriyorum.
> Görüşlerinizi bekliyorum.
>
> *Not: "Dönüşümü %20 artırıyor" iddiasının kaynağı metinde yok. ... göndermeden önce
> kaynağı ekleyin ya da bu cümleyi kaldırın.*

### 2. Instagram açıklaması (sahnelenmiş vurgu)

**Kaynak**

> Peki sabah rutini gerçekten bu kadar önemli mi? Kesinlikle evet! 🌅
>
> Birçok kişi erken kalkmanın sadece bir alışkanlık olduğunu düşünür, ancak bu tam
> anlamıyla bir yaşam felsefesidir. Araştırmalar gösteriyor ki sabah 6'da kalkanlar
> günün geri kalanında %15 daha verimli oluyor.
>
> Benim rutinim şu: 10 dakika esneme, 1 bardak su, 15 dakika kitap. Adeta güne yeniden
> doğmak gibi. ✨
>
> Unutmayın, büyük değişimler küçük adımlarla başlar. Ve bu her şeyi değiştirir. 💪

**DevVettel**

> ... Büyük değişimler küçük adımlarla başlar, bu da her şeyi değiştirir.

Özdeyiş ve dramatik kapanış kaldı.

**bushrabeg**

> ... Güne yeniden doğmak gibi bir his veriyor ✨
>
> Büyük değişimler küçük adımlarla başlar, bu üç küçük adım da günümü baştan sona
> değiştirdi 💪

Üç emoji kaldı ve kaynakta olmayan bir iddia eklendi ("günümü baştan sona değiştirdi").

**Humanizer TR**

> Sabah rutini gerçekten bu kadar önemli mi? Evet. 🌅
>
> Erken kalkmak bir alışkanlıktan fazlası, bir yaşam felsefesi. Araştırmalara göre sabah
> 6'da kalkanlar günün geri kalanında %15 daha verimli oluyor.
>
> Benim rutinim şöyle: 10 dakika esneme, 1 bardak su, 15 dakika kitap. Güne yeniden
> doğmak gibi.
>
> *Not: "Araştırmalar gösteriyor ki" cümlesinde kaynak belirtilmemiş. %15 oranı
> doğrulanmalı, doğrulanamıyorsa cümle çıkarılabilir.*

### 3. "Benim gibi yaz" (yazar profili)

Kullanıcı kendi yazılarından iki parça verdi. Parçalarda "açıkçası", "bence", "yani"
sık geçiyor, cümleler kısa ve parantez içi yorumlar var.

**Kaynak**

> Yeni bir programlama dili öğrenmek, sabır ve disiplin gerektiren bir süreçtir. Bu
> süreçte en önemli unsur, temel kavramların derinlemesine anlaşılmasıdır. Ayrıca düzenli
> pratik yapılması, öğrenmenin kalıcı hale gelmesinde kritik bir rol oynamaktadır. Sonuç
> olarak, acele etmeden adım adım ilerlemek başarının anahtarıdır.

**Humanizer TR**

> Yeni bir programlama dili öğrenmek sabır ister, disiplin ister. Bence en önemli şey
> temel kavramları derinlemesine anlamak. Bir de düzenli pratik var (öğrenmenin kalıcı
> olması buna bağlı). Yani acele etmeden, adım adım ilerlemek lazım.

Kullanıcının örneklerindeki anılar ("ilk hafta", "üç proje") yeni metne taşınmadı.

## Örüntü kategorileri

| Önek | Kategori | Örnek |
|---|---|---|
| `YAPI` | Cümle ve paragraf yapısı | "-mektedir" yığını, eşit uzunlukta cümleler |
| `SOZ` | Klişe ve şişirilmiş sözcük | "önemli bir rol oynamaktadır", "gerçekleştirmek" |
| `CEV` | Çeviri kokan ifade | "olanak sağlamak", "-e sahip olmak" |
| `NOK` | Noktalama | uzun çizgi (—), noktalı virgül, eğik çizgi |
| `BIC` | Biçim | kısa e-postada başlık ve madde işareti |
| `DOL` | Açılış ve kapanış dolgusu | "Günümüz dünyasında", "Sonuç olarak" |
| `YAZ` | Yazım | de/da, ki, mi, kesme işareti |
| `SAH` | Sahneleme | "Sonuç mu? ...", "Ve bu her şeyi değiştirir." |
| `PLZ` | Plaza ve bürokrasi dili | "align olmak", "hususunda" |
| `OTR` | Ödünç otorite | "Uzmanlara göre" (kaynaksız) |
| `KAL` | Sohbet kalıntısı | "İşte düzenlenmiş metin:", doldurulmamış `[İSİM]` |

Tam liste: [`humanizer-tr/references/ai-oruntuleri.md`](humanizer-tr/references/ai-oruntuleri.md)

## Proje yapısı

```
humanizer-tr/
  SKILL.md                 çalışma adımları ve değişmez kurallar
  references/              örüntü kataloğu, cümle türleri, bağlaçlar, noktalama, yazar profili
  examples/                beş metin türü için önce/sonra çiftleri
  evals/                   test vakaları (claude plugin eval biçimi)
scripts/tek-dosya-olustur.py   dist/ çıktılarını üretir
dist/                      Claude.ai zip'i ve tek dosya sürümü
```

## Katkı

Yeni örüntü, daha iyi örnek ya da anlam kayması bildirimi için
[`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasına bakın.

## Teşekkür

- [DevVettel/turkish-humanizer](https://github.com/DevVettel/turkish-humanizer) (MIT):
  taban. Anlam koruma kuralları, örüntü kataloğunun ilk 30 maddesi, cümle türleri,
  bağlaçlar, TDK noktalama notları, örnekler, test vakaları ve dist script'i buradan geldi.
- [bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer) (MIT):
  yazar profili fikri ve güçlü cümle örnekleri. Burada profil soru sormadan, yalnızca
  örnek verildiğinde kullanılır.
- [blader/humanizer](https://github.com/blader/humanizer) ve Wikipedia "Signs of AI
  writing": `SAH`, `OTR`, `KAL` kategorilerindeki dilden bağımsız kalıplar.

## Lisans

MIT. Bkz. [LICENSE](LICENSE).
