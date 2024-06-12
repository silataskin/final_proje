class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def get_hasta_no(self):
        return self.__hasta_no

    def set_ad(self, ad):
        self.__ad = ad

    def get_ad(self):
        return self.__ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_soyad(self):
        return self.__soyad

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def get_hastalik(self):
        return self.__hastalik

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def get_tedavi(self):
        return self.__tedavi

    def __str__(self):
        return (f"Hasta Bilgileri:\n"
                f"Hasta No: {self.__hasta_no}\n"
                f"Ad: {self.__ad}\n"
                f"Soyad: {self.__soyad}\n"
                f"Doğum Tarihi: {self.__dogum_tarihi}\n"
                f"Hastalık: {self.__hastalik}\n"
                f"Tedavi: {self.__tedavi}")

    def tedavi_suresi_hesapla(self):

        harf_sayisi = len(self.__hastalik)

        if harf_sayisi <= 3:
            derece = "Hafif"
        elif harf_sayisi <= 6:
            derece = "Orta"
        else:
            derece = "Ciddi"

        if derece == "Hafif":
            tedavi_suresi_gun = 3
        elif derece == "Orta":
            tedavi_suresi_gun = 5
        else:
            tedavi_suresi_gun = 7

        return tedavi_suresi_gun



