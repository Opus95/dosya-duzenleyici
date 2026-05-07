# 🗂️  Dosya Düzenleyici

Bir klasördeki dosyaları otomatik olarak türlerine göre alt klasörlere taşıyan Python betiği.

---

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Desteklenen Dosya Türleri](#-desteklenen-dosya-türleri)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Örnek](#-örnek)


---

## ✨ Özellikler

- 📁 Dosyaları otomatik olarak kategorilere ayırır
- 🔒 Betiğin kendisini taşımaz
- ⚠️ Aynı isimde dosya varsa üzerine yazmaz, `_kopya` ekler
- 🖨️ Her taşınan dosya için konsola bilgi verir
- 🧹 `os.makedirs(..., exist_ok=True)` ile temiz klasör oluşturma

---

## 📂 Desteklenen Dosya Türleri

| Klasör      | Uzantılar                                           |
|-------------|-----------------------------------------------------|
| `Images`    | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg`          |
| `Documents` | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.pptx` `.csv` |
| `Audio`     | `.mp3` `.wav` `.aac` `.flac`                        |
| `Video`     | `.mp4` `.mkv` `.mov` `.avi`                         |
| `Archives`  | `.zip` `.rar` `.tar` `.gz` `.7z`                    |
| `Scripts`   | `.py` `.js` `.html` `.css` `.cpp` `.java`           |
| `Others`    | Yukarıdakilerin dışındaki tüm dosyalar              |

---

## ⚙️ Kurulum

**Gereksinimler:** Python 3.x (ek kütüphane gerekmez)

```bash
git clone https://github.com/kullanici-adi/dosya-duzenleyici.git
cd dosya-duzenleyici
```

---

## 🚀 Kullanım

```bash
python dosyadüzenleyici.py
```

Çalıştırdıktan sonra terminal senden bir klasör yolu ister:

```
Düzenlenecek klasörün tam yolunu girin: C:\Users\Kullanici\Desktop\Karisik
```

### İşletim Sistemine Göre Yol Örnekleri

| İşletim Sistemi | Örnek Yol                              |
|-----------------|----------------------------------------|
| Windows         | `C:\Users\Kullanici\Desktop\Karisik`   |
| macOS / Linux   | `/home/kullanici/Masaustu/Karisik`     |

---

## 📁 Örnek

**Önce:**
```
Karisik/
├── tatil.jpg
├── rapor.pdf
├── muzik.mp3
├── script.py
├── arsiv.zip
└── bilinmeyen.xyz
```

**Sonra:**
```
Karisik/
├── Images/
│   └── tatil.jpg
├── Documents/
│   └── rapor.pdf
├── Audio/
│   └── muzik.mp3
├── Scripts/
│   └── script.py
├── Archives/
│   └── arsiv.zip
└── Others/
    └── bilinmeyen.xyz
```

---


```




---



