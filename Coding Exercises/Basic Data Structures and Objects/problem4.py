# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = input("Adınızı giriniz:")
soyad = input("Soyadınızı giriniz:")
numara = input("Numaranızı giriniz:")

bilgiler = [ad,soyad,numara]

print("\nAdınız: {}\nSoyadınız: {}\nNumaranız: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))