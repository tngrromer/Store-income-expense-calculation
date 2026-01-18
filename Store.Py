def satis_hesapla(satis_adet, birim_fiyat):
    return satis_adet * birim_fiyat

def gider_hesapla(giderler):
    toplam_gider = sum(giderler)
    return toplam_gider

# Günlük satış verileri
fiziksel_satis_adet = 50
eticaret_satis_adet = 100
birim_fiyat = 2000 # Her bir ürünün fiyatı

# Günlük Giderler
fiziksel_magaza_giderleri = [300, 500, 200] #Elektrik, kira, personel
eticaret_site_giderleri = [150, 100, 250] #Hosting, reklam, yazılım

# Satış ve gider hesaplamaları
fiziksel_satis_tutari = satis_hesapla(fiziksel_satis_adet, birim_fiyat)
eticaret_satis_tutari = satis_hesapla(eticaret_satis_adet, birim_fiyat)

fiziksel_magaza_toplam_gider = gider_hesapla(fiziksel_magaza_giderleri)
eticaret_magaza_toplam_gider = gider_hesapla(eticaret_site_giderleri)

# Günlük toplam kar
kar = (fiziksel_satis_tutari + eticaret_satis_tutari) - (fiziksel_magaza_toplam_gider + eticaret_magaza_toplam_gider)

print("Fiziksel mağaza satış tutarı :", fiziksel_satis_tutari)
print("E-ticaret mağaza satış tutarı :", eticaret_satis_tutari)
print("Fiziksel mağaza giderleri :", fiziksel_magaza_giderleri)
print("E-ticaret mağagza giderleri :", eticaret_site_giderleri)
print("Günlük kar :" , kar)
