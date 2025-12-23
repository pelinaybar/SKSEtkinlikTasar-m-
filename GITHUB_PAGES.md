# GitHub Pages'e Yayınlama Rehberi

Bu projeyi GitHub Pages'te yayınlamak için aşağıdaki adımları izleyin:

## 1. GitHub Repository Oluşturma

1. GitHub'da yeni bir repository oluşturun
2. Repository adını belirleyin (örn: `etkinlik-tasarim-sistemi`)

## 2. Dosyaları Yükleme

Aşağıdaki dosyaları repository'ye yükleyin:

```
├── index.html          (Ana dosya - MUTLAKA olmalı)
├── logos/              (Logo klasörü)
│   ├── üülogo.png
│   ├── SKS LOGO.png
│   └── ... (diğer logo dosyaları)
└── README.md           (Opsiyonel)
```

## 3. GitHub Pages'i Aktifleştirme

1. Repository sayfasında **Settings** sekmesine gidin
2. Sol menüden **Pages** seçeneğine tıklayın
3. **Source** bölümünden **Deploy from a branch** seçin
4. **Branch** olarak **main** (veya **master**) seçin
5. **Folder** olarak **/ (root)** seçin
6. **Save** butonuna tıklayın

## 4. Site URL'i

Birkaç dakika sonra siteniz şu formatta yayınlanacak:
```
https://[kullanıcı-adınız].github.io/[repository-adı]/
```

## 5. Logo Yönetimi

### Logo Ekleme

1. Logo dosyalarını `logos/` klasörüne ekleyin
2. Dosya adlarında Türkçe karakter ve boşluk kullanmayın (sistem otomatik düzenler)
3. Önerilen boyut: **300x300 piksel** (1:1 kare format)
4. Format: **PNG** (şeffaf arka plan önerilir)

### Logo Yönetim Paneli

1. Sitede **"Logo Yönetim Paneli"** butonuna tıklayın
2. Kulüp seçin
3. Logo dosyasını yükleyin (sürükle-bırak veya tıklayarak)
4. Dosya adını kontrol edin
5. **Kaydet** butonuna tıklayın

### GitHub için Logo Export (ÖNEMLİ!)

**Herkesin aynı logoları görmesi için:**

1. Logo Yönetim Paneli'nde tüm logoları yükleyip kaydedin
2. **"JSON'a Aktar (GitHub için)"** butonuna tıklayın
3. İndirilen `logos.json` dosyasını repository'nizin **ana dizinine** yükleyin
4. Commit ve push edin

**Önemli:** `logos.json` dosyası base64 logoları içerir. Bu sayede:
- ✅ Herkes aynı logoları görür
- ✅ logos/ klasöründeki dosyalar yoksa bile logolar çalışır
- ✅ GitHub Pages'te sorunsuz çalışır

### Header Logoları (ÜÜ / SKS)

Header (üst) logolarını da herkesin görmesi için:
1. Logo Yönetim Paneli’nde **Header Logoları (ÜÜ / SKS)** bölümünden logoları yükleyin
2. Ardından **JSON’a Aktar** yapın
3. `logos.json` dosyasını repo’ya koyun

`logos.json` artık `header.uu` ve `header.sks` alanlarını da içerir.

**Dosya Yapısı:**
```
repository/
├── index.html
├── logos.json          ← Bu dosyayı ekleyin!
└── logos/
    ├── üülogo.png
    └── ...
```

## 6. Önemli Notlar

- ✅ Logo dosyaları `logos/` klasöründe olmalı
- ✅ Logo yönetim panelinden yüklenen logolar base64 olarak kaydedilir
- ✅ Base64 logolar GitHub Pages'te de çalışır (logos/ klasöründeki dosya yoksa)
- ✅ LocalStorage/IndexedDB verileri tarayıcıda saklanır (farklı cihazlarda senkronize olmaz)
- ✅ Logo eşleştirmeleri LocalStorage'da saklanır
- ✅ Paylaşımlı kullanım için `logos.json` dosyasını repo’da tutun (tek kaynak bu)

## 7. Sorun Giderme

### Logolar görünmüyor

1. Logo dosyalarının `logos/` klasöründe olduğundan emin olun
2. Dosya adlarının doğru olduğunu kontrol edin
3. Logo Yönetim Paneli'nden logo eşleştirmesini kontrol edin
4. Tarayıcı konsolunu kontrol edin (F12)

### Base64 Logolar

Logo yönetim panelinden yüklenen logolar otomatik olarak base64'e çevrilir ve LocalStorage'a kaydedilir. Bu sayede logos/ klasöründeki dosya yoksa bile logo görünür.

## 8. Güncelleme

Repository'ye yeni dosya ekledikten sonra:
1. Değişiklikleri commit edin
2. Push edin
3. Birkaç dakika bekleyin (GitHub Pages otomatik güncellenir)

---

**İyi çalışmalar! 🚀**

