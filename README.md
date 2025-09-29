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

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

- **Python 3.x** - Ana programlama dili
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
