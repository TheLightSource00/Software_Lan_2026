# Veri Yapıları ve Algoritma Temelleri
# Bu dosya akademik gelişim sürecimi temsil eder.

class AkademikGelişim:
    def __init__(self):
        self.profil = {
            "durum": "Çift Üniversite",
            "hedef": "AI & Big Data Expert",
            "plan": "Bahar dönemi sonu AI Camp başlangıcı"
        }
      
    def hedef_goster(self):
        # Mevcut akademik hedefleri ekrana yazdırır
        for anahtar , deger in self.profil.items():
          print (f"{anahtar.capitalize()}: {deger}")

if__name__ == "__main__":
   gelişim = AkademikGelişim()
   gelişim.hedef_goster()
