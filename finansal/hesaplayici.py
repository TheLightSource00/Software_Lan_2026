# Finansal Analiz ve Hesaplama Aracı
# Yazarı: TheLightSource00

def kredi_hesapla(anapara, faiz_orani, vade):
    """Basit bir kredi geri ödeme hesaplayıcısı"""
    toplam_odeme = anapara + (anapara * (faiz_orani / 100) * vade)
    aylik_taksit = toplam_odeme / (vade * 12)
    return toplam_odeme, aylik_taksit

print("--- Bankacılık ve Finans Analiz Modülü ---")
ana = float(input("Kredi tutarını giriniz: "))
faiz = float(input("Yıllık faiz oranını (%) giriniz: "))
yil = int(input("Kaç yıl vade yapılacak?: "))

toplam, taksit = kredi_hesapla(ana, faiz, yil)

print(f"\nToplam Geri Ödeme: {toplam} TL")
print(f"Tahmini Aylık Taksit: {taksit:.2f} TL")
