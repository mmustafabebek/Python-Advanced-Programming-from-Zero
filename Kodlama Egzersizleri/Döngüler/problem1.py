"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

sayi = int(input("Bir sayı giriniz:"))
bolen = 0

for i in range(1,sayi):
    if(sayi % i == 0):
        bolen += i
    else:
        continue

if(bolen == sayi):
    print("Bu sayı bir mükemmel sayıdır.")
else:
    print("Bu sayı bir mükemmel sayı değildir.")

