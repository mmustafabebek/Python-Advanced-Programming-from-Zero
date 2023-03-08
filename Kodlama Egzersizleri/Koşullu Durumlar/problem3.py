"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

vize1 = float(input("Birinci vize notunuz:"))
vize2 = float(input("İkinci vize notunuz:"))
final = float(input("Final notunuz:"))

toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

if(toplam_not >= 90):
    print("AA")
elif(toplam_not >= 85):
    print("BA")
elif(toplam_not >= 80):
    print("BB")
elif(toplam_not >= 75):
    print("CB")
elif(toplam_not >= 70):
    print("CC")
elif(toplam_not >= 65):
    print("DC")
elif(toplam_not >= 60):
    print("DD")
elif(toplam_not >= 55):
    print("FD")
elif(toplam_not < 55):
    print("FF")
