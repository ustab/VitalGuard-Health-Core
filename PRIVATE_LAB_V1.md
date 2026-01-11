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
```python
## 🛠️ Modül 3: Dil ve Kimlik Motoru (Kod Taslağı)
> **Kural:** Hastane adı değiştirilmedikçe "Merkez Hastanesi" kalır.

```python
class UIController:
    def __init__(self, hospital_name="Merkez Hastanesi"):
        self.hospital_identity = hospital_name
        self.current_lang = "TR"
        
        self.translations = {
            "TR": {"welcome": "Hoş geldiniz", "pulse": "Nabız"},
            "EN": {"welcome": "Welcome", "pulse": "Heart Rate"}
        }

    def render(self):## 📁 Modül 4: Hastane Entegrasyonu (JSON Data Package)
> **Senaryo:** Risk Analiz Motoru "Kritik" kararı verdiğinde, bulut sistemine aşağıdaki paket gönderilir.
}
        return f"{self.hospital_identity} | {self.translations[self.current_lang]['welcome']}"

### 🚀 Acil Durum Veri Paketi Yapısı
```python
```json
{
  "hospital_id": "Merkez Hastanesi",
  "timestamp": "2026-01-11T12:10:00Z",
  "patient_status": {
    "risk_level": "CRITICAL",
    "language_preference": "TR"
  },
  "vital_signs": {
    "heart_rate_bpm": 112,
    "ai_camera_confidence": 0.94,
    "bio_ohm_resistance": 385,
    "edema_index": "%22 Increase"
  },
  "location": {
    "home_address": "Private_Encrypted_Data",
    "gps": "41.0082, 28.9784"
  }

## 🖼️ Modül 5: Master Dashboard (Görsel Tasarım Planı)
> **Hedef:** Verilerin karmaşadan uzak, hayati bilgiyi öne çıkaracak şekilde sunulması.

### 📐 Ekran Yerleşim Şeması (Wireframe)

| Üst Bar (Header) | Sol Panel (Vital) | Sağ Panel (Grafik) |
| :--- | :--- | :--- |
| **[🏥 Merkez Hastanesi]** | **[📷 AI Kamera View]** | **[📈 Nabız Trendi]** |
| (Sabit Branding) | (Yüz Takibi & ROI) | (Son 24 Saat) |
| **[🌐 TR / EN]** | **[💓 Anlık BPM: 72]** | **[🌊 Ödem İndeksi]** |
| (Dil Değiştirici) | (Büyük Dijital Rakam) | (% Değişim Çizelgesi) |

### 🎨 Görsel Kurallar (UI Rules)
1. **Renk Kodları:** - Normal: Yeşil (#2ECC71)
   - Uyarı: Sarı (#F1C40F)
   - Kritik: Kırmızı (#E74C3C)
2. **Hastane İsmi:** Yazılımın `config` dosyasından okunur, kullanıcı müdahalesiyle dashboard üzerinden değiştirilemez.
3. **Dil:** Tek tıkla tüm etiketler (BPM -> Nabız, Status -> Durum vb.) anlık güncellenir.
## 🎙️ Modül 6: Sesli Komut ve Acil Tetikleme (Voice Assist)
> **Senaryo:** Hasta fiziksel olarak cihaza dokunamadığında, belirli anahtar kelimelerle sistemi aktive eder.

### 🛠️ Teknik Altyapı
- **Kütüphane:** SpeechRecognition (Python) / Web Speech API
- **Anahtar Kelimeler (Trigger Words):** - [TR]: "Yardım et", "Fenalaştım", "Acil durum"
  - [EN]: "Help me", "Emergency", "I feel sick"

### 📜 Sesli Komut Algoritması (Kod Taslağı)
```python
def listen_for_emergency(audio_input):
    # Senin kuralın: Çift dil desteği burada da aktif.
    triggers = {
        "TR": ["yardım et", "acil durum", "fenalaştım"],
        "EN": ["help me", "emergency", "i feel sick"]
    }
    
    command = audio_input.lower()
    
    # Her iki dilde de kontrol et
    if any(word in command for word in triggers["TR"] + triggers["EN"]):
        return trigger_emergency_protocol()
    return "Listening..."

def trigger_emergency_protocol():
    # Hastane ismini sabit tutarak alarm gönder
    hospital = "Merkez Hastanesi"
    return f"🚨 {hospital}: Acil durum protokolü sesli komutla başlatıldı!"

## 🎬 Modül 7: Video Lansman Senaryosu (Final)
Zaman,Görüntü (Visual),Ses/Metin (Audio/Text)
00:00 - 05:00,"Karanlık bir ekran, ortada şık bir logo. Üstte sabit: Merkez Hastanesi.","Derin bir nefes sesi. ""Geleceğin sağlık takibi, dokunmadan başlıyor."""
05:00 - 15:00,"Ekran ikiye bölünür. Sol tarafta bir kullanıcının yüzü, üzerinde yeşil bir tarama karesi (AI Kamera). Sağda ""Nabız: 72 BPM"" yazısı belirir.","""AI rPPG teknolojisiyle, sadece kameraya bakarak hayati verilerinizi ölçün."""
15:00 - 30:00,"Ekranın sağ alt köşesinde bir bar grafiği yükselir: ""Ödem İndeksi (Bio-Ohm)"". Sağ üstteki TR/EN butonu yanıp söner ve dil anlık olarak İngilizceye döner (Heart Rate, Edema Index).","""Dil engellerini kaldırın, kurumsal kimliğinizi koruyun. Tam entegre sağlık paneli."""
30:00 - 45:00,"Kullanıcı ""Yardım et!"" (veya ""Help me!"") diye fısıldar. Ekranda mavi ses dalgaları yayılır. Bir anda ekranın her yeri kırmızı bir çerçeveyle kaplanır: 🚨 ACİL DURUM BİLDİRİMİ.","""Sesli komutla hayat kurtaran müdahale. Sistem otomatik olarak hastaneye veri paketini gönderiyor."""
45:00 - 60:00,"Ekranda bir JSON veri paketinin hızlıca aktığı görülür. Video, Merkez Hastanesi logosu ve ""VitalGuard: Her An Yanınızda"" sloganıyla biter.","""VitalGuard. Güven, teknolojiyle buluşuyor."""
