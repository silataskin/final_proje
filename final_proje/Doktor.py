from Personel import Personel
class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_uzmanlik(self):
        return self.__uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_hastane(self):
        return self.__hastane

    def __str__(self):
        return (f"Doktor Bilgileri: \n"
                f"Personel No: {self.get_personel_no()} \n"
                f"Ad: {self.get_ad()} \n"
                f"Soyad: {self.get_soyad()} \n"
                f"Departman: {self.get_departman()} \n"
                f"Maas: {self.get_maas()} \n"
                f"Uzmanlık: {self.__uzmanlik} \n"
                f"Deneyim Yılı: {self.__deneyim_yili} \n"
                f"Hastane: {self.__hastane}")

    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (oran + 1 / 100)
        self.set_maas(yeni_maas)


