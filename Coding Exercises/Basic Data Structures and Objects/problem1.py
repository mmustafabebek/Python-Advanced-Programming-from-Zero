# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

a = int(input("Birinci sayi:"))
b = int(input("Ikinci sayi:"))
c = int(input("Ucuncu sayi:"))

carpim = a * b * c

print("Birinci sayi: {}\nIkinci sayi: {}\nUcuncu sayi: {}\nSayilarin carpimi: {}".format(a,b,c,carpim))