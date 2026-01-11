# 🧪 VitalGuard - Private R&D Lab (V1)
> **Not:** Bu sayfa ana vizyondan bağımsız, teknik geliştirme alanıdır.

## 🧠 AI Kamera & Nabız Takibi (rPPG)
Bu bölümde kameradan gelen ışık verisini analiz ediyoruz:
- Hedef: 30 FPS görüntü işleme.
- Yüz tespiti ve yeşil kanal analizi aktif.

## 🏥 Hospital Branding (Özel Kural Testi)
- [x] Kural 1: Hastane ismi boşsa "Merkez Hastanesi" kalır.
- [ ] Kural 2: TR/EN dil seçeneği dashboard'da sabitlenir.

## 🛠️ Gelecek Planı (Gizli Mod)
1. AI Kamera ile Bio-Ohm verisini tek bir "Risk Skoru"na dönüştür.
2. Acil durum butonunu "Sesli Komut" ile çalışacak hale getir.
# 🧠 VitalGuard Decision Engine (Zeka Katmanı)
# Amacı: İki farklı veriyi yorumlayıp hastaneye bildirim göndermek.

def analyze_risk(bpm, ohm_value):
    # Senin Kuralın: Hastane ismi her zaman sabit kalmalı.
    hospital_name = "Merkez Hastanesi" 
    
    # Eşik Değerleri
    CRITICAL_BPM = 110      # Nabız 110 üstü riskli
    EDEMA_THRESHOLD = 400   # Ohm değeri 400 altı (sıvı artışı/direnç düşüşü)

    if bpm > CRITICAL_BPM and ohm_value < EDEMA_THRESHOLD:
        status = "🔴 KRİTİK: Acil Müdahale Gerekli!"
        action = "Hastaneye ve Yakınlarına Konum Gönderiliyor..."
    elif ohm_value < EDEMA_THRESHOLD:
        status = "🟡 UYARI: Ödem Belirtisi."
        action = "Tuz tüketimini kısıtlayın ve dinlenin."
    else:
        status = "🟢 STABİL: Durum Normal."
        action = "Takibe devam ediliyor."

    return f"[{hospital_name}] Durum Raporu: {status} | Aksiyon: {action}"

# Örnek Test: Nabız 115, Ohm 350 (Kritik Durum)
# print(analyze_risk(115, 350))
Bileşen,Konum,Kural
Hastane Adı,Sol Üst,"Değiştirilmedikçe ""Merkez Hastanesi"" yazar."
Dil Seçeneği,Sağ Üst,EN / TR bayrakları (Tıklandığında anlık çeviri).
AI Kamera,Orta Panel,Yüz çevresi yeşil kare; nabız grafiği altında.
Ohm Grafiği,Alt Panel,% düşüşü gösteren bar (Kırmızı/Yeşil).
AI Face Tracking Logic:Detection: Haar-Cascades veya MediaPipe kullanılarak yüz koordinatları ($x, y, w, h$) belirlenir.ROI (Region of Interest): Alın bölgesi, ışık yansıması ve damar yoğunluğu nedeniyle "Sinyal Odak Noktası" olarak seçilir.Filtering: Ortam ışığındaki titremeler (noise), "Band-pass filter" ile temizlenerek sadece $0.75\text{ Hz} - 4\text{ Hz}$ (45-240 BPM arası) frekanslar kabul edilir.

