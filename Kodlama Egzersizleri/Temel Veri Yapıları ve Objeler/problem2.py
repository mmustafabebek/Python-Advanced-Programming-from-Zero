# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy = float(input("Boy bilginizi giriniz:"))
kilo = int(input("Kilo bilginizi giriniz:"))

bedenkitleindeksi = input("Beden Kitle İndeksiniz: {}\n".format(kilo / boy ** 2))