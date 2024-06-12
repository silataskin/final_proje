from Personel import Personel
class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def get_calisma_saati(self):
        return self.__calisma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def get_sertifika(self):
        return self.__sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_hastane(self):
        return self.__hastane

    def __str__(self):
        return (f"Hemşire Bilgileri:\n"
                f"Personel No: {self.get_personel_no()}\n"
                f"Ad: {self.get_ad()}\n"
                f"Soyad: {self.get_soyad()}\n"
                f"Departman: {self.get_departman()}\n"
                f"Maas: {self.get_maas()}\n"
                f"Çalışma Saati: {self.__calisma_saati}\n"
                f"Sertifika: {self.__sertifika}\n"
                f"Hastane: {self.__hastane}")

    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (oran + 1 / 100)
        self.set_maas(yeni_maas)


