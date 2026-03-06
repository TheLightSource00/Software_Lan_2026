# Veri Yapıları ve Algoritma Temelleri
# Bu dosya akademik gelisim sürecimi temsil eder.

class AkademikGelisim:
    def __init__(self):
        self.profil = {
            "durum": "Cift Universite",
            "hedef": "AI & Big Data Expert",
            "plan": "Bahar dönemi sonu AI Camp başlangıcı"
        }
      
    def hedef_goster(self):
        # Mevcut akademik hedefleri ekrana yazdırır
        for anahtar , deger in self.profil.items():
          print (f"{anahtar.capitalize()}: {deger}")

if__name__ == "__main__":
   gelişim = AkademikGelisim()
   gelişim.hedef_goster()
