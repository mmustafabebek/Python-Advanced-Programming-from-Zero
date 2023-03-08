"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

print("""**************************************************
Beden Kitle Endeksi Hesaplayıcı
**************************************************""")

boy = float(input("Boyunuz:"))
kilo = float(input("Kilonuz:"))

beden_kitle_indeksi = kilo / (boy * boy)

if (beden_kitle_indeksi < 18.5):
    print("Zayıf")
elif (18.5 <= beden_kitle_indeksi and beden_kitle_indeksi < 25):
    print("Normal")
elif (25 <= beden_kitle_indeksi and beden_kitle_indeksi < 30):
    print("Fazla Kilolu")
elif (beden_kitle_indeksi > 30):
    print("Obez")
