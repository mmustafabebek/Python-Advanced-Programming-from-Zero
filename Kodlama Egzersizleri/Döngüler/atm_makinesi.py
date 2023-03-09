print("""***************************************

Atm Makinesine Hoşgeldiniz.

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekma

Programdan çıkmak için 'q' ya basın.
***************************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi seçiniz:")

    if(islem == "q"):
        print("Yine bekleriz")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if(miktar > bakiye):
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem...")