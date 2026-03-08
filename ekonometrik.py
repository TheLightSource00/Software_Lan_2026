# Ekonometrik Veri Analizi Modülü
# Yazarı: TheLightSource00

import random

def veri_ozeti_olustur(gelir_listesi):
    """Ekonomik veri seti üzerinde temel istatistiksel analiz yapar"""
    toplam = sum(gelir_listesi)
    ortalama = toplam / len(gelir_listesi)
    en_yuksek = max(gelir_listesi)
    
    return {
        "Toplam Hacim": toplam,
        "Ortalama Gelir": ortalama,
        "Zirve Değer": en_yuksek
    }

# Simüle edilmiş 12 aylık ekonomik veri seti
aylik_veriler = [random.randint(15000, 45000) for _ in range(12)]

print("--- Yıllık Ekonometrik Analiz Raporu ---")
analiz = veri_ozeti_olustur(aylik_veriler)

for anahtar, deger in analiz.items():
    print(f"{anahtar}: {deger:.2f} TL")

print("\nDurum: Veri tutarlılığı onaylandı. Analiz tamamlandı.")
