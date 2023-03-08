# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a = float(input("Birinci Sayı:"))
b = float(input("Üçüncü Sayı:"))
c = float(input("İkinci Sayı:"))

if (a > b and a > c):
    print("En büyük sayı {} dır.".format(a))
elif (b > a and b > c):
    print("En büyük sayı {} dır.".format(b))
elif (c > a and c > b):
    print("En büyük sayı {}".format(c))
