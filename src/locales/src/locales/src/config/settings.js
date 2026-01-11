// Hastane İsmi ve Sistem Ayarları
const AppSettings = {
    // KURAL: Eğer kullanıcı ismi değiştirmezse bu isim kalıcıdır.
    defaultHospitalName: "Merkez Hastanesi", 
    
    // Tarayıcı hafızasından veya varsayılandan ismi getirir
    getHospitalName: function() {
        return localStorage.getItem("hospital_name") || this.defaultHospitalName;
    },

    // Sistem dili ayarı
    currentLang: localStorage.getItem("app_lang") || "TR"
};

export default AppSettings;
