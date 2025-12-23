## Üsküdar Üniversitesi Haftalık Etkinlik Programı Tasarım Sistemi (Web)

Bu proje, haftalık etkinlikleri web arayüzünden girip **tasarıma dönüştürmenizi** ve **PNG olarak indirmenizi** sağlar.

### En önemli hedef: Başkaları da kullanabilsin
- Projeyi **GitHub Pages/Netlify/Vercel** üzerinde yayınlayarak herkesin erişmesini sağlayabilirsiniz.
- Logoların herkes için görünmesi için **`logos.json`** dosyasını repo’ya koymanız gerekir (aşağıda anlatılıyor).

## 📋 Özellikler

- ✅ Etkinlik ekleme/düzenleme arayüzü
- ✅ “Tasarıma Dönüştür” ile tasarım çıktısı
- ✅ “Tasarımı İndir” ile PNG indirme
- ✅ Kulüp logo yönetimi (tekil yükleme + toplu içe aktarma)
- ✅ ÜÜ/SKS header logoları
- ✅ GitHub Pages uyumlu ortak logo verisi (`logos.json`)

## 🚀 Kullanım (Web)

1. `index.html` dosyasını açın.
2. Etkinlikleri ekleyin.
3. **Tasarıma Dönüştür** → tasarım önizlemeyi üretir.
4. **Tasarımı İndir** → PNG indirir.

### Önemli not (file:// ile açıyorsanız)
Chrome, `file://` altında bazı görselleri canvas’a çizdirmediği için indirme boş çıkabilir. Bunun için:
- **Logo Yönetim Paneli → Toplu Logo İçe Aktar (Klasör Seç)** kullanın (logolar base64 olur).

## 🌍 Başkaları da kullansın (Paylaşımlı kullanım)

### GitHub Pages (Önerilen)
1. Projeyi GitHub’a yükleyin (`index.html` zorunlu).
2. Repo → **Settings → Pages** → yayınlayın.
3. Site açıldıktan sonra:
   - Logo Yönetim Paneli’nde logoları yükleyin
   - **“JSON’a Aktar (GitHub için)”** ile `logos.json` indirin
   - `logos.json` dosyasını repo’nun ana dizinine koyup push edin

Bu sayede siteye giren herkes aynı logoları görür (localStorage/IndexedDB cihazdan cihaza taşınmaz).

Detaylar için `GITHUB_PAGES.md` dosyasına bakın.

---

## (Legacy) E-posta üretimi
Repo’da geçmişten kalan `generate-email.js/.py` ve `output-email.html` dosyaları bulunabilir; güncel akış web tabanlı tasarım/indirme üzerinedir.

## 📁 Dosya Yapısı

```
Tasarım/
├── index.html             # Ana uygulama (web)
├── logos/                 # (Opsiyonel) logo dosyaları
├── logos.json             # (Önerilen) paylaşımlı base64 logolar + header (GitHub Pages için)
├── GITHUB_PAGES.md        # Yayınlama rehberi
└── README.md              # Bu dosya
```

## 🎨 Tasarım Özellikleri

- **Renk Paleti:**
  - Ana arka plan: `#1a5f5f` (Koyu teal)
  - Gün bölümleri: `#2a7a7a` (Açık teal)
  - Vurgu rengi: `#ffd700` (Altın sarısı)
  - Metin: Beyaz ve altın sarısı

- **Yapı:**
  - Üst başlık: Üniversite logosu ve başlık
  - Tarih banner'ı: Sarı arka planlı hafta bilgisi
  - Günlük bölümler: Her gün için ayrı bölüm
  - Etkinlik kartları: Kulüp ikonu, adı, etkinlik başlığı, saat ve konum
  - Alt bilgi: Web sitesi ve sosyal medya linkleri

## 📧 E-Posta Gönderimi

Oluşturulan HTML dosyasını e-posta gönderim servisinize (Mailchimp, SendGrid, vb.) yükleyebilir veya doğrudan HTML içeriği olarak kullanabilirsiniz.

## 🔧 Özelleştirme

### Renkleri Değiştirme

`template.html` dosyasındaki renk kodlarını düzenleyebilirsiniz:
- `#1a5f5f` - Ana arka plan
- `#2a7a7a` - Gün bölümleri
- `#ffd700` - Vurgu rengi

### İkonları Değiştirme

`events-data.json` dosyasındaki `clubIcon` alanlarını emoji veya ikon kodları ile değiştirebilirsiniz.

## 📞 Destek

Sorularınız için: www.sks.uskudar.edu.tr

## 📄 Lisans

Bu proje Üsküdar Üniversitesi için özel olarak geliştirilmiştir.

