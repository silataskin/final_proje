import pandas as pd   #Gerekli kütüphaneleri tanımlama
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

try:  #Hataları kontrol

        #Personel nesnelerini oluşturma
        personel1 = Personel("P520", "Ali", "Kara", "Hizmetli", 8000)
        personel2 = Personel("P293", "İrem", "Işık", "Sekreter", 10000)

        #Doktor nesnelerini oluşturma
        doktor1 = Doktor("D647", "Sıla", "Taşkın", "Kardiyoloji", 25000, "Kalp Cerrahisi", 10, "İzmir Şehir Hastansi")
        doktor2 = Doktor("D182", "Ege", "Çetin", "Kulak Burun Boğaz", 21000, "Ağız ve Boğaz Uzmanı", 8, "Dokuz Eylül Hastanesi")
        doktor3 = Doktor("D983", "Ayşegül", "Beyaz", "Üroloji", 18000, "Üroloji Uzmanı", 6, "Ege Üniversitesi Hastane")

        #Hemşire nesnelerini oluşturma
        hemsire1 = Hemsire("H643", "Merve", "Girgin", "Psikiyatri", 20000, 7, "Psikiyatri Hemşireliği", "İzmir Şehir Hastanesi")
        hemsire2 = Hemsire("H748", "Eylül", "Öz", "Pediatri", 15000, 6, "Pediatri Hemşireliği", "Ege Üniversitesi Hastanesi")
        hemsire3 = Hemsire("H276", "Alpay", "Yılmaz", "Acil", 12000, 9, "Yoğun Bakım Hemşireliği", "İzmir Şehir Hastanesi")

        #Hasta nesnelerini oluşturma
        hasta1 = Hasta("H380", "Ahmet", "Uygur", "23.06.1987", "Grip", "İlaç Kullanımı")
        hasta2 = Hasta("H474", "Melike", "Karaca", "16.11.1993", "Gastrit", "İlaç Kullanımı")
        hasta3 = Hasta("H594", "Mehmet", "Kaya", "24.09.1975", "Çarpıntı", "Dinlenme ve İlaç Kullanımı")

        #Tüm nesneleri listelere ekleme
        personel_listesi = [personel1, personel2]
        doktor_listesi = [doktor1, doktor2, doktor3]
        hemsire_listesi = [hemsire1, hemsire2, hemsire3]
        hasta_listesi = [hasta1, hasta2, hasta3]


        def print_info(label, obj):   #tüm bilgileri yazdır
            if isinstance(obj, Personel):
                print(f"{label} = Personel No: {obj.get_personel_no()}, Ad: {obj.get_ad()}, Soyad: {obj.get_soyad()}, "
                      f"Departman: {obj.get_departman()}, Maaş: {obj.get_maas()}")
            elif isinstance(obj, Doktor):
                print(f"{label} = Personel No: {obj.get_personel_no()}, Ad: {obj.get_ad()}, Soyad: {obj.get_soyad()}, "
                      f"Departman: {obj.get_departman()}, Maaş: {obj.get_maas()}, Uzmanlık: {obj.get_uzmanlik()}, "
                      f"Deneyim Yılı: {obj.get_deneyim_yili()}, Hastane: {obj.get_hastane()}")
            elif isinstance(obj, Hemsire):
                print(f"{label} = Personel No: {obj.get_personel_no()}, Ad: {obj.get_ad()}, Soyad: {obj.get_soyad()}, "
                      f"Departman: {obj.get_departman()}, Maaş: {obj.get_maas()}, Çalışma Saati: {obj.get_calisma_saati()}, "
                      f"Sertifika: {obj.get_sertifika()}, Hastane: {obj.get_hastane()}")
            elif isinstance(obj, Hasta):
                print(f"{label} = Hasta No: {obj.get_hasta_no()}, Ad: {obj.get_ad()}, Soyad: {obj.get_soyad()}, "
                      f"Doğum Tarihi: {obj.get_dogum_tarihi()}, Hastalık: {obj.get_hastalik()}, Tedavi: {obj.get_tedavi()}")


        # Tüm bilgileri yazdırma
        print("Tüm bilgiler:")
        for i, p in enumerate(personel_listesi, 1):
            print_info(f"Personel{i}", p)
        for i, d in enumerate(doktor_listesi, 1):
            print_info(f"Doktor{i}", d)
        for i, h in enumerate(hemsire_listesi, 1):
            print_info(f"Hemşire{i}", h)
        for i, h in enumerate(hasta_listesi, 1):
            print_info(f"Hasta{i}", h)

        #Personel nesnelerinden veri listesi oluşturma
        personel_veri = [{"personel_no": p.get_personel_no(), "ad": p.get_ad(), "soyad": p.get_soyad(),
                  "departman": p.get_departman(), "maas": p.get_maas()} for p in personel_listesi]

        #Doktor nesnelerinden veri listesi oluşturma
        doktor_veri = [{"personel_no": d.get_personel_no(), "ad": d.get_ad(), "soyad": d.get_soyad(),
                "departman": d.get_departman(), "maas": d.get_maas(), "uzmanlik": d.get_uzmanlik(),
                "deneyim_yili": d.get_deneyim_yili(), "hastane": d.get_hastane()} for d in doktor_listesi]

        #Hemşire nesnelerinden veri listesi oluşturma
        hemsire_veri = [{"personel_no": h.get_personel_no(), "ad": h.get_ad(), "soyad": h.get_soyad(),
                 "calisma_saati": h.get_calisma_saati(), "sertifika": h.get_sertifika(),
                 "hastane": h.get_hastane()} for h in hemsire_listesi]

        #Hasta nesnelerinden veri listesi oluşturma
        hasta_veri = [{"hasta_no": h.get_hasta_no(), "ad": h.get_ad(), "soyad": h.get_soyad(),
               "dogum_tarihi": h.get_dogum_tarihi(), "hastalik": h.get_hastalik(),
               "tedavi": h.get_tedavi()} for h in hasta_listesi]

        #DataFrame oluşturma
        personel_df = pd.DataFrame(personel_veri)
        doktor_df = pd.DataFrame(doktor_veri)
        hemsire_df = pd.DataFrame(hemsire_veri)
        hasta_df = pd.DataFrame(hasta_veri)

        #Boş olan değişkenlere 0 atama
        personel_df.fillna(0, inplace=True)
        doktor_df.fillna(0, inplace=True)
        hemsire_df.fillna(0,inplace=True)
        hasta_df.fillna(0, inplace=True)


        #Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama ve yazdırma
        doktor_grup = doktor_df.groupby('uzmanlik').size()
        print("Doktorların uzmanlık alanlarına göre gruplandırılmış toplam sayıları:")
        print(doktor_grup)


        #5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
        deneyimli_doktor_sayisi = doktor_df[doktor_df["deneyim_yili"] > 5].shape[0]
        print("5 yıldan fazla deneyime sahip doktorların toplam sayısı:", deneyimli_doktor_sayisi)

        #Hasta adına göre DataFrame’i alfabetik olarak sıralama ve yazdırma
        hasta_df_sirali = hasta_df.sort_values(by="ad")
        print("Hasta adına göre alfabetik olarak sıralanmış DataFrame:\n", hasta_df_sirali)

        #Maaşı 7000 TL üzerinde olan personelleri bulma ve yazdırma
        yuksek_maas_personel = personel_df[personel_df["maas"] > 7000]
        print("Maaşı 7000 TL üzerinde olan personeller:\n", yuksek_maas_personel)

        #Doğum tarihi 1990 ve sonrası olan hastaları gösterme ve yazdırma
        genc_hastalar = hasta_df[hasta_df["dogum_tarihi"].str.split(".").str[-1].astype(int) >= 1990]
        print("Doğum tarihi 1990 ve sonrası olan hastalar:\n", genc_hastalar)

        #Tüm verilerle  yeni DataFrame oluşturma
        yeni_df = pd.concat([personel_df, doktor_df, hemsire_df, hasta_df], ignore_index=True)

        print("Yeni DataFrame:\n", yeni_df)

except Exception as e:  # Hatayı ve hatanın türünü bulmamıza yardımcı oluyor.
    print("Bir hata oluştu:", str(e))





