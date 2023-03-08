"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
"""

sayi = input("Tipini bulmak istediğiniz çokgeni seçiniz.\n1.Üçgen\n2.Dörtgen\n")

if(sayi == "1"):
    a = float(input("Birinci kenarı giriniz:"))
    b = float(input("İkinci kenarı giriniz:"))
    c = float(input("Üçüncü kenarı giriniz:"))
    if(abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and b == c):
            print("Bu üçgen eşkenardır.")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Bu üçgen ikizkenardır.")
        else:
            print("Bu üçgen çeşitkenardır.")
    else:
        print("Üçgen belirtmiyor.")
elif(sayi == "2"):
    a = float(input("Birinci kenarı giriniz:"))
    b = float(input("İkinci kenarı giriniz:"))
    c = float(input("Üçüncü kenarı giriniz:"))
    d = float(input("Dördüncü kenarı giriniz:"))
    if(a == b and b == c and c == d):
        print("Bu dörtgen karedir.")
    elif((a == b and c == d) or (a == c and b == d) or (a == d and b == c)):
        print("Bu dörtgen dikdörtgendir.")
    else:
        print("Bu dörtgen sıradan bir dörtgendir.")
