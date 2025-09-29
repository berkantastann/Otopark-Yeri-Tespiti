# 🚗 Otopark Yeri Tespiti

![Demo](demo.gif)

Bilgisayarlı görü ve makine öğrenmesi kullanarak gerçek zamanlı otopark yerlerini tespit eden ve boş/dolu durumlarını sayan Python uygulaması.

## ✨ Özellikler

- 🎯 Gerçek zamanlı park yeri tespiti
- 📊 Boş/dolu park yeri sayacı
- 🎨 Görsel geri bildirim (yeşil: boş, kırmızı: dolu)
- 🤖 Makine öğrenmesi tabanlı sınıflandırma
- ⚡ Optimize edilmiş performans

## 🛠️ Teknoloji Stack

- **Python 3.x**
- **OpenCV** - Görüntü işleme ve video analizi
- **scikit-learn** - Makine öğrenmesi modeli
- **scikit-image** - Görüntü ön işleme
- **NumPy** - Sayısal hesaplamalar
- **Pandas** - Veri manipülasyonu
- **Matplotlib** - Görselleştirme

## 📋 Gereksinimler

```bash
pip install -r requirements.txt
```

## 🚀 Kullanım

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/Otopark-Yeri-Tespiti.git
cd Otopark-Yeri-Tespiti
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:
```bash
python main.py
```

4. Çıkmak için `q` tuşuna basın.

## 📁 Proje Yapısı

```
├── main.py          # Ana uygulama
├── util.py          # Yardımcı fonksiyonlar
├── model.p          # Eğitilmiş ML modeli
├── mask_1920_1080.png  # Park yeri maskeleri
├── requirements.txt    # Gerekli kütüphaneler
└── README.md          # Proje dokümantasyonu
```

## 🎯 Nasıl Çalışır?

1. **Mask İşleme**: Park yerlerinin konumları önceden tanımlanmış mask dosyasından alınır
2. **Frame Analizi**: Video karelerinde değişiklik tespiti yapılır
3. **ML Sınıflandırma**: Her park yeri için boş/dolu durumu makine öğrenmesi ile belirlenir
4. **Görselleştirme**: Sonuçlar renkli dikdörtgenler ile gösterilir

## 📊 Çıktı

- **Yeşil Dikdörtgen**: Boş park yeri
- **Kırmızı Dikdörtgen**: Dolu park yeri
- **Sayaç**: "Available spots: X / Y" formatında toplam bilgi

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE.md` dosyasına bakın.
